"""
Main entry point for the chatbot service - Multi-Use Case Menu
"""
from src.handlers.faq_handler import FAQHandler
from src.handlers.order_status_handler import OrderStatusHandler
from src.handlers.password_reset_handler import PasswordResetHandler
from src.handlers.ticket_handler import TicketHandler
from src.handlers.escalation_handler import EscalationHandler
from src.handlers.feedback_handler import FeedbackHandler


def display_main_menu():
    """Display the main menu."""
    print("\n" + "=" * 70)
    print("🤖  TECHSHOP INC. CHATBOT SERVICE  🤖".center(70))
    print("=" * 70)
    print("\nPlease select a service:")
    print("\n1. 💬 FAQ - Frequently Asked Questions")
    print("2. 📦 Order Status - Check Your Order")
    print("3. 🔐 Password Reset - Reset Your Password")
    print("4. 🎫 Support Ticket - Create a Support Ticket")
    print("5. 👤 Escalate to Human - Speak with an Agent")
    print("6. ⭐ Feedback - Share Your Experience")
    print("7. � Exit")
    print("\n" + "-" * 70)


def run_faq_chatbot():
    """Run the FAQ chatbot."""
    print("\n" + "=" * 70)
    print("FAQ CHATBOT".center(70))
    print("=" * 70)
    print("\nI can help you with questions about:")
    print("- Operating hours")
    print("- Shipping information")
    print("- Return policy")
    print("- Payment methods")
    print("- Contact information")
    print("- Warranty information")
    print("- Account management")
    print("\nType 'back' to return to main menu or 'quit' to exit.")
    print("=" * 70)
    
    try:
        faq_handler = FAQHandler()
        
        while True:
            print("\n" + "-" * 70)
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                return 'quit'
            
            if user_input.lower() == 'back':
                return 'back'
            
            if not user_input:
                print("Please ask a question.")
                continue
            
            print("\n🤖 Assistant: ", end="")
            response = faq_handler.handle(user_input)
            
            print(response.text)
            
            if response.links:
                print("\n📎 Helpful Links:")
                for link in response.links:
                    print(f"   - {link}")
            
            if response.suggestions:
                print("\n💡 You might also want to ask:")
                for suggestion in response.suggestions[:3]:
                    print(f"   - {suggestion}")
    
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        return 'back'


def run_order_status_chatbot():
    """Run the order status chatbot."""
    print("\n" + "=" * 70)
    print("ORDER STATUS CHECKER".center(70))
    print("=" * 70)
    print("\nI can help you check the status of your orders!")
    print("\nAvailable test orders:")
    print("  • ORD-12345 - Shipped order")
    print("  • ORD-67890 - Processing order")
    print("  • ORD-11111 - Delivered order")
    print("  • ORD-22222 - Cancelled order")
    print("  • ORD-33333 - Out for delivery")
    print("\nType 'back' to return to main menu or 'quit' to exit.")
    print("=" * 70)
    
    try:
        order_handler = OrderStatusHandler()
        
        while True:
            print("\n" + "-" * 70)
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                return 'quit'
            
            if user_input.lower() == 'back':
                return 'back'
            
            if not user_input:
                print("Please enter your order ID or question.")
                continue
            
            print("\n🤖 Assistant: ", end="")
            response = order_handler.handle(user_input)
            
            print(response.text)
            
            if response.links:
                print("\n📎 Helpful Links:")
                for link in response.links:
                    print(f"   - {link}")
            
            if response.suggestions:
                print("\n💡 You might also want to:")
                for suggestion in response.suggestions[:3]:
                    print(f"   - {suggestion}")
    
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        return 'back'


