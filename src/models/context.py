"""
Context - Context information for handling requests
"""
from typing import Any
from src.models.conversation import Conversation
from src.models.user import User
from src.models.analysis_result import AnalysisResult
from src.services.service_layer import ServiceLayer


class Context:
    """
    Context object containing all necessary information for handling a request.
    
    Attributes:
        conversation (Conversation): Current conversation
        user (User): User information
        analysis (AnalysisResult): NLP analysis result
        services (ServiceLayer): Access to service layer
    """
    
    def __init__(self, conversation: Conversation, user: User, 
                 analysis: AnalysisResult, services: ServiceLayer):
        """
        Initialize Context.
        
        Args:
            conversation (Conversation): Current conversation
            user (User): User information
            analysis (AnalysisResult): NLP analysis result
            services (ServiceLayer): Service layer instance
        """
        self.conversation: Conversation = conversation
        self.user: User = user
        self.analysis: AnalysisResult = analysis
        self.services: ServiceLayer = services
