"""
FAQHandler - Handles frequently asked questions using Ozwell AI
"""
import os
import requests
from typing import Any
from dotenv import load_dotenv
from src.models.context import Context
from src.models.response import Response

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


class FAQHandler:
    """
    Handler for FAQ (Frequently Asked Questions) intent.
    Uses Ozwell AI to answer questions based on a knowledge base.
    """
    
    # Sample FAQ knowledge base
    FAQ_KNOWLEDGE_BASE = """
    Company Name: TechShop Inc.
    
    Operating Hours:
    - Monday to Friday: 9:00 AM to 6:00 PM EST
    - Saturday: 10:00 AM to 4:00 PM EST
    - Sunday: Closed
    
    Shipping Information:
    - Standard Shipping: 5-7 business days (Free on orders over $50)
    - Express Shipping: 2-3 business days ($15)
    - Overnight Shipping: 1 business day ($30)
    
    Return Policy:
    - Returns accepted within 30 days of purchase
    - Items must be unused and in original packaging
    - Refund processed within 5-7 business days after receiving the return
    
    Payment Methods:
    - Credit Cards (Visa, MasterCard, American Express)
    - PayPal
    - Apple Pay
    - Google Pay
    
    Contact Information:
    - Email: support@techshop.com
    - Phone: 1-800-TECH-SHOP
    - Live Chat: Available on our website during business hours
    
    Warranty Information:
    - All products come with a 1-year manufacturer warranty
    - Extended warranty available for purchase
    - Warranty covers manufacturing defects only
    
    Account Management:
    - Create account on our website
    - Track orders through your account dashboard
    - Save multiple shipping addresses
    - View order history
    """
    
    def __init__(self):
        """Initialize FAQ handler with Ozwell AI."""
        self.api_key = os.getenv('OZWELL_API_KEY')
        if not self.api_key:
            raise ValueError("OZWELL_API_KEY not found in environment variables")
        self.ozwell_url = "https://ai.bluehive.com/api/v1/completion"
    
    def handle(self, question: str) -> Response:
        """
        Handle FAQ request using Ozwell AI.
        
        Args:
            question (str): User's question
            
        Returns:
            Response: Response object with answer to FAQ
        """
        try:
            # Create the system message with knowledge base context
            system_message = f"""You are a helpful customer service assistant for TechShop Inc. 
Answer customer questions based on the following knowledge base. 
Be concise, friendly, and helpful. If the information is not in the knowledge base, 
politely say you don't have that specific information and suggest contacting support.

Knowledge Base:
{self.FAQ_KNOWLEDGE_BASE}
"""
            
            # Prepare Ozwell AI request
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "prompt": question,
                "systemMessage": system_message,
                "temperature": 0.7,
                "maxTokens": 300
            }
            
            # Call Ozwell AI API
            ozwell_response = requests.post(self.ozwell_url, headers=headers, json=payload)
            
            if ozwell_response.ok:
                try:
                    answer = ozwell_response.json()["choices"][0]["message"]["content"]
                except Exception as parse_error:
                    answer = f"I received a response but couldn't parse it properly. Error: {str(parse_error)}"
            else:
                answer = f"I apologize, but I couldn't get a response from the AI service. Status code: {ozwell_response.status_code}"
            
            # Create suggestions based on common follow-up questions
            suggestions = [
                "What are your operating hours?",
                "What is your return policy?",
                "How can I contact support?"
            ]
            
            return Response(
                text=answer,
                links=["https://techshop.com/faq", "https://techshop.com/contact"],
                suggestions=suggestions
            )
            
        except Exception as e:
            # Handle errors gracefully
            error_message = f"I apologize, but I encountered an error while processing your question: {str(e)}"
            return Response(
                text=error_message,
                suggestions=["Try asking another question", "Contact support directly"]
            )