def run_password_reset():
    """Run the password reset flow."""
    print("\n" + "=" * 70)
    print("PASSWORD RESET".center(70))
    print("=" * 70)
    
    try:
        reset_handler = PasswordResetHandler()
        
        # Display user information
        response = reset_handler.handle()
        print(f"\n{response.text}")
        
        print("\n" + "=" * 70)
        
        while True:
            # Prompt for new password
            print("\n" + "-" * 70)
            new_password = input("\nEnter new password (or 'back' to return to menu): ").strip()
            
            if new_password.lower() == 'back':
                return 'back'
            
            if new_password.lower() in ['quit', 'exit']:
                return 'quit'
            
            if not new_password:
                print("❌ Password cannot be empty. Please try again.")
                continue
            
            # Confirm password
            confirm_password = input("Confirm new password: ").strip()
            
            if new_password != confirm_password:
                print("\n❌ Passwords do not match. Please try again.")
                continue
            
            # Reset password
            print("\n🔄 Updating password...")
            reset_response = reset_handler.reset_password(new_password)
            
            print(f"\n{reset_response.text}")
            
            if reset_response.suggestions:
                print("\n💡 Next steps:")
                for suggestion in reset_response.suggestions[:3]:
                    print(f"   - {suggestion}")
            
            # If successful, return to menu
            if "successfully" in reset_response.text.lower():
                input("\nPress Enter to return to main menu...")
                return 'back'
    
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        return 'back'


def run_support_ticket():
    """Run the support ticket creation."""
    print("\n" + "=" * 70)
    print("SUPPORT TICKET CREATION".center(70))
    print("=" * 70)
    print("\nCreate a support ticket for technical issues or questions.")
    print("\nCustomer: Ayush Dhoundiyal")
    print("Email: ayush@techshop.com")
    print("\nType 'back' to return to main menu or 'quit' to exit.")
    print("=" * 70)
    
    try:
        ticket_handler = TicketHandler()
        
        while True:
            print("\n" + "-" * 70)
            
            # Get ticket subject
            print("\n📝 Enter ticket subject (or 'back'/'quit'):")
            subject = input("Subject: ").strip()
            
            if subject.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                return 'quit'
            
            if subject.lower() == 'back':
                return 'back'
            
            if not subject:
                print("❌ Subject cannot be empty. Please try again.")
                continue
            
            # Get ticket description
            print("\n📋 Enter detailed description of your issue:")
            description = input("Description: ").strip()
            
            if description.lower() in ['quit', 'exit', 'back']:
                return 'back'
            
            if not description:
                print("❌ Description cannot be empty. Please try again.")
                continue
            
            # Create the ticket
            print("\n⏳ Creating your support ticket...")
            response = ticket_handler.handle(subject, description)
            
            print(f"\n{response.text}")
            
            if response.links:
                print("\n📎 Helpful Links:")
                for link in response.links:
                    print(f"   - {link}")
            
            if response.suggestions:
                print("\n💡 What would you like to do next?")
                for suggestion in response.suggestions[:3]:
                    print(f"   - {suggestion}")
            
            # Ask if user wants to create another ticket
            print("\n" + "-" * 70)
            another = input("\nCreate another ticket? (yes/no): ").strip().lower()
            if another not in ['yes', 'y']:
                return 'back'
    
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        return 'back'


def run_escalation():
    """Run the escalation to human agent."""
    print("\n" + "=" * 70)
    print("ESCALATE TO HUMAN AGENT".center(70))
    print("=" * 70)
    print("\nConnect with a human agent for personalized assistance.")
    print("\nType 'back' to return to main menu or 'quit' to exit.")
    print("=" * 70)
    
    try:
        escalation_handler = EscalationHandler()
        
        while True:
            print("\n" + "-" * 70)
            print("\n👤 Please provide your contact information:\n")
            
            # Get customer name
            name = input("Your Name: ").strip()
            
            if name.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                return 'quit'
            
            if name.lower() == 'back':
                return 'back'
            
            if not name:
                print("❌ Name cannot be empty. Please try again.")
                continue
            
            # Get phone number
            phone = input("Your Phone Number: ").strip()
            
            if phone.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                return 'quit'
            
            if phone.lower() == 'back':
                return 'back'
            
            if not phone:
                print("❌ Phone number cannot be empty. Please try again.")
                continue
            
            # Get reason (optional)
            print("\nBriefly describe your issue (or press Enter to skip):")
            reason = input("Reason: ").strip()
            
            if reason.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                return 'quit'
            
            if reason.lower() == 'back':
                return 'back'
            
            # Handle escalation
            response = escalation_handler.handle(name, phone, reason if reason else None)
            
            print("\n" + response.text)
            
            # Check if successful by looking for success indicator in text
            if "✅" in response.text:
                # Ask if they want to create another escalation
                print("\n" + "-" * 70)
                another = input("\nWould you like to submit another escalation request? (yes/no): ").strip().lower()
                if another not in ['yes', 'y']:
                    return 'back'
            else:
                # If failed, ask to retry
                retry = input("\nWould you like to try again? (yes/no): ").strip().lower()
                if retry not in ['yes', 'y']:
                    return 'back'
    
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        return 'back'


