"""
TicketHandler - Handles support ticket creation
"""
import os
import json
from datetime import datetime
from typing import Any, Dict
from src.models.context import Context
from src.models.response import Response


class TicketHandler:
    """
    Handler for support ticket creation intent.
    Saves support tickets to a JSON file.
    """
    
    def __init__(self):
        """Initialize ticket handler."""
        # Get the data directory path
        self.data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        self.tickets_file = os.path.join(self.data_dir, 'tickets.json')
        
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Initialize tickets file if it doesn't exist
        if not os.path.exists(self.tickets_file):
            with open(self.tickets_file, 'w') as f:
                json.dump([], f, indent=2)
    
    def _generate_ticket_id(self) -> str:
        """
        Generate a unique ticket ID.
        
        Returns:
            str: Ticket ID in format TKT-XXXXX
        """
        # Read existing tickets to get the next ID
        try:
            with open(self.tickets_file, 'r') as f:
                tickets = json.load(f)
                next_id = len(tickets) + 1
        except:
            next_id = 1
        
        return f"TKT-{next_id:05d}"
    
    def _save_ticket(self, ticket: Dict[str, Any]) -> bool:
        """
        Save ticket to JSON file.
        
        Args:
            ticket (Dict): Ticket data
            
        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            # Read existing tickets
            with open(self.tickets_file, 'r') as f:
                tickets = json.load(f)
            
            # Add new ticket
            tickets.append(ticket)
            
            # Save back to file
            with open(self.tickets_file, 'w') as f:
                json.dump(tickets, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving ticket: {str(e)}")
            return False
    
    def handle(self, subject: str, description: str, customer_name: str = "Ayush Dhoundiyal", 
               customer_email: str = "ayush@techshop.com") -> Response:
        """
        Handle support ticket creation.
        
        Args:
            subject (str): Ticket subject/title
            description (str): Ticket description/issue details
            customer_name (str): Customer name (default: Ayush Dhoundiyal)
            customer_email (str): Customer email
            
        Returns:
            Response: Response object confirming ticket creation
        """
        try:
            # Generate ticket ID
            ticket_id = self._generate_ticket_id()
            
            # Create ticket data
            ticket = {
                "ticket_id": ticket_id,
                "customer_name": customer_name,
                "customer_email": customer_email,
                "subject": subject,
                "description": description,
                "status": "Open",
                "priority": "Medium",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Save ticket
            if self._save_ticket(ticket):
                success_message = f"""Thank you, {customer_name}! Your support ticket has been created successfully.

📋 Ticket Details:
   • Ticket ID: {ticket_id}
   • Subject: {subject}
   • Status: Open
   • Created: {ticket['created_at']}

Our support team will review your ticket and get back to you within 24 hours at {customer_email}.

You can reference ticket ID {ticket_id} in any future communication regarding this issue."""
                
                return Response(
                    text=success_message,
                    links=["https://techshop.com/support", "https://techshop.com/contact"],
                    suggestions=[
                        "Check ticket status",
                        "Create another ticket",
                        "Contact support directly"
                    ]
                )
            else:
                raise Exception("Failed to save ticket")
        
        except Exception as e:
            error_message = f"I apologize, but there was an error creating your support ticket: {str(e)}\n\nPlease try again or contact our support team directly."
            return Response(
                text=error_message,
                links=["https://techshop.com/contact"],
                suggestions=["Try again", "Contact support by phone"]
            )
