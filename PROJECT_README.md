# 🤖 TechShop Customer Service Chatbot

A multi-functional customer service chatbot built with Python and Ozwell AI, featuring FAQ handling, order status checking, password reset, support ticket creation, human agent escalation, and feedback collection.

## 🌟 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the chatbot
python main.py
```

## 📚 Features

### ✅ Use Case 1: FAQ Chatbot
Answer frequently asked questions about:
- Operating hours
- Shipping information
- Return policy
- Payment methods
- Contact information
- Warranty details
- Account management

### ✅ Use Case 2: Order Status Checker
Check order status with:
- Natural language queries
- Real-time order information
- Tracking details
- 5 sample orders for testing
- Clear "not found" messaging

### ✅ Use Case 3: Password Reset
Reset password securely with:
- Single user management (Ayush Dhoundiyal)
- Password validation (length, case, numbers)
- Secure SHA-256 hashing
- JSON file storage
- Clear requirement feedback

### ✅ Use Case 4: Support Ticket Creation
Create support tickets with:
- Simple ticket submission
- Auto-generated ticket IDs
- JSON file storage
- Customer information (Ayush Dhoundiyal)
- Timestamp tracking
- Status and priority fields

### ✅ Use Case 5: Escalate to Human
Request human agent assistance with:
- Contact information collection
- Phone number validation (10-15 digits)
- International number support (+, -, (), spaces)
- Auto-generated escalation IDs
- JSON file storage
- Estimated wait time notification

### ✅ Use Case 6: Feedback Collection
Collect customer feedback with:
- Rating system (1-5 stars)
- Comments collection
- Auto-generated feedback IDs
- JSON file storage
- Visual star rating display
- Appreciation message

## 🎮 Interactive Menu

```
🤖  TECHSHOP INC. CHATBOT SERVICE  🤖

Please select a service:

1. 💬 FAQ - Frequently Asked Questions
2. 📦 Order Status - Check Your Order
3. 🔐 Password Reset - Reset Your Password
4. 🎫 Support Ticket - Create a Support Ticket
5. 👤 Escalate to Human - Speak with an Agent
6. ⭐ Feedback - Share Your Experience
7. 🚪 Exit
```

## 🚀 Usage Examples

### FAQ
```
You: What are your operating hours?
🤖: Our operating hours are Monday to Friday from 9:00 AM 
    to 6:00 PM EST, and Saturday from 10:00 AM to 4:00 PM EST.
```

### Order Status
```
You: Where is my order ORD-12345?
🤖: Your order ORD-12345 has been shipped! Expected delivery: 
    November 15, 2025. Tracking: 1Z999AA10123456784 (UPS)
```

### Password Reset
```
You: MyNewPassword123
🤖: ✅ Password successfully updated for Ayush Dhoundiyal!
    Your new password has been securely saved.
```

### Support Ticket
```
You: [Subject] Cannot login
     [Description] Getting invalid credentials error
🤖: Thank you, Ayush Dhoundiyal! Your support ticket has been 
    created successfully.
    📋 Ticket ID: TKT-00001
```

### Escalate to Human
```
You: [Name] John Doe
     [Phone] 555-123-4567
     [Reason] Need urgent help with my account
🤖: ✅ Escalation Request Submitted Successfully!
    📋 Escalation ID: ESC-00001
    A human agent will contact you shortly.
```

### Feedback
```
You: [Name] Jane Doe
     [Rating] 5
     [Comments] Excellent service!
🤖: ✅ Thank you for your feedback!
    📋 Feedback ID: FB-00001
    ⭐⭐⭐⭐⭐ Rating: 5/5
```

## 🧪 Testing

```bash
# Test FAQ only
python test_faq.py

# Test Order Status only
python test_order_status.py

# Test Password Reset only
python test_password_reset.py

# Test Support Ticket only
python test_ticket.py

# Test Escalation only
python test_escalation.py

# Test Feedback only
python test_feedback.py

# Test everything
python test_all.py

# Quick demo
python test_all.py --quick
```

## 📦 Sample Orders

Try these order IDs:
- `ORD-12345` - Shipped
- `ORD-67890` - Processing
- `ORD-11111` - Delivered
- `ORD-22222` - Cancelled
- `ORD-33333` - Out for Delivery

## 🔐 Password Reset

User: Ayush Dhoundiyal  
Default Password: TechShop2025!  
Storage: data/passwords.json (hashed)

## 🎫 Support Tickets

Customer: Ayush Dhoundiyal (ayush@techshop.com)  
Storage: data/tickets.json  
Ticket ID Format: TKT-00001, TKT-00002, etc.

## 👤 Escalations

Storage: data/escalations.json  
Escalation ID Format: ESC-00001, ESC-00002, etc.  
Phone Validation: 10-15 digits, supports international formats

## ⭐ Feedback

Storage: data/feedback.json  
Feedback ID Format: FB-00001, FB-00002, etc.  
Rating Range: 1-5 stars

## � Configuration

Create `src/.env`:
```properties
OZWELL_API_KEY=your-api-key-here
```

## 📖 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Get started quickly
- **[USE_CASE_1_FAQ.md](USE_CASE_1_FAQ.md)** - FAQ handler details
- **[USE_CASE_2_ORDER_STATUS.md](USE_CASE_2_ORDER_STATUS.md)** - Order status details
- **[USE_CASE_3_PASSWORD_RESET.md](USE_CASE_3_PASSWORD_RESET.md)** - Password reset details
- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - Complete summary

## 🏗️ Project Structure

```
AI_Chatbot/
├── main.py                     # Menu-based entry point
├── test_*.py                   # Test scripts
├── data/
│   ├── passwords.json         # Password storage
│   ├── tickets.json           # Support tickets storage
│   ├── escalations.json       # Escalation requests storage
│   └── feedback.json          # Customer feedback storage
├── src/
│   ├── .env                   # Configuration
│   ├── handlers/
│   │   ├── faq_handler.py    # FAQ implementation
    │   ├── order_status_handler.py  # Order status implementation
    │   ├── password_reset_handler.py  # Password reset implementation
    │   ├── ticket_handler.py  # Support ticket implementation
    │   └── escalation_handler.py  # Escalation implementation
    │   └── feedback_handler.py  # Feedback implementation
    └── models/
        └── response.py        # Response model
```

## 🛠️ Tech Stack

- **Python 3.11+**
- **Ozwell AI** - Natural language processing
- **requests** - HTTP client
- **python-dotenv** - Environment management

## ✨ Key Features

- 🎯 Menu-driven interface
- 🤖 AI-powered responses
- 📝 Clear error messages
- 🔗 Helpful links and suggestions
- 🧪 Comprehensive test coverage
- 📚 Complete documentation
- 🎨 User-friendly navigation

## 🎓 Design Principles

- **Single Responsibility**: Each handler has one clear purpose
- **Type Safety**: Full type annotations
- **Error Handling**: Graceful degradation
- **Documentation**: Comprehensive docstrings
- **Modularity**: Easy to extend

## 🔮 Future Enhancements

- Web interface (Flask/FastAPI)
- Real database integration
- User authentication
- Multi-language support
- Email notifications
- SMS notifications for escalations
- Feedback sentiment analysis
- Analytics dashboard
- Ticket assignment and tracking
- Multi-user password management
- Agent availability and queue management

## 📄 License

Educational project for SE coursework.

## 👨‍💻 Author

Ayush Dhoundiyal

---

**Status**: ✅ Fully Functional (6 Use Cases) | **Last Updated**: November 14, 2025

**Status**: ✅ Fully Functional | **Last Updated**: November 13, 2025
