# Quick Start Guide - TechShop Chatbot

## What Was Implemented

✅ **Menu System** with multiple use cases  
✅ **Use Case 1: FAQ Handler** with Ozwell AI integration  
✅ **Use Case 2: Order Status Checker** with dummy order database  
✅ **Use Case 3: Password Reset** with secure password management  
✅ **Use Case 4: Support Ticket Creation** with JSON storage  
✅ **Use Case 5: Escalate to Human** with agent contact request  
✅ **Use Case 6: Feedback Collection** with rating and comments  
✅ **Command-line interface** for interactive conversations  
✅ **Sample knowledge base and order data**  
✅ **Automated test scripts** for demonstration

## Files Modified/Created

### Modified Files:
1. **`requirements.txt`** - Added requests and python-dotenv dependencies
2. **`main.py`** - Created menu-based interface with multiple use cases
3. **`src/handlers/faq_handler.py`** - Implemented FAQ handler with Ozwell AI
4. **`src/handlers/order_status_handler.py`** - Implemented order status checker
5. **`src/handlers/password_reset_handler.py`** - Implemented password reset
6. **`src/handlers/ticket_handler.py`** - Implemented support ticket creation
7. **`src/handlers/escalation_handler.py`** - Implemented escalation to human agent
8. **`src/handlers/feedback_handler.py`** - Implemented feedback collection

### New Files:
1. **`USE_CASE_1_FAQ.md`** - Detailed FAQ documentation
2. **`USE_CASE_2_ORDER_STATUS.md`** - Detailed Order Status documentation
3. **`USE_CASE_3_PASSWORD_RESET.md`** - Detailed Password Reset documentation
4. **`test_faq.py`** - Automated FAQ test script
5. **`test_order_status.py`** - Automated order status test script
6. **`test_password_reset.py`** - Automated password reset test script
7. **`test_ticket.py`** - Automated support ticket test script
8. **`test_escalation.py`** - Automated escalation test script
9. **`test_feedback.py`** - Automated feedback test script
10. **`test_all.py`** - Comprehensive test for all use cases
11. **`data/passwords.json`** - Password storage file
12. **`data/tickets.json`** - Support tickets storage file
13. **`data/escalations.json`** - Escalation requests storage file
14. **`data/feedback.json`** - Customer feedback storage file
15. **`QUICK_START.md`** - This file

## How to Use

### Main Menu (Recommended)
```bash
python main.py
```

This will display a menu:
```
1. 💬 FAQ - Frequently Asked Questions
2. 📦 Order Status - Check Your Order
3. 🔐 Password Reset - Reset Your Password
4. 🎫 Support Ticket - Create a Support Ticket
5. 👤 Escalate to Human - Speak with an Agent
6. ⭐ Feedback - Share Your Experience
7. 🚪 Exit
```

Select the service you want to use by entering 1, 2, 3, 4, 5, 6, or 7.

### Navigation Commands
- Type `back` to return to the main menu from any service
- Type `quit` or `exit` to close the chatbot entirely
- Use Ctrl+C to force quit

### Individual Test Scripts

**Test FAQ only:**
```bash
python test_faq.py
```

**Test Order Status only:**
```bash
python test_order_status.py
```

**Test Password Reset only:**
```bash
python test_password_reset.py
```

**Test Support Ticket only:**
```bash
python test_ticket.py
```

**Test Escalation only:**
```bash
python test_escalation.py
```

**Test Feedback only:**
```bash
python test_feedback.py
```

**Test all use cases:**
```bash
python test_all.py
```

**Quick demo (one example per use case):**
```bash
python test_all.py --quick
```

## Use Case 1: FAQ Questions

Sample questions to try:
1. "What are your operating hours?"
2. "How long does standard shipping take?"
3. "Can I return a product after 30 days?"
4. "Do you accept PayPal?"
5. "What's covered under warranty?"
6. "How can I track my order?"

## Use Case 2: Order Status

Sample order IDs to try:
- `ORD-12345` - Shipped order
- `ORD-67890` - Processing order
- `ORD-11111` - Delivered order
- `ORD-22222` - Cancelled order
- `ORD-33333` - Out for delivery

You can ask in natural language:
- "Where is my order ORD-12345?"
- "Check status of ORD-67890"
- "Track ORD-33333"

