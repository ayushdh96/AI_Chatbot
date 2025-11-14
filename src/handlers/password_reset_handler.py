"""
PasswordResetHandler - Handles password reset requests
"""
import os
import json
import hashlib
from typing import Dict, Optional
from src.models.context import Context
from src.models.response import Response


class PasswordResetHandler:
    """
    Handler for password reset intent.
    Manages password updates for a single user (Ayush Dhoundiyal).
    """
    
    # Single user configuration
    USER_NAME = "Ayush Dhoundiyal"
    USER_ID = "ayush.dhoundiyal"
    
    def __init__(self):
        """Initialize password reset handler."""
        self.password_file = os.path.join(
            os.path.dirname(__file__), 
            '..', 
            '..', 
            'data', 
            'passwords.json'
        )
        # Ensure data directory exists
        os.makedirs(os.path.dirname(self.password_file), exist_ok=True)
        
        # Initialize password file if it doesn't exist
        if not os.path.exists(self.password_file):
            self._initialize_password_file()
    
    def _initialize_password_file(self):
        """Initialize the password file with default password."""
        initial_data = {
            self.USER_ID: self._hash_password("TechShop2025!")
        }
        with open(self.password_file, 'w') as f:
            json.dump(initial_data, f, indent=2)
    
    def _hash_password(self, password: str) -> str:
        """
        Hash password using SHA-256.
        
        Args:
            password (str): Plain text password
            
        Returns:
            str: Hashed password
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _load_passwords(self) -> Dict[str, str]:
        """
        Load passwords from file.
        
        Returns:
            Dict[str, str]: Dictionary of user_id to hashed password
        """
        try:
            with open(self.password_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self._initialize_password_file()
            return {self.USER_ID: self._hash_password("TechShop2025!")}
    
    def _save_passwords(self, passwords: Dict[str, str]) -> bool:
        """
        Save passwords to file.
        
        Args:
            passwords (Dict[str, str]): Dictionary of user_id to hashed password
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(self.password_file, 'w') as f:
                json.dump(passwords, f, indent=2)
            return True
        except Exception:
            return False
    
    def _validate_password(self, password: str) -> tuple[bool, Optional[str]]:
        """
        Validate password meets requirements.
        
        Args:
            password (str): Password to validate
            
        Returns:
            tuple[bool, Optional[str]]: (is_valid, error_message)
        """
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        
        if not any(c.isupper() for c in password):
            return False, "Password must contain at least one uppercase letter"
        
        if not any(c.islower() for c in password):
            return False, "Password must contain at least one lowercase letter"
        
        if not any(c.isdigit() for c in password):
            return False, "Password must contain at least one number"
        
        return True, None
    
    def reset_password(self, new_password: str) -> Response:
        """
        Reset password for the user.
        
        Args:
            new_password (str): New password to set
            
        Returns:
            Response: Response object with reset status
        """
        # Validate password
        is_valid, error_message = self._validate_password(new_password)
        
        if not is_valid:
            return Response(
                text=f"❌ Password reset failed: {error_message}",
                suggestions=[
                    "Try a stronger password",
                    "Password must be 8+ characters with uppercase, lowercase, and numbers"
                ]
            )
        
        # Load current passwords
        passwords = self._load_passwords()
        
        # Update password
        passwords[self.USER_ID] = self._hash_password(new_password)
        
        # Save updated passwords
        if self._save_passwords(passwords):
            return Response(
                text=f"✅ Password successfully updated for {self.USER_NAME}!\n\n"
                     f"Your new password has been securely saved. "
                     f"Please use this password for your next login.",
                links=["https://techshop.com/login"],
                suggestions=[
                    "Test your new password",
                    "Update password manager",
                    "Return to main menu"
                ]
            )
        else:
            return Response(
                text="❌ An error occurred while saving your password. Please try again or contact support.",
                suggestions=["Try again", "Contact support"]
            )
    
    def handle(self) -> Response:
        """
        Handle password reset request (display user info).
        
        Returns:
            Response: Response object with user information
        """
        return Response(
            text=f"🔐 Password Reset for {self.USER_NAME}\n\n"
                 f"User ID: {self.USER_ID}\n"
                 f"You will be prompted to enter a new password.\n\n"
                 f"Password Requirements:\n"
                 f"• At least 8 characters long\n"
                 f"• At least one uppercase letter\n"
                 f"• At least one lowercase letter\n"
                 f"• At least one number",
            suggestions=[
                "Enter new password when prompted",
                "Return to main menu"
            ]
        )
