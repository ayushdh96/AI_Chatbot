# Use Case 1: Simple FAQ Chatbot

## Overview
This use case implements a simple FAQ chatbot that uses Ozwell AI to answer customer questions based on a predefined knowledge base.

## Features
- Command-line interface for easy interaction
- Integration with Ozwell AI (Bluehive AI platform)
- Predefined knowledge base about TechShop Inc. including:
  - Operating hours
  - Shipping information
  - Return policy
  - Payment methods
  - Contact information
  - Warranty information
  - Account management

## Setup

### 1. Install Dependencies
```bash
pip install requests python-dotenv
```

### 2. Configure Ozwell AI API Key
Make sure your `.env` file in the `src/` directory contains your Ozwell AI API key:
```
OZWELL_API_KEY=
```

### 3. Run the Chatbot
```bash
python main.py
```

## Usage

Once you run the chatbot, you can ask questions like:

**Example Questions:**
- "What are your operating hours?"
- "How long does shipping take?"
- "What is your return policy?"
- "What payment methods do you accept?"
- "How can I contact customer support?"
- "Do you offer warranties on products?"

**To Exit:**
Type `quit`, `exit`, `bye`, or `goodbye` to end the conversation.

## Implementation Details

### Architecture
- **FAQHandler** (`src/handlers/faq_handler.py`): Main handler class that:
  - Loads the Ozwell AI API key from environment variables
  - Contains a knowledge base as a class variable
  - Uses Ozwell AI to answer questions based on the knowledge base
  - Returns structured `Response` objects with text, links, and suggestions

### Ozwell AI Integration
The FAQ handler uses Ozwell AI's completion API at `https://ai.bluehive.com/api/v1/completion`
- **Model**: Ozwell AI's default model
- **Temperature**: 0.7 (balanced responses)
- **Max Tokens**: 300 (concise answers)
- **System Message**: Contains the knowledge base context

### Knowledge Base
The FAQ knowledge base is stored as a string constant in the `FAQHandler` class. For this small project, this approach is sufficient. In a production environment, you might want to:
- Store it in a database
- Use a vector database for semantic search
- Implement RAG (Retrieval Augmented Generation)

### Response Structure
Each response includes:
- **Text**: The main answer from ChatGPT
- **Links**: Helpful related links
- **Suggestions**: Follow-up questions the user might ask

## Example Interaction

```
============================================================
Welcome to TechShop Inc. FAQ Chatbot!
============================================================

I can help you with questions about:
- Operating hours
- Shipping information
- Return policy
- Payment methods
- Contact information
- Warranty information
- Account management

Type 'quit' or 'exit' to end the conversation.
============================================================

------------------------------------------------------------

You: What are your operating hours?

🤖 Assistant: Our operating hours are as follows:
- Monday to Friday: 9:00 AM to 6:00 PM EST
- Saturday: 10:00 AM to 4:00 PM EST
- Sunday: Closed

Feel free to reach out during these times for assistance!

📎 Helpful Links:
   - https://techshop.com/faq
   - https://techshop.com/contact

💡 You might also want to ask:
   - What are your operating hours?
   - What is your return policy?
   - How can I contact support?

------------------------------------------------------------

You: How much is express shipping?

🤖 Assistant: Express shipping costs $15 and typically takes 2-3 business days 
for delivery.

📎 Helpful Links:
   - https://techshop.com/faq
   - https://techshop.com/contact

💡 You might also want to ask:
   - What are your operating hours?
   - What is your return policy?
   - How can I contact support?

------------------------------------------------------------

You: quit

Thank you for using TechShop FAQ Chatbot! Goodbye! 👋
```

## Error Handling
- If the Ozwell AI API key is missing, the chatbot will display an error message
- If there's an error during API calls, a friendly error message is shown
- The chatbot gracefully handles keyboard interrupts (Ctrl+C)

## Customization

### Adding More FAQ Topics
To add more topics to the knowledge base, edit the `FAQ_KNOWLEDGE_BASE` constant in `src/handlers/faq_handler.py`:

```python
FAQ_KNOWLEDGE_BASE = """
    # Your existing content
    
    New Topic:
    - Information about the topic
    - More details
"""
```

### Changing the AI Model
Ozwell AI uses its default model. The temperature and maxTokens can be adjusted in the `handle()` method:

```python
payload = {
    "prompt": question,
    "systemMessage": system_message,
    "temperature": 0.7,  # Adjust between 0.0 (deterministic) and 1.0 (creative)
    "maxTokens": 300     # Adjust for longer/shorter responses
}
```

## Future Enhancements
- Add conversation history tracking
- Implement user authentication
- Add analytics for popular questions
- Create a web interface
- Integrate with actual business systems (order tracking, etc.)
