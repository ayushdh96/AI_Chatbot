"""
AnalysisResult - Result from NLP analysis
"""
from typing import Dict, Any, Optional


class AnalysisResult:
    """
    Result of NLP analysis containing intent, entities, and confidence.
    
    Attributes:
        intent (str): Identified intent from the text
        entities (Dict[str, Any]): Extracted entities from the text
        confidence (float): Confidence score of the analysis
    """
    
    def __init__(self, intent: str = "", entities: Optional[Dict[str, Any]] = None, 
                 confidence: float = 0.0):
        """
        Initialize AnalysisResult.
        
        Args:
            intent (str): Identified intent
            entities (Dict[str, Any]): Extracted entities
            confidence (float): Confidence score (0.0 to 1.0)
        """
        self.intent: str = intent
        self.entities: Dict[str, Any] = entities if entities is not None else {}
        self.confidence: float = confidence