## Use Case 3: Password Reset

**User:** Ayush Dhoundiyal  
**User ID:** ayush.dhoundiyal

Password requirements:
- At least 8 characters long
- At least one uppercase letter
- At least one lowercase letter
- At least one number

Example passwords to try:
- `NewSecure2025!` - Valid
- `MyPass123` - Valid
- `weak` - Invalid (too short, no uppercase)

## Use Case 4: Support Ticket

Create support tickets for issues or questions.

**Customer:** Ayush Dhoundiyal  
**Email:** ayush@techshop.com

Sample tickets you can create:
- **Subject:** "Cannot login to my account"  
  **Description:** "Getting invalid credentials error"
  
- **Subject:** "Product not working"  
  **Description:** "Wireless mouse won't connect"
  
- **Subject:** "Refund inquiry"  
  **Description:** "Haven't received my refund yet"

Tickets are saved to `data/tickets.json` with auto-generated IDs (TKT-00001, TKT-00002, etc.)

## Use Case 5: Escalate to Human

Request to speak with a human agent.

Provide your contact information:
- **Name:** Your full name
- **Phone Number:** 10-15 digits (supports +, -, (), spaces)
- **Reason:** Brief description of your issue (optional)

Sample valid phone numbers:
- `555-123-4567`
- `5551234567`
- `+1-555-987-6543`
- `(555) 123-4567`

Escalation requests are saved to `data/escalations.json` with auto-generated IDs (ESC-00001, ESC-00002, etc.)

## Use Case 6: Feedback

Share your experience with TechShop.

Provide your feedback:
- **Name:** Your full name
- **Rating:** 1-5 stars
- **Comments:** Your feedback comments (optional)

Sample feedback:
- **Rating 5:** "Excellent service! Very helpful and responsive."
- **Rating 3:** "Service was okay, could be better."
- **Rating 1:** "Very disappointed with the service."

Feedback is saved to `data/feedback.json` with auto-generated IDs (FB-00001, FB-00002, etc.)

## Technical Details

### Use Case 1: FAQ Handler
- **Purpose**: Answer frequently asked questions
- **Data Source**: Embedded knowledge base string
- **AI Integration**: Ozwell AI with system context
- **Knowledge Topics**: Hours, shipping, returns, payments, contact, warranty, accounts

### Use Case 2: Order Status Checker
- **Purpose**: Check order status and tracking
- **Data Source**: Dummy order database (5 sample orders)
- **AI Integration**: Ozwell AI for natural language responses
- **Order States**: Shipped, Processing, Delivered, Cancelled, Out for Delivery

### Use Case 3: Password Reset
- **Purpose**: Reset user password securely
- **User**: Single user (Ayush Dhoundiyal)
- **Storage**: JSON file with hashed passwords (SHA-256)
- **Validation**: Length, uppercase, lowercase, number requirements

### Use Case 4: Support Ticket
- **Purpose**: Create and save support tickets
- **Storage**: JSON file (data/tickets.json)
- **Auto-generated IDs**: TKT-XXXXX format
- **Fields**: Subject, description, customer info, timestamps, status

### Use Case 5: Escalate to Human
- **Purpose**: Request human agent assistance
- **Storage**: JSON file (data/escalations.json)
- **Auto-generated IDs**: ESC-XXXXX format
- **Validation**: Phone number format (10-15 digits, supports international)
- **Fields**: Name, phone, reason, status, timestamps

### Use Case 6: Feedback
- **Purpose**: Collect customer feedback
- **Storage**: JSON file (data/feedback.json)
- **Auto-generated IDs**: FB-XXXXX format
- **Validation**: Rating must be 1-5
- **Fields**: Name, rating, comments, timestamp

### API Configuration:
- Using **Ozwell AI** (Bluehive platform)
- Temperature: 0.7 (balanced creativity)
- Max tokens: 250-300 (concise answers)
- API key loaded from `src/.env` file

## Menu System

The chatbot now features a user-friendly menu system:
1. Select a service from the main menu
2. Use the selected service
3. Type `back` to return to menu or `quit` to exit
4. Choose another service or exit

This makes it easy to switch between different chatbot capabilities without restarting the application.

## Knowledge Base Content (FAQ)

