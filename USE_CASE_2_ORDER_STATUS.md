# Use Case 2: Order Status Checker

## Overview
This use case implements an order status checker that uses Ozwell AI to provide natural language responses about customer orders. Users can check their order status by providing an order ID, and the chatbot will fetch the information from a dummy order database and provide a friendly, conversational response.

## Features
- Command-line interface integrated into the main menu
- Integration with Ozwell AI for natural language responses
- Dummy order database with 5 sample orders in various states
- Order ID extraction from natural language queries
- Comprehensive order information including:
  - Order status (Shipped, Processing, Delivered, Cancelled, Out for Delivery)
  - Items ordered
  - Total amount
  - Order date
  - Estimated/actual delivery date
  - Tracking information (when available)
  - Cancellation/refund details (when applicable)

## Sample Orders in Database

### ORD-12345 - Shipped Order
- **Items**: Wireless Mouse, USB-C Cable
- **Total**: $45.99
- **Status**: Shipped
- **Order Date**: November 8, 2025
- **Estimated Delivery**: November 15, 2025
- **Tracking**: 1Z999AA10123456784 (UPS)

### ORD-67890 - Processing Order
- **Items**: Laptop Stand, Keyboard, Monitor
- **Total**: $329.99
- **Status**: Processing
- **Order Date**: November 12, 2025
- **Estimated Delivery**: November 18, 2025

### ORD-11111 - Delivered Order
- **Items**: Phone Case, Screen Protector
- **Total**: $24.99
- **Status**: Delivered
- **Delivery Date**: November 4, 2025
- **Tracking**: 1Z999AA10987654321 (UPS)

### ORD-22222 - Cancelled Order
- **Items**: Headphones
- **Total**: $89.99
- **Status**: Cancelled
- **Cancellation Date**: November 11, 2025
- **Refund Status**: Processed

### ORD-33333 - Out for Delivery
- **Items**: Gaming Mouse, Mouse Pad
- **Total**: $79.99
- **Status**: Out for Delivery
- **Estimated Delivery**: November 13, 2025 (Today!)
- **Tracking**: 1Z999AA10555555555 (UPS)

## How to Use

### Access from Main Menu
```bash
python main.py
```

Then select option `2` for Order Status Checker.

### Example Queries

You can ask about orders in various natural ways:

**Direct order ID:**
- `ORD-12345`
- `Check ORD-67890`

**Natural language:**
- `Where is my order ORD-12345?`
- `What's the status of order ORD-33333?`
- `Check order ORD-11111`
- `Track my package ORD-12345`
- `When will ORD-67890 arrive?`

### Navigation
- Type `back` to return to the main menu
- Type `quit` or `exit` to close the chatbot

## Implementation Details

### Architecture

**OrderStatusHandler** (`src/handlers/order_status_handler.py`):
- Contains a dummy order database (`ORDERS_DB`) as a class variable
- Extracts order IDs from natural language queries
- Looks up order information in the database
- Uses Ozwell AI to generate natural, conversational responses
- Returns structured `Response` objects

### Key Methods

1. **`_extract_order_id(query)`**
   - Extracts order ID from user's natural language query
   - Looks for pattern `ORD-XXXXX` in the text
   - Returns the order ID or None if not found

2. **`_get_order_info(order_id)`**
   - Retrieves order information from the database
   - Returns order details dictionary or None if not found

3. **`handle(query)`**
   - Main handler method
   - Coordinates order lookup and AI response generation
   - Handles errors gracefully

### Order Not Found Handling

When a user provides an invalid order ID:
- The chatbot directly tells them the order wasn't found
- No ambiguous "please check your order number" messages
- Suggests contacting support if they continue having issues
- Provides alternative actions (try another order, contact support)

Example:
```
You: Check order ORD-99999

🤖 Assistant: I couldn't find order ORD-99999 in our system. 
Please double-check your order number and try again. If you 
continue to have issues, please contact our support team.
```

### AI Integration

The handler uses Ozwell AI to create natural, contextual responses:

```python
system_message = """You are a helpful customer service assistant for TechShop Inc.
Provide a clear, friendly response about the order status based on the order information provided.
Be conversational and helpful. Include relevant details but keep it concise.
If the order is shipped, mention tracking information. If delivered, congratulate them.
If processing, give them an estimated timeline. If cancelled, be empathetic."""
```

This ensures responses are:
- Friendly and conversational
- Appropriate to the order status
- Concise but informative
- Empathetic when needed (cancellations, delays)

## Example Interactions

### Shipped Order
```
You: Where is my order ORD-12345?

🤖 Assistant: Hi there! Your order with ID ORD-12345 has been shipped 
and is on its way to you. It includes a Wireless Mouse and a USB-C Cable, 
totaling $45.99. You can expect it to arrive by November 15, 2025. 
Your tracking number is 1Z999AA10123456784 with UPS. Safe travels to 
your package!

📎 Helpful Links:
   - https://www.ups.com/track?tracknum=1Z999AA10123456784
   - https://techshop.com/orders

💡 You might also want to:
   - Track package 1Z999AA10123456784
   - Check another order
```

### Processing Order
```
You: Status of ORD-67890

🤖 Assistant: Your order ORD-67890 is currently being processed. You 
ordered a Laptop Stand, Keyboard, and Monitor for a total of $329.99 
on November 12, 2025. The estimated delivery date is November 18, 2025. 
We'll send you tracking information once your order ships!

📎 Helpful Links:
   - https://techshop.com/orders

💡 You might also want to:
   - Check another order
   - Contact customer support
```

### Delivered Order
```
You: Track ORD-11111

🤖 Assistant: Great news! Your order ORD-11111 has been successfully 
delivered on November 4, 2025! This order included a Phone Case and 
Screen Protector totaling $24.99. We hope you enjoy your purchase!

📎 Helpful Links:
   - https://www.ups.com/track?tracknum=1Z999AA10987654321
   - https://techshop.com/orders

💡 You might also want to:
   - Track package 1Z999AA10987654321
   - Check another order
```

### Cancelled Order
```
You: What happened to ORD-22222?

🤖 Assistant: I'm sorry to inform you that order ORD-22222 for Headphones 
was cancelled on November 11, 2025 due to a customer request. The refund 
of $89.99 has been processed and should appear in your account within 
5-7 business days. If you have any questions, feel free to reach out!

📎 Helpful Links:
   - https://techshop.com/orders

💡 You might also want to:
   - Check another order
   - Contact customer support
```

## Error Handling

### No Order ID Provided
```
You: Where is my package?

🤖 Assistant: I couldn't find an order number in your request. 
Please provide your order ID (format: ORD-XXXXX) to check the status.

💡 You might also want to ask:
   - Check order ORD-12345
   - What's the status of ORD-67890?
   - Track my order ORD-11111
```

### Order Not Found
```
You: Check ORD-99999

🤖 Assistant: I couldn't find order ORD-99999 in our system. 
Please double-check your order number and try again. If you continue 
to have issues, please contact our support team.

📎 Helpful Links:
   - https://techshop.com/contact

💡 You might also want to:
   - Try another order number
   - Contact customer support
```

## Customization

### Adding More Orders

Edit the `ORDERS_DB` dictionary in `src/handlers/order_status_handler.py`:

```python
ORDERS_DB = {
    "ORD-XXXXX": {
        "order_id": "ORD-XXXXX",
        "customer_name": "Customer Name",
        "status": "Shipped",  # or Processing, Delivered, Cancelled, Out for Delivery
        "items": ["Item1", "Item2"],
        "total": "$XX.XX",
        "order_date": "Date",
        "estimated_delivery": "Date",
        "tracking_number": "TRACKING123",  # Optional
        "carrier": "UPS"  # Optional
    }
}
```

### Modifying AI Response Style

Adjust the `system_message` in the `handle()` method to change the tone and style of responses.

### Changing Temperature

Modify the temperature for more/less creative responses:
```python
payload = {
    "temperature": 0.5,  # Lower = more deterministic, Higher = more creative
    ...
}
```

## Future Enhancements

- Integration with real order management system
- Customer authentication before showing order details
- Email notifications for order updates
- Real-time tracking updates
- Order modification capabilities
- Return/refund request handling
- Multiple orders per customer lookup
