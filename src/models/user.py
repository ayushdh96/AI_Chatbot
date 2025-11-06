"""
User - User model
"""
from typing import Optional


class User:
    """
    User model representing a chatbot user.
    
    Attributes:
        user_id (str): Unique user identifier
        name (str): User's name
        email (str): User's email address
    """
    
    def __init__(self, user_id: str, name: str = "", email: str = ""):
        """
        Initialize User.
        
        Args:
            user_id (str): Unique user identifier
            name (str): User's name
            email (str): User's email address
        """
        self.user_id: str = user_id
        self.name: str = name
        self.email: str = email
