"""
EscalationHandler - Handles escalation to human agent
"""
import json
import os
from datetime import datetime
from typing import Optional
from src.models.response import Response


class EscalationHandler:
    """
    Handler for escalating conversation to human agent.
    Collects customer phone number and saves escalation request.
    """
    
    def __init__(self):
        """Initialize escalation handler."""
        self.escalations_file = "data/escalations.json"
        self._ensure_data_file()
    
    def _ensure_data_file(self) -> None:
        """Ensure the escalations data file exists."""
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.escalations_file):
            with open(self.escalations_file, 'w') as f:
                json.dump([], f)
    
    def _generate_escalation_id(self) -> str:
        """
        Generate unique escalation ID.
        
        Returns:
            str: Escalation ID in format ESC-XXXXX
        """
        try:
            with open(self.escalations_file, 'r') as f:
                escalations = json.load(f)
                next_id = len(escalations) + 1
                return f"ESC-{next_id:05d}"
        except Exception:
            return "ESC-00001"
    
    def _validate_phone_number(self, phone: str) -> bool:
        """
        Validate phone number format.
        
        Args:
            phone (str): Phone number to validate
            
        Returns:
            bool: True if valid format
        """
        # Remove common separators and plus sign
        cleaned = phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "").replace("+", "")
        
        # Check if it's all digits and has reasonable length (10-15 digits)
        return cleaned.isdigit() and 10 <= len(cleaned) <= 15
    
    def _save_escalation(self, customer_name: str, phone: str, reason: str) -> str:
        """
        Save escalation request to file.
        
        Args:
            customer_name (str): Customer name
            phone (str): Customer phone number
            reason (str): Reason for escalation
            
        Returns:
            str: Generated escalation ID
        """
        escalation_id = self._generate_escalation_id()
        
        escalation = {
            "escalation_id": escalation_id,
            "customer_name": customer_name,
            "phone_number": phone,
            "reason": reason,
            "status": "Pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            with open(self.escalations_file, 'r') as f:
                escalations = json.load(f)
            
            escalations.append(escalation)
            
            with open(self.escalations_file, 'w') as f:
                json.dump(escalations, f, indent=2)
            
            return escalation_id
        except Exception as e:
            raise Exception(f"Failed to save escalation: {str(e)}")
    
    def handle(self, customer_name: str, phone: str, reason: Optional[str] = None) -> Response:
        """
        Handle escalation request.
        
        Args:
            customer_name (str): Customer name
            phone (str): Customer phone number
            reason (Optional[str]): Reason for escalation
            
        Returns:
            Response: Response object confirming escalation
        """
        # Validate phone number
        if not self._validate_phone_number(phone):
            return Response(
                text="❌ Invalid phone number format. Please enter a valid phone number (10-15 digits)."
            )
        
        # Use default reason if not provided
        if not reason:
            reason = "Customer requested human agent assistance"
        
        try:
            # Save escalation
            escalation_id = self._save_escalation(customer_name, phone, reason)
            
            message = f"""✅ Escalation Request Submitted Successfully!

📋 Escalation ID: {escalation_id}
👤 Name: {customer_name}
📞 Phone: {phone}

A human agent will contact you shortly at the provided number.
Estimated wait time: 5-10 minutes

Thank you for your patience!"""
            
            return Response(text=message)
        
        except Exception as e:
            return Response(
                text=f"❌ Failed to submit escalation request: {str(e)}"
            )
