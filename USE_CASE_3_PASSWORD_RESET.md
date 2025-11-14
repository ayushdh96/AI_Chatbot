# Use Case 3: Password Reset

## Overview
This use case implements a password reset functionality for a single user (Ayush Dhoundiyal). The user can reset their password through an interactive flow with password validation and secure storage using SHA-256 hashing.

## Features
- Single user password management
- Interactive password reset flow
- Password validation with security requirements
- Secure password hashing (SHA-256)
- Password storage in JSON file
- Clear success/error messaging
- Integration with main menu

## User Information

**Name**: Ayush Dhoundiyal  
**User ID**: ayush.dhoundiyal  
**Default Password**: TechShop2025!  
**Storage**: `data/passwords.json`

## Password Requirements

✓ At least 8 characters long  
✓ At least one uppercase letter  
✓ At least one lowercase letter  
✓ At least one number

## How to Use

### Access from Main Menu
```bash
python main.py
```

Then select option `3` for Password Reset.

### Interactive Flow

```
======================================================================
                         PASSWORD RESET                         
======================================================================

🔐 Resetting password for: Ayush Dhoundiyal

Password Requirements:
• At least 8 characters long
• At least one uppercase letter
• At least one lowercase letter
• At least one number

Please enter your new password (or 'back' to return to menu):

----------------------------------------------------------------------

New Password: ********

🤖 Assistant: ✅ Password successfully updated for Ayush Dhoundiyal!

Your new password has been securely saved. Please use this password for 
your next login.

💡 You might also want to:
   - Test your new password
   - Update password manager
   - Return to main menu
```

### Navigation
- Enter a new password that meets the requirements
- Type `back` to return to the main menu
- Type `quit` to exit the application

## Implementation Details

### Architecture

**PasswordResetHandler** (`src/handlers/password_reset_handler.py`):
- Manages password for single user (Ayush Dhoundiyal)
- Stores password in `data/passwords.json`
- Validates password requirements
- Hashes passwords using SHA-256
- Returns structured `Response` objects

### Key Methods

1. **`_validate_password(password)`**
   - Validates password against security requirements
   - Returns tuple (is_valid, error_message)
   - Checks length, uppercase, lowercase, and numbers

2. **`_hash_password(password)`**
   - Hashes password using SHA-256
   - Returns hexadecimal hash string
   - Used for secure password storage

3. **`_save_password(password)`**
   - Saves hashed password to JSON file
   - Creates data directory if needed
   - Returns True on success

4. **`handle(new_password)`**
   - Main handler method
   - Validates and saves the new password
   - Returns appropriate success/error response

### Password Storage Format

File: `data/passwords.json`

```json
{
  "ayush.dhoundiyal": "hashed_password_here"
}
```

The password is stored as a SHA-256 hash for security.

### Validation Logic

```python
# Length check
if len(password) < 8:
    return False, "Password must be at least 8 characters long"

# Uppercase check
if not any(c.isupper() for c in password):
    return False, "Password must contain at least one uppercase letter"

# Lowercase check
if not any(c.islower() for c in password):
    return False, "Password must contain at least one lowercase letter"

# Number check
if not any(c.isdigit() for c in password):
    return False, "Password must contain at least one number"
```

## Example Interactions

### Successful Password Reset
```
You: MyNewPassword123

🤖 Assistant: ✅ Password successfully updated for Ayush Dhoundiyal!

Your new password has been securely saved. Please use this password for 
your next login.

💡 You might also want to:
   - Test your new password
   - Update password manager
   - Return to main menu
```

### Password Too Short
```
You: Short1

🤖 Assistant: ❌ Password reset failed!

Password must be at least 8 characters long

Please try again with a password that meets all requirements.

💡 Password Requirements:
   - At least 8 characters long
   - At least one uppercase letter
   - At least one lowercase letter
   - At least one number
```

### Missing Uppercase Letter
```
You: lowercase123

🤖 Assistant: ❌ Password reset failed!

Password must contain at least one uppercase letter

Please try again with a password that meets all requirements.

💡 Password Requirements:
   - At least 8 characters long
   - At least one uppercase letter
   - At least one lowercase letter
   - At least one number
```

### Missing Lowercase Letter
```
You: UPPERCASE123

🤖 Assistant: ❌ Password reset failed!

Password must contain at least one lowercase letter

Please try again with a password that meets all requirements.
```

### Missing Number
```
You: NoNumbers

🤖 Assistant: ❌ Password reset failed!

Password must contain at least one number

Please try again with a password that meets all requirements.
```

## Security Features

### 1. Password Hashing
- Uses SHA-256 cryptographic hash function
- Passwords never stored in plain text
- One-way hashing (cannot be reversed)

### 2. Password Requirements
- Enforces strong password policy
- Prevents weak passwords
- Clear error messages for each requirement