def run_feedback():
    """Run the feedback collection."""
    print("\n" + "=" * 70)
    print("SHARE YOUR FEEDBACK".center(70))
    print("=" * 70)
    print("\nWe'd love to hear about your experience!")
    print("\nType 'back' to return to main menu or 'quit' to exit.")
    print("=" * 70)
    
    try:
        feedback_handler = FeedbackHandler()
        
        while True:
            print("\n" + "-" * 70)
            print("\n⭐ Please share your feedback:\n")
            
            # Get customer name
            name = input("Your Name: ").strip()
            
            if name.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                return 'quit'
            
            if name.lower() == 'back':
                return 'back'
            
            if not name:
                print("❌ Name cannot be empty. Please try again.")
                continue
            
            # Get rating
            print("\nHow would you rate your experience? (1-5 stars)")
            rating_input = input("Rating (1-5): ").strip()
            
            if rating_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                return 'quit'
            
            if rating_input.lower() == 'back':
                return 'back'
            
            # Validate rating
            try:
                rating = int(rating_input) if rating_input else 3
            except ValueError:
                print("❌ Invalid rating. Please enter a number between 1 and 5.")
                continue
            
            # Get comments
            print("\nPlease share your comments (or press Enter to skip):")
            comments = input("Comments: ").strip()
            
            if comments.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                return 'quit'
            
            if comments.lower() == 'back':
                return 'back'
            
            # Handle feedback
            response = feedback_handler.handle(name, rating, comments if comments else None)
            
            print("\n" + response.text)
            
            # Check if successful
            if "✅" in response.text:
                # Ask if they want to submit another feedback
                print("\n" + "-" * 70)
                another = input("\nWould you like to submit another feedback? (yes/no): ").strip().lower()
                if another not in ['yes', 'y']:
                    return 'back'
            else:
                # If failed, ask to retry
                retry = input("\nWould you like to try again? (yes/no): ").strip().lower()
                if retry not in ['yes', 'y']:
                    return 'back'
    
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        return 'back'


def main():
    """
    Main function to run the chatbot service with menu.
    """
    print("\n" + "🌟" * 35)
    print("Welcome to TechShop Inc. Customer Service Chatbot!".center(70))
    print("🌟" * 35)
    
    try:
        while True:
            display_main_menu()
            
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == '1':
                result = run_faq_chatbot()
                if result == 'quit':
                    break
            
            elif choice == '2':
                result = run_order_status_chatbot()
                if result == 'quit':
                    break
            
            elif choice == '3':
                result = run_password_reset()
                if result == 'quit':
                    break
            
            elif choice == '4':
                result = run_support_ticket()
                if result == 'quit':
                    break
            
            elif choice == '5':
                result = run_escalation()
                if result == 'quit':
                    break
            
            elif choice == '6':
                result = run_feedback()
                if result == 'quit':
                    break
            
            elif choice == '7':
                print("\n" + "=" * 70)
                print("Thank you for using TechShop Chatbot! Goodbye! 👋")
                print("=" * 70 + "\n")
                break
            
            else:
                print("\n❌ Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")
    
    except KeyboardInterrupt:
        print("\n\n" + "=" * 70)
        print("Chatbot interrupted. Goodbye! 👋")
        print("=" * 70 + "\n")
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        print("Please make sure your .env file contains a valid OZWELL_API_KEY")


if __name__ == "__main__":
    main()