The FAQ chatbot knows about:
- **Operating Hours**: Mon-Fri 9AM-6PM EST, Sat 10AM-4PM EST
- **Shipping**: Standard (5-7 days), Express (2-3 days), Overnight (1 day)
- **Returns**: 30-day return policy
- **Payment**: Credit cards, PayPal, Apple Pay, Google Pay
- **Contact**: Email, phone, live chat
- **Warranty**: 1-year manufacturer warranty
- **Account**: Order tracking, address management, order history

## Order Database (Order Status)

The order status checker has 5 dummy orders:
- **ORD-12345**: Shipped (Wireless Mouse, USB-C Cable) - $45.99
- **ORD-67890**: Processing (Laptop Stand, Keyboard, Monitor) - $329.99
- **ORD-11111**: Delivered (Phone Case, Screen Protector) - $24.99
- **ORD-22222**: Cancelled (Headphones) - $89.99
- **ORD-33333**: Out for Delivery (Gaming Mouse, Mouse Pad) - $79.99

## Password Storage (Password Reset)

User credentials stored in `data/passwords.json`:
- **User**: Ayush Dhoundiyal (ayush.dhoundiyal)
- **Default Password**: TechShop2025!
- **Storage**: SHA-256 hashed password
- **Format**: JSON file

## Support Tickets Storage

Tickets stored in `data/tickets.json`:
- **Format**: JSON array of ticket objects
- **Ticket ID**: Auto-generated (TKT-00001, TKT-00002, etc.)
- **Fields**: ticket_id, customer_name, customer_email, subject, description, status, priority, created_at, updated_at
- **Customer**: Ayush Dhoundiyal (ayush@techshop.com)

## Escalation Requests Storage

Escalations stored in `data/escalations.json`:
- **Format**: JSON array of escalation objects
- **Escalation ID**: Auto-generated (ESC-00001, ESC-00002, etc.)
- **Fields**: escalation_id, customer_name, phone_number, reason, status, created_at, updated_at
- **Status**: Pending (default)

## Feedback Storage

Feedback stored in `data/feedback.json`:
- **Format**: JSON array of feedback objects
- **Feedback ID**: Auto-generated (FB-00001, FB-00002, etc.)
- **Fields**: feedback_id, customer_name, rating, comments, created_at
- **Rating**: 1-5 stars

## Next Steps

### To expand the FAQ use case:
1. Add more topics to the knowledge base in `faq_handler.py`
2. Integrate with actual documentation/knowledge base
3. Add conversation history tracking
4. Implement caching for common questions

### To expand the Order Status use case:
1. Add more orders to `ORDERS_DB` in `order_status_handler.py`
2. Integrate with real order management system/API
3. Add customer authentication
4. Implement order modification features
5. Add email notifications

### To expand the Password Reset use case:
1. Add multi-user support in `password_reset_handler.py`
2. Use bcrypt instead of SHA-256 for better security
3. Add password confirmation (enter twice)
4. Implement email verification
5. Add password strength indicator
6. Add password history to prevent reuse

### To expand the Support Ticket use case:
1. Add ticket status updates (Open, In Progress, Resolved, Closed)
2. Implement ticket priority assignment logic
3. Add file attachment support
4. Create ticket search and filter functionality
5. Integrate with email notifications
6. Add support agent assignment

### To expand the Escalation use case:
1. Add agent assignment and availability tracking
2. Implement queue management system
3. Add SMS notifications to customers
4. Create escalation priority levels
5. Add estimated wait time calculator
6. Integrate with CRM system

### To expand the Feedback use case:
1. Add sentiment analysis on feedback comments
2. Implement feedback analytics dashboard
3. Add email notifications for low ratings
4. Create feedback categories/tags
5. Add follow-up system for negative feedback
6. Integrate with customer satisfaction metrics

### To add new use cases:
1. Create a new handler in `src/handlers/`
2. Add menu option in `main.py`
3. Create a corresponding test script
4. Document in a new USE_CASE_X.md file

## Troubleshooting

**If you get an API key error:**
- Check that `src/.env` file exists
- Verify the OZWELL_API_KEY is correct (no spaces)
- Make sure python-dotenv is installed

**If imports fail:**
- Run: `pip install requests python-dotenv`
- Make sure you're in the project directory

**If the chatbot doesn't respond:**
- Check your internet connection
- Verify your Ozwell AI API key is active
- Check the API endpoint is accessible