### 3. Secure File Storage
- Passwords stored in dedicated data directory
- JSON format for easy reading/writing
- File permissions respected by OS

### 4. No Password Display
- Password input can be hidden in production
- Hash values not displayed to user
- Secure transmission to handler

## Testing

### Automated Test Script

Run comprehensive tests:
```bash
python test_password_reset.py
```

This tests:
- ✓ User information display
- ✓ Password too short (< 8 characters)
- ✓ No uppercase letter
- ✓ No lowercase letter
- ✓ No numbers
- ✓ Valid password reset
- ✓ Multiple password changes

### Manual Testing

Test different scenarios:
```bash
python main.py
# Select option 3
# Try various passwords to test validation
```

## File Structure

```
AI_Chatbot/
├── data/
│   └── passwords.json          # Password storage (hashed)
├── src/
│   └── handlers/
│       └── password_reset_handler.py  # Password reset logic
└── test_password_reset.py      # Test script
```

## Default Credentials

**Initial Setup:**
- Username: ayush.dhoundiyal
- Password: TechShop2025!

After first reset, use your new password.

## Customization

### Change Password Requirements

Edit the `_validate_password` method in `password_reset_handler.py`:

```python
def _validate_password(self, password: str) -> tuple[bool, str]:
    """Validate password requirements."""
    
    # Change minimum length
    if len(password) < 12:  # Changed from 8
        return False, "Password must be at least 12 characters long"
    
    # Add special character requirement
    if not any(c in "!@#$%^&*" for c in password):
        return False, "Password must contain a special character"
    
    # ... rest of validation
```

### Add More Users

To support multiple users, modify the class:

```python
USERS = {
    "ayush.dhoundiyal": "Ayush Dhoundiyal",
    "john.doe": "John Doe"
}

def handle(self, user_id: str, new_password: str) -> Response:
    # Validate user_id exists
    # Reset password for that user
```

### Change Hashing Algorithm

To use a different hashing algorithm:

```python
import hashlib

def _hash_password(self, password: str) -> str:
    # Using bcrypt (more secure for passwords)
    import bcrypt
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
```

Note: bcrypt is recommended for password hashing in production.

## Error Handling

### File Not Found
If `passwords.json` doesn't exist:
- Automatically creates the file
- Initializes with default password
- Creates data directory if needed

### Invalid Password
If password doesn't meet requirements:
- Returns clear error message
- Suggests requirements
- Allows retry

### File Permission Issues
If can't write to file:
- Returns error message
- Suggests checking permissions
- Doesn't crash the application

## Production Considerations

### For Real-World Use:

1. **Use bcrypt or argon2** instead of SHA-256
   ```bash
   pip install bcrypt
   ```

2. **Add password confirmation**
   ```python
   # Ask user to enter password twice
   if password1 != password2:
       return error_response
   ```

3. **Add email verification**
   - Send verification code to email
   - Confirm identity before reset

4. **Add rate limiting**
   - Prevent brute force attacks
   - Limit reset attempts per hour

5. **Add password history**
   - Prevent reusing recent passwords
   - Store last N password hashes

6. **Add multi-factor authentication**
   - Require additional verification
   - SMS or authenticator app

7. **Use database instead of JSON**
   - More secure
   - Better concurrency
   - Transaction support

8. **Add audit logging**
   - Log all password changes
   - Track IP addresses
   - Alert on suspicious activity

## Future Enhancements

- [ ] Email verification before reset
- [ ] Password strength indicator
- [ ] Password history (prevent reuse)
- [ ] Multi-factor authentication
- [ ] Account lockout after failed attempts
- [ ] Password expiry (force periodic changes)
- [ ] Security questions
- [ ] SMS verification
- [ ] Biometric authentication option
- [ ] Password recovery via email
- [ ] Multi-user support
- [ ] Role-based access control

## Best Practices

✅ Never store passwords in plain text  
✅ Use strong hashing algorithms (bcrypt, argon2)  
✅ Enforce password complexity requirements  
✅ Provide clear feedback on requirements  
✅ Log security events  
✅ Use HTTPS in production  
✅ Implement rate limiting  
✅ Add multi-factor authentication  
✅ Regular security audits  
✅ Keep dependencies updated  

## Troubleshooting

**Problem**: Password file not found  
**Solution**: Handler automatically creates it with default password

**Problem**: Password validation failing  
**Solution**: Check that password meets all 4 requirements

**Problem**: Can't save password  
**Solution**: Check file permissions on `data/` directory

**Problem**: Password not updating  
**Solution**: Verify `passwords.json` is writable

## Conclusion

The password reset use case provides:
- ✅ Secure password storage
- ✅ Strong validation
- ✅ User-friendly interface
- ✅ Easy integration
- ✅ Production-ready foundation

Perfect for POC/demo purposes, with clear path for production enhancement.

---

*Last Updated: November 14, 2025*
