"""
Test script for Escalation Handler
Tests the escalation to human agent functionality
"""
from src.handlers.escalation_handler import EscalationHandler


def test_escalation_handler():
    """Test the escalation handler with various scenarios."""
    print("\n" + "=" * 70)
    print("TESTING ESCALATION HANDLER".center(70))
    print("=" * 70)
    
    handler = EscalationHandler()
    
    # Test 1: Valid escalation with reason
    print("\n" + "-" * 70)
    print("Test 1: Valid escalation with reason")
    print("-" * 70)
    response = handler.handle(
        customer_name="John Doe",
        phone="555-123-4567",
        reason="Need help with billing issue"
    )
    print(response.text)
    
    # Test 2: Valid escalation without reason
    print("\n" + "-" * 70)
    print("Test 2: Valid escalation without reason")
    print("-" * 70)
    response = handler.handle(
        customer_name="Jane Smith",
        phone="5551234567"
    )
    print(response.text)
    
    # Test 3: Invalid phone number (too short)
    print("\n" + "-" * 70)
    print("Test 3: Invalid phone number (too short)")
    print("-" * 70)
    response = handler.handle(
        customer_name="Bob Wilson",
        phone="12345"
    )
    print(response.text)
    
    # Test 4: Invalid phone number (contains letters)
    print("\n" + "-" * 70)
    print("Test 4: Invalid phone number (contains letters)")
    print("-" * 70)
    response = handler.handle(
        customer_name="Alice Brown",
        phone="555-ABC-1234"
    )
    print(response.text)
    
    # Test 5: International format
    print("\n" + "-" * 70)
    print("Test 5: International phone number")
    print("-" * 70)
    response = handler.handle(
        customer_name="David Lee",
        phone="+1-555-987-6543",
        reason="Product inquiry"
    )
    print(response.text)
    
    print("\n" + "=" * 70)
    print("TESTING COMPLETE".center(70))
    print("=" * 70)
    print("\nCheck data/escalations.json to see saved escalation requests.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    test_escalation_handler()
