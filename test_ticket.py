"""
Test script for Support Ticket handler - demonstrates automated testing
"""
from src.handlers.ticket_handler import TicketHandler


def test_ticket_handler():
    """
    Test the Support Ticket handler with sample tickets.
    """
    print("=" * 70)
    print("Support Ticket Handler - Automated Test")
    print("=" * 70)
    
    # Sample test tickets
    test_tickets = [
        {
            "subject": "Cannot login to my account",
            "description": "I'm trying to log in to my account but keep getting an 'Invalid credentials' error even though I'm sure my password is correct."
        },
        {
            "subject": "Product not working as expected",
            "description": "The wireless mouse I ordered (ORD-12345) is not connecting to my computer. I've tried replacing batteries and restarting, but it still doesn't work."
        },
        {
            "subject": "Refund not received",
            "description": "I returned an item 2 weeks ago (ORD-22222) and was told the refund would be processed in 5-7 business days, but I still haven't received it."
        }
    ]
    
    try:
        # Initialize Ticket handler
        print("\n✓ Initializing Support Ticket Handler...")
        ticket_handler = TicketHandler()
        print("✓ Support Ticket Handler initialized successfully!\n")
        
        # Test each ticket
        for i, ticket_data in enumerate(test_tickets, 1):
            print("\n" + "=" * 70)
            print(f"Test {i}/{len(test_tickets)}")
            print("=" * 70)
            print(f"\n📝 Subject: {ticket_data['subject']}")
            print(f"📋 Description: {ticket_data['description']}")
            print("\n🎫 Creating ticket...")
            
            # Create ticket
            response = ticket_handler.handle(
                subject=ticket_data['subject'],
                description=ticket_data['description']
            )
            
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
        print("\n📁 Check 'data/tickets.json' to see all created tickets.")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    test_ticket_handler()
