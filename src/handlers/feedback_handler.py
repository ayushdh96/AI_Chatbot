"""
FeedbackHandler - Handles user feedback
"""
import json
import os
from datetime import datetime
from typing import Optional
from src.models.response import Response


class FeedbackHandler:
    """
    Handler for user feedback intent.
    Collects and stores customer feedback.
    """
    
    def __init__(self):
        """Initialize feedback handler."""
        self.feedback_file = "data/feedback.json"
        self._ensure_data_file()
    
    def _ensure_data_file(self) -> None:
        """Ensure the feedback data file exists."""
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.feedback_file):
            with open(self.feedback_file, 'w') as f:
                json.dump([], f)
    
    def _generate_feedback_id(self) -> str:
        """
        Generate unique feedback ID.
        
        Returns:
            str: Feedback ID in format FB-XXXXX
        """
        try:
            with open(self.feedback_file, 'r') as f:
                feedbacks = json.load(f)
                next_id = len(feedbacks) + 1
                return f"FB-{next_id:05d}"
        except Exception:
            return "FB-00001"
    
    def _save_feedback(self, customer_name: str, rating: int, comments: str) -> str:
        """
        Save feedback to file.
        
        Args:
            customer_name (str): Customer name
            rating (int): Rating (1-5)
            comments (str): Feedback comments
            
        Returns:
            str: Generated feedback ID
        """
        feedback_id = self._generate_feedback_id()
        
        feedback = {
            "feedback_id": feedback_id,
            "customer_name": customer_name,
            "rating": rating,
            "comments": comments,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            with open(self.feedback_file, 'r') as f:
                feedbacks = json.load(f)
            
            feedbacks.append(feedback)
            
            with open(self.feedback_file, 'w') as f:
                json.dump(feedbacks, f, indent=2)
            
            return feedback_id
        except Exception as e:
            raise Exception(f"Failed to save feedback: {str(e)}")
    
    def handle(self, customer_name: str, rating: Optional[int] = None, comments: Optional[str] = None) -> Response:
        """
        Handle feedback submission.
        
        Args:
            customer_name (str): Customer name
            rating (Optional[int]): Rating from 1-5
            comments (Optional[str]): Feedback comments
            
        Returns:
            Response: Response object confirming feedback receipt
        """
        # Validate rating if provided
        if rating is not None and (rating < 1 or rating > 5):
            return Response(
                text="❌ Invalid rating. Please provide a rating between 1 and 5."
            )
        
        # Use default values if not provided
        if rating is None:
            rating = 3  # Default neutral rating
        
        if not comments:
            comments = "No comments provided"
        
        try:
            # Save feedback
            feedback_id = self._save_feedback(customer_name, rating, comments)
            
            # Create response based on rating
            rating_emoji = "⭐" * rating
            
            message = f"""✅ Thank you for your feedback!

📋 Feedback ID: {feedback_id}
👤 Name: {customer_name}
{rating_emoji} Rating: {rating}/5
💬 Comments: {comments}

We appreciate you taking the time to share your experience with us!"""
            
            return Response(text=message)
        
        except Exception as e:
            return Response(
                text=f"❌ Failed to submit feedback: {str(e)}"
            )
