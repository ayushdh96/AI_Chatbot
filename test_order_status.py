"""
Test script for Order Status chatbot - demonstrates automated testing
"""
from src.handlers.order_status_handler import OrderStatusHandler


def test_order_status_chatbot():
    """
    Test the Order Status chatbot with sample queries.
    """
    print("=" * 70)
    print("Order Status Chatbot - Automated Test")
    print("=" * 70)
    
    # Sample test queries
    test_queries = [
        "Where is my order ORD-12345?",
        "Check status of ORD-67890",
        "What's happening with order ORD-11111?",
        "Track ORD-33333",
        "Status of ORD-22222",
        "Where is order ORD-99999?"  # Non-existent order
    ]
    
    try:
        # Initialize Order Status handler
        print("\n✓ Initializing Order Status Handler...")
        order_handler = OrderStatusHandler()
        print("✓ Order Status Handler initialized successfully!\n")
        
        # Test each query
        for i, query in enumerate(test_queries, 1):
            print("\n" + "=" * 70)
            print(f"Test {i}/{len(test_queries)}")
            print("=" * 70)
            print(f"\n📝 Query: {query}")
            print("\n🤖 Response:")
            
            # Get response
            response = order_handler.handle(query)
            
            # Display response
            print(f"\n{response.text}")
            
            if response.links:
                print("\n📎 Links provided:")
                for link in response.links:
                    print(f"   - {link}")
            
            if response.suggestions:
                print("\n💡 Suggestions provided:")
                for suggestion in response.suggestions[:2]:
                    print(f"   - {suggestion}")
        
        print("\n" + "=" * 70)
        print("✓ All tests completed successfully!")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Make sure your .env file contains a valid OZWELL_API_KEY")


if __name__ == "__main__":
    test_order_status_chatbot()
