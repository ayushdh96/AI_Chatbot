"""
Conversation - Conversation model
"""
from typing import List
from src.models.message import Message


class Conversation:
    """
    Conversation model representing a chat conversation.
    
    Attributes:
        conversation_id (str): Unique conversation identifier
        status (str): Current conversation status
        messages (List[Message]): List of messages in the conversation
    """
    
    def __init__(self, conversation_id: str, status: str = "active"):
        """
        Initialize Conversation.
        
        Args:
            conversation_id (str): Unique conversation identifier
            status (str): Conversation status (default: 'active')
        """
        self.conversation_id: str = conversation_id
        self.status: str = status
        self.messages: List[Message] = []
    
    def add_message(self, msg: Message) -> None:
        """
        Add a message to the conversation.
        
        Args:
            msg (Message): Message to add to the conversation
        """
        # TODO: Implement message addition logic
        pass
