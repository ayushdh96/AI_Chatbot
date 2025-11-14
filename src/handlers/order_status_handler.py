"""
OrderStatusHandler - Handles order status inquiries using Ozwell AI
"""
import os
import requests
from typing import Any, Dict, Optional
from dotenv import load_dotenv
from src.models.context import Context
from src.models.response import Response

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


class OrderStatusHandler:
    """
    Handler for order status inquiry intent.
    Uses Ozwell AI to provide natural language responses about order status.
    """
    
    # Dummy order database
    ORDERS_DB = {
        "ORD-12345": {
            "order_id": "ORD-12345",
            "customer_name": "John Doe",
            "status": "Shipped",
            "items": ["Wireless Mouse", "USB-C Cable"],
            "total": "$45.99",
            "order_date": "November 8, 2025",
            "estimated_delivery": "November 15, 2025",
            "tracking_number": "1Z999AA10123456784",
            "carrier": "UPS"
        },
        "ORD-67890": {
            "order_id": "ORD-67890",
            "customer_name": "Jane Smith",
            "status": "Processing",
            "items": ["Laptop Stand", "Keyboard", "Monitor"],
            "total": "$329.99",
            "order_date": "November 12, 2025",
            "estimated_delivery": "November 18, 2025",
            "tracking_number": None,
            "carrier": None
        },
        "ORD-11111": {
            "order_id": "ORD-11111",
            "customer_name": "Bob Johnson",
            "status": "Delivered",
            "items": ["Phone Case", "Screen Protector"],
            "total": "$24.99",
            "order_date": "November 1, 2025",
            "estimated_delivery": "November 5, 2025",
            "delivery_date": "November 4, 2025",
            "tracking_number": "1Z999AA10987654321",
            "carrier": "UPS"
        },
        "ORD-22222": {
            "order_id": "ORD-22222",
            "customer_name": "Alice Williams",
            "status": "Cancelled",
            "items": ["Headphones"],
            "total": "$89.99",
            "order_date": "November 10, 2025",
            "cancellation_date": "November 11, 2025",
            "cancellation_reason": "Customer request",
            "refund_status": "Processed"
        },
        "ORD-33333": {
            "order_id": "ORD-33333",
            "customer_name": "Mike Davis",
            "status": "Out for Delivery",
            "items": ["Gaming Mouse", "Mouse Pad"],
            "total": "$79.99",
            "order_date": "November 9, 2025",
            "estimated_delivery": "November 13, 2025 (Today!)",
            "tracking_number": "1Z999AA10555555555",
            "carrier": "UPS"
        }
    }
    
    def __init__(self):
        """Initialize order status handler with Ozwell AI."""
        self.api_key = os.getenv('OZWELL_API_KEY')
        if not self.api_key:
            raise ValueError("OZWELL_API_KEY not found in environment variables")
        self.ozwell_url = "https://ai.bluehive.com/api/v1/completion"
    
    def _extract_order_id(self, query: str) -> Optional[str]:
        """
        Extract order ID from user query.
        
        Args:
            query (str): User's query text
            
        Returns:
            Optional[str]: Order ID if found, None otherwise
        """
        # Simple extraction - look for pattern ORD-XXXXX
        query_upper = query.upper()
        for order_id in self.ORDERS_DB.keys():
            if order_id in query_upper:
                return order_id
        return None
    
    def _get_order_info(self, order_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve order information from database.
        
        Args:
            order_id (str): Order ID to look up
            
        Returns:
            Optional[Dict]: Order information if found, None otherwise
        """
        return self.ORDERS_DB.get(order_id)
    
    def handle(self, query: str) -> Response:
        """
        Handle order status request.
        
        Args:
            query (str): User's query about order status
            
        Returns:
            Response: Response object with order status information
        """
        try:
            # Extract order ID from query
            order_id = self._extract_order_id(query)
            
            if not order_id:
                # No order ID found in query
                return Response(
                    text="I couldn't find an order number in your request. Please provide your order ID (format: ORD-XXXXX) to check the status.",
                    suggestions=[
                        "Check order ORD-12345",
                        "What's the status of ORD-67890?",
                        "Track my order ORD-11111"
                    ]
                )
            
            # Get order information
            order_info = self._get_order_info(order_id)
            
            if not order_info:
                # Order not found
                return Response(
                    text=f"I couldn't find order {order_id} in our system. Please double-check your order number and try again. If you continue to have issues, please contact our support team.",
                    links=["https://techshop.com/contact"],
                    suggestions=[
                        "Try another order number",
                        "Contact customer support"
                    ]
                )
            
            # Create context for AI with order information
            system_message = """You are a helpful customer service assistant for TechShop Inc.
Provide a clear, friendly response about the order status based on the order information provided.
Be conversational and helpful. Include relevant details but keep it concise.
If the order is shipped, mention tracking information. If delivered, congratulate them.
If processing, give them an estimated timeline. If cancelled, be empathetic."""
            
            # Format order info for the AI
            order_context = f"""
Order Information:
- Order ID: {order_info['order_id']}
- Status: {order_info['status']}
- Items: {', '.join(order_info['items'])}
- Total: {order_info['total']}
- Order Date: {order_info['order_date']}
"""
            
            if order_info.get('estimated_delivery'):
                order_context += f"- Estimated Delivery: {order_info['estimated_delivery']}\n"
            
            if order_info.get('delivery_date'):
                order_context += f"- Delivered On: {order_info['delivery_date']}\n"
            
            if order_info.get('tracking_number'):
                order_context += f"- Tracking Number: {order_info['tracking_number']}\n"
                order_context += f"- Carrier: {order_info['carrier']}\n"
            
            if order_info.get('cancellation_reason'):
                order_context += f"- Cancellation Reason: {order_info['cancellation_reason']}\n"
                order_context += f"- Refund Status: {order_info['refund_status']}\n"
            
            # Prepare Ozwell AI request
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "prompt": f"User asked: {query}\n\n{order_context}\n\nProvide a friendly response about this order.",
                "systemMessage": system_message,
                "temperature": 0.7,
                "maxTokens": 250
            }
            
            # Call Ozwell AI API
            ozwell_response = requests.post(self.ozwell_url, headers=headers, json=payload)
            
            if ozwell_response.ok:
                try:
                    answer = ozwell_response.json()["choices"][0]["message"]["content"]
                except Exception as parse_error:
                    # Fallback response if AI fails
                    answer = f"Order {order_id} is currently {order_info['status']}."
                    if order_info.get('tracking_number'):
                        answer += f" Tracking number: {order_info['tracking_number']}"
            else:
                # Fallback response
                answer = f"Order {order_id} is currently {order_info['status']}."
                if order_info.get('tracking_number'):
                    answer += f" Tracking number: {order_info['tracking_number']}"
            
            # Create suggestions based on order status
            suggestions = []
            if order_info.get('tracking_number'):
                suggestions.append(f"Track package {order_info['tracking_number']}")
            suggestions.extend([
                "Check another order",
                "Contact customer support"
            ])
            
            # Add tracking link if available
            links = []
            if order_info.get('tracking_number'):
                links.append(f"https://www.ups.com/track?tracknum={order_info['tracking_number']}")
            links.append("https://techshop.com/orders")
            
            return Response(
                text=answer,
                links=links,
                suggestions=suggestions[:3]
            )
            
        except Exception as e:
            # Handle errors gracefully
            error_message = f"I apologize, but I encountered an error while checking your order: {str(e)}"
            return Response(
                text=error_message,
                suggestions=["Try again", "Contact support"]
            )
