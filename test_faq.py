"""
Test script for FAQ chatbot - demonstrates automated testing
"""
from src.handlers.faq_handler import FAQHandler


def test_faq_chatbot():
    """
    Test the FAQ chatbot with sample questions.
    """
    print("=" * 70)
    print("FAQ Chatbot - Automated Test")
    print("=" * 70)
    
    # Sample test questions
    test_questions = [
        "What are your operating hours?",
        "How long does shipping take?",
        "What is your return policy?",
        "What payment methods do you accept?",
        "How can I contact support?",
    ]
    
    try:
        # Initialize FAQ handler
        print("\n✓ Initializing FAQ Handler...")
        faq_handler = FAQHandler()
        print("✓ FAQ Handler initialized successfully!\n")
        
        # Test each question
        for i, question in enumerate(test_questions, 1):
            print("\n" + "=" * 70)
            print(f"Test {i}/{len(test_questions)}")
            print("=" * 70)
            print(f"\n📝 Question: {question}")
            print("\n🤖 Answer:")
            
            # Get response
            response = faq_handler.handle(question)
            
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
        print("Make sure your .env file contains a valid OPENAI_API_KEY")


if __name__ == "__main__":
    test_faq_chatbot()
