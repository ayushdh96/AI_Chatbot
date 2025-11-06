"""
Message - Message model for conversations
"""
from datetime import datetime
from typing import Optional


class Message:
    """
    Message model representing a single message in a conversation.
    
    Attributes:
        sender_type (str): Type of sender ('user' or 'bot')
        text (str): Message text content
        timestamp (datetime): When the message was sent
    """
    
    def __init__(self, sender_type: str, text: str, 
                 timestamp: Optional[datetime] = None):
        """
        Initialize Message.
        
        Args:
            sender_type (str): Type of sender ('user' or 'bot')
            text (str): Message text content
            timestamp (datetime): When the message was sent (defaults to now)
        """
        self.sender_type: str = sender_type
        self.text: str = text
        self.timestamp: datetime = timestamp if timestamp is not None else datetime.now()
