# Chatbot Service - Basic Structure

This project implements a chatbot service based on the UML class diagram specification.

## Project Structure

```
SE Project/
├── src/
│   ├── __init__.py
│   ├── core/                    # Core orchestration components
│   │   ├── __init__.py
│   │   ├── chat_service.py      # Main ChatService orchestrator
│   │   ├── nlp.py               # NLP analysis component
│   │   └── intent_router.py     # Intent routing component
│   │
│   ├── handlers/                # Intent handlers
│   │   ├── __init__.py
│   │   ├── faq_handler.py       # FAQ handler
│   │   ├── order_status_handler.py
│   │   ├── password_reset_handler.py
│   │   ├── ticket_handler.py
│   │   ├── escalation_handler.py
│   │   └── feedback_handler.py
│   │
│   ├── models/                  # Domain models
│   │   ├── __init__.py
│   │   ├── analysis_result.py   # NLP analysis result
│   │   ├── context.py           # Request context
│   │   ├── response.py          # Response object
│   │   ├── conversation.py      # Conversation model
│   │   ├── message.py           # Message model
│   │   └── user.py              # User model
│   │
│   └── services/                # Service layer
│       ├── __init__.py
│       └── service_layer.py     # Business logic services
│
└── main.py                      # Entry point

```

## Programming Standards Applied

### 1. **Naming Conventions**
- **Classes**: PascalCase (e.g., `ChatService`, `IntentRouter`, `FAQHandler`)
- **Methods**: snake_case (e.g., `handle_message`, `add_message`, `kb_search`)
- **Variables**: snake_case (e.g., `user_id`, `conversation_id`, `sender_type`)
- **Private attributes**: Prefixed with underscore (e.g., `_registry`)

### 2. **Type Annotations**
- All method parameters include type hints
- All return types are explicitly declared
- Attributes are type-annotated for clarity

### 3. **Documentation**
- Every class has a docstring explaining its purpose
- All methods include docstrings with:
  - Brief description
  - Args section documenting parameters
  - Returns section documenting return values

### 4. **Code Organization**
- Separation of concerns with dedicated packages:
  - `core/`: Main orchestration logic
  - `handlers/`: Intent-specific handling logic
  - `models/`: Data models and domain objects
  - `services/`: Business logic and external service access
- Clear module structure with `__init__.py` files

### 5. **Design Principles**
- **Single Responsibility**: Each class has one clear purpose
- **Dependency Injection**: Components receive dependencies via constructors
- **Type Safety**: Using Python type hints throughout
- **Modularity**: Loose coupling between components

## Class Overview

### Core Components
- **ChatService**: Main orchestrator handling incoming messages
- **NLP**: Analyzes text to extract intent and entities
- **IntentRouter**: Routes intents to appropriate handlers
- **AnalysisResult**: Stores NLP analysis results

### Handlers
- **FAQHandler**: Handles FAQ queries
- **OrderStatusHandler**: Handles order status inquiries
- **PasswordResetHandler**: Handles password reset requests
- **TicketHandler**: Creates support tickets
- **EscalationHandler**: Escalates to human agents
- **FeedbackHandler**: Records user feedback

### Models
- **Context**: Contains conversation, user, and analysis data
- **Response**: Chatbot response with text, links, and suggestions
- **Conversation**: Manages conversation state and messages
- **Message**: Individual message in a conversation
- **User**: User information

### Services
- **ServiceLayer**: Provides access to:
  - Knowledge base search
  - Order status retrieval
  - Ticket creation
  - Feedback recording

## Next Steps

The structure is now ready for implementation. Each class contains:
- ✅ Proper class definition with attributes
- ✅ Constructor with type-annotated parameters
- ✅ Method signatures with documentation
- ✅ TODO comments marking implementation points

All skeleton code follows Python best practices and is ready for logic implementation.
