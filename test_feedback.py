"""
Test script for Feedback Handler
Tests the feedback collection functionality
"""
from src.handlers.feedback_handler import FeedbackHandler


def test_feedback_handler():
    """Test the feedback handler with various scenarios."""
    print("\n" + "=" * 70)
    print("TESTING FEEDBACK HANDLER".center(70))
    print("=" * 70)
    
    handler = FeedbackHandler()
    
    # Test 1: Valid feedback with 5 stars
    print("\n" + "-" * 70)
    print("Test 1: Excellent experience (5 stars)")
    print("-" * 70)
    response = handler.handle(
        customer_name="John Doe",
        rating=5,
        comments="Excellent service! Very helpful and responsive."
    )
    print(response.text)
    
    # Test 2: Valid feedback with 3 stars
    print("\n" + "-" * 70)
    print("Test 2: Average experience (3 stars)")
    print("-" * 70)
    response = handler.handle(
        customer_name="Jane Smith",
        rating=3,
        comments="Service was okay, could be better."
    )
    print(response.text)
    
    # Test 3: Valid feedback with 1 star
    print("\n" + "-" * 70)
    print("Test 3: Poor experience (1 star)")
    print("-" * 70)
    response = handler.handle(
        customer_name="Bob Wilson",
        rating=1,
        comments="Very disappointed with the service."
    )
    print(response.text)
    
    # Test 4: Feedback without comments
    print("\n" + "-" * 70)
    print("Test 4: Feedback without comments")
    print("-" * 70)
    response = handler.handle(
        customer_name="Alice Brown",
        rating=4
    )
    print(response.text)
    
    # Test 5: Invalid rating (too high)
    print("\n" + "-" * 70)
    print("Test 5: Invalid rating (6 stars)")
    print("-" * 70)
    response = handler.handle(
        customer_name="David Lee",
        rating=6,
        comments="Great service!"
    )
    print(response.text)
    
    # Test 6: Invalid rating (too low)
    print("\n" + "-" * 70)
    print("Test 6: Invalid rating (0 stars)")
    print("-" * 70)
    response = handler.handle(
        customer_name="Emily Clark",
        rating=0,
        comments="Not satisfied"
    )
    print(response.text)
    
    # Test 7: Default rating (no rating provided)
    print("\n" + "-" * 70)
    print("Test 7: Default rating (no rating)")
    print("-" * 70)
    response = handler.handle(
        customer_name="Frank Miller",
        comments="Just wanted to leave some comments"
    )
    print(response.text)
    
    print("\n" + "=" * 70)
    print("TESTING COMPLETE".center(70))
    print("=" * 70)
    print("\nCheck data/feedback.json to see saved feedback.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    test_feedback_handler()
