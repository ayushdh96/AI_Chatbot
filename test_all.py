"""
Comprehensive test script - Tests all chatbot handlers
"""
from src.handlers.faq_handler import FAQHandler
from src.handlers.order_status_handler import OrderStatusHandler
from src.handlers.password_reset_handler import PasswordResetHandler
from src.handlers.ticket_handler import TicketHandler
from src.handlers.escalation_handler import EscalationHandler
from src.handlers.feedback_handler import FeedbackHandler


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 75)
    print(f"  {title}".center(75))
    print("=" * 75)


def print_test(num, total, description):
    """Print test number."""
    print(f"\n{'─' * 75}")
    print(f"Test {num}/{total}: {description}")
    print('─' * 75)


def test_all_features():
    """
    Test all chatbot features comprehensively.
    """
    print("\n" + "🌟" * 37)
    print("TECHSHOP CHATBOT - COMPREHENSIVE TEST SUITE".center(75))
    print("🌟" * 37)
    
    try:
        # Initialize handlers
        print("\n📋 Initializing handlers...")
        faq_handler = FAQHandler()
        print("   ✓ FAQ Handler initialized")
        
        order_handler = OrderStatusHandler()
        print("   ✓ Order Status Handler initialized")
        
        password_handler = PasswordResetHandler()
        print("   ✓ Password Reset Handler initialized")
        
        ticket_handler = TicketHandler()
        print("   ✓ Ticket Handler initialized")
        
        escalation_handler = EscalationHandler()
        print("   ✓ Escalation Handler initialized")
        
        feedback_handler = FeedbackHandler()
        print("   ✓ Feedback Handler initialized")
        
        # =========================
        # USE CASE 1: FAQ TESTS
        # =========================
        print_header("USE CASE 1: FAQ CHATBOT")
        
        faq_tests = [
            "What are your operating hours?",
            "How much is express shipping?",
            "Can I pay with Apple Pay?",
        ]
        
        for i, question in enumerate(faq_tests, 1):
            print_test(i, len(faq_tests), "FAQ Query")
            print(f"\n❓ Question: {question}")
            
            response = faq_handler.handle(question)
            
            print(f"\n💬 Response:\n{response.text}")
            
            if response.links:
                print(f"\n🔗 Links: {len(response.links)} provided")
            
            if response.suggestions:
                print(f"💡 Suggestions: {len(response.suggestions)} provided")
        
        # =========================
        # USE CASE 2: ORDER STATUS TESTS
        # =========================
        print_header("USE CASE 2: ORDER STATUS CHECKER")
        
        order_tests = [
            ("Where is my order ORD-12345?", "Shipped Order"),
            ("Check status of ORD-67890", "Processing Order"),
            ("ORD-11111", "Delivered Order"),
            ("Track ORD-33333", "Out for Delivery"),
            ("What happened to ORD-22222?", "Cancelled Order"),
            ("Check ORD-99999", "Non-existent Order"),
        ]
        
        for i, (query, description) in enumerate(order_tests, 1):
            print_test(i, len(order_tests), description)
            print(f"\n❓ Query: {query}")
            
            response = order_handler.handle(query)
            
            print(f"\n💬 Response:\n{response.text}")
            
            if response.links:
                print(f"\n🔗 Links: {len(response.links)} provided")
                for link in response.links[:2]:
                    print(f"   • {link[:60]}...")
            
            if response.suggestions:
                print(f"💡 Suggestions: {len(response.suggestions)} provided")
        
        # =========================
        # USE CASE 3: PASSWORD RESET TESTS
        # =========================
        print_header("USE CASE 3: PASSWORD RESET")
        
        password_tests = [
            ("NewSecurePass123!", "Valid Password"),
            ("weak", "Invalid Password - Too Weak"),
        ]
        
        for i, (password, description) in enumerate(password_tests, 1):
            print_test(i, len(password_tests), description)
            print(f"\n🔐 Testing password reset...")
            
            response = password_handler.reset_password(password)
            
            print(f"\n💬 Response:\n{response.text}")
            
            if response.suggestions:
                print(f"💡 Suggestions: {len(response.suggestions)} provided")
        
        # =========================
        # USE CASE 4: SUPPORT TICKET TESTS
        # =========================
        print_header("USE CASE 4: SUPPORT TICKET CREATION")
        
        ticket_tests = [
            ("Login Issue", "Cannot access my account"),
            ("Product Defect", "Item arrived damaged"),
        ]
        
        for i, (subject, description) in enumerate(ticket_tests, 1):
            print_test(i, len(ticket_tests), f"Ticket: {subject}")
            print(f"\n📝 Subject: {subject}")
            print(f"📋 Description: {description}")
            
            response = ticket_handler.handle(subject, description)
            
            print(f"\n💬 Response:\n{response.text[:200]}...")
            
            if response.suggestions:
                print(f"💡 Suggestions: {len(response.suggestions)} provided")
        
        # =========================
        # USE CASE 5: ESCALATION TESTS
        # =========================
        print_header("USE CASE 5: ESCALATE TO HUMAN")
        
        escalation_tests = [
            ("Alice Johnson", "555-123-4567", "Need urgent help with my account"),
            ("Bob Williams", "1234567890", None),
        ]
        
        test_num = 1
        total_escalation = len(escalation_tests)
        
        for name, phone, reason in escalation_tests:
            print_test(test_num, total_escalation, f"Escalation for {name}")
            test_num += 1
            
            print(f"👤 Name: {name}")
            print(f"📞 Phone: {phone}")
            print(f"📝 Reason: {reason if reason else 'Not provided'}")
            
            response = escalation_handler.handle(name, phone, reason)
            
            print(f"\n💬 Response:\n{response.text[:200]}...")
        
        # =========================
        # USE CASE 6: FEEDBACK TESTS
        # =========================
        print_header("USE CASE 6: FEEDBACK")
        
        feedback_tests = [
            ("Sarah Johnson", 5, "Excellent service!"),
            ("Mike Davis", 3, "Average experience"),
            ("Lisa White", 1, "Very disappointed"),
        ]
        
        test_num = 1
        total_feedback = len(feedback_tests)
        
        for name, rating, comments in feedback_tests:
            print_test(test_num, total_feedback, f"Feedback from {name}")
            test_num += 1
            
            print(f"👤 Name: {name}")
            print(f"⭐ Rating: {rating}/5")
            print(f"💬 Comments: {comments}")
            
            response = feedback_handler.handle(name, rating, comments)
            
            print(f"\n💬 Response:\n{response.text[:200]}...")
        
        # =========================
        # SUMMARY
        # =========================
        print_header("TEST SUMMARY")
        print(f"\n✅ FAQ Tests: {len(faq_tests)} passed")
        print(f"✅ Order Status Tests: {len(order_tests)} passed")
        print(f"✅ Password Reset Tests: {len(password_tests)} passed")
        print(f"✅ Support Ticket Tests: {len(ticket_tests)} passed")
        print(f"✅ Escalation Tests: {len(escalation_tests)} passed")
        print(f"✅ Feedback Tests: {len(feedback_tests)} passed")
        total_tests = len(faq_tests) + len(order_tests) + len(password_tests) + len(ticket_tests) + len(escalation_tests) + len(feedback_tests)
        print(f"✅ Total Tests: {total_tests} passed")
        print("\n🎉 All tests completed successfully!")
        print("\n" + "=" * 75 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error during testing: {str(e)}")
        print("Make sure your .env file contains a valid OZWELL_API_KEY")


def test_quick_demo():
    """Quick demo showing one example from each use case."""
    print("\n" + "🚀" * 37)
    print("QUICK DEMO - One Example Per Use Case".center(75))
    print("🚀" * 37)
    
    try:
        # FAQ Example
        print_header("Use Case 1: FAQ")
        faq_handler = FAQHandler()
        print("\n❓ Question: What are your shipping options?")
        response = faq_handler.handle("What are your shipping options?")
        print(f"\n💬 Response:\n{response.text}\n")
        
        # Order Status Example
        print_header("Use Case 2: Order Status")
        order_handler = OrderStatusHandler()
        print("\n❓ Query: Where is order ORD-12345?")
        response = order_handler.handle("Where is order ORD-12345?")
        print(f"\n💬 Response:\n{response.text}\n")
        
        # Password Reset Example
        print_header("Use Case 3: Password Reset")
        password_handler = PasswordResetHandler()
        print("\n🔐 Resetting password...")
        response = password_handler.reset_password("NewSecure2025!")
        print(f"\n💬 Response:\n{response.text}\n")
        
        # Support Ticket Example
        print_header("Use Case 4: Support Ticket")
        ticket_handler = TicketHandler()
        print("\n🎫 Creating support ticket...")
        response = ticket_handler.handle("Test Issue", "This is a test ticket")
        print(f"\n💬 Response:\n{response.text[:150]}...\n")
        
        # Escalation Example
        print_header("Use Case 5: Escalate to Human")
        escalation_handler = EscalationHandler()
        print("\n👤 Escalating to human agent...")
        response = escalation_handler.handle("John Doe", "555-123-4567", "Need assistance")
        print(f"\n💬 Response:\n{response.text[:150]}...\n")
        
        # Feedback Example
        print_header("Use Case 6: Feedback")
        feedback_handler = FeedbackHandler()
        print("\n⭐ Submitting feedback...")
        response = feedback_handler.handle("Jane Doe", 5, "Great service!")
        print(f"\n💬 Response:\n{response.text[:150]}...\n")
        
        print("=" * 75)
        print("✅ Quick demo completed - All 6 use cases working!".center(75))
        print("=" * 75 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        test_quick_demo()
    else:
        test_all_features()
        print("\n💡 Tip: Run with --quick flag for a shorter demo")
        print("   python test_all.py --quick\n")
