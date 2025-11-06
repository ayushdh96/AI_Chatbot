"""
Response - Response object for chatbot replies
"""
from typing import List, Optional


class Response:
    """
    Response object containing the chatbot's reply.
    
    Attributes:
        text (str): Response text message
        links (List[str]): Related links to include in response
        suggestions (List[str]): Suggested follow-up actions or questions
    """
    
    def __init__(self, text: str = "", links: Optional[List[str]] = None, 
                 suggestions: Optional[List[str]] = None):
        """
        Initialize Response.
        
        Args:
            text (str): Response text message
            links (List[str]): Related links
            suggestions (List[str]): Suggested actions
        """
        self.text: str = text
        self.links: List[str] = links if links is not None else []
        self.suggestions: List[str] = suggestions if suggestions is not None else []
