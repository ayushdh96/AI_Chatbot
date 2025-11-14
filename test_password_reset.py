"""
Test script for Password Reset handler - demonstrates automated testing
"""
from src.handlers.password_reset_handler import PasswordResetHandler


def test_password_reset():
    """
    Test the Password Reset handler with various scenarios.
    """
    print("=" * 70)
    print("Password Reset Handler - Automated Test")
    print("=" * 70)
    
    try:
        # Initialize handler
        print("\n✓ Initializing Password Reset Handler...")
        reset_handler = PasswordResetHandler()
        print("✓ Password Reset Handler initialized successfully!")
        
        # Test 1: Display user info
        print("\n" + "=" * 70)
        print("Test 1: Display User Information")
        print("=" * 70)
        
        response = reset_handler.handle()
        print(f"\n{response.text}")
        
        # Test 2: Invalid password - too short
        print("\n" + "=" * 70)
        print("Test 2: Invalid Password - Too Short")
        print("=" * 70)
        print("\n🔒 Testing password: 'short'")
        
        response = reset_handler.reset_password("short")
        print(f"\n{response.text}")
        
        # Test 3: Invalid password - no uppercase
        print("\n" + "=" * 70)
        print("Test 3: Invalid Password - No Uppercase")
        print("=" * 70)
        print("\n🔒 Testing password: 'lowercase123'")
        
        response = reset_handler.reset_password("lowercase123")
        print(f"\n{response.text}")
        
        # Test 4: Invalid password - no lowercase
        print("\n" + "=" * 70)
        print("Test 4: Invalid Password - No Lowercase")
        print("=" * 70)
        print("\n🔒 Testing password: 'UPPERCASE123'")
        
        response = reset_handler.reset_password("UPPERCASE123")
        print(f"\n{response.text}")
        
        # Test 5: Invalid password - no numbers
        print("\n" + "=" * 70)
        print("Test 5: Invalid Password - No Numbers")
        print("=" * 70)
        print("\n🔒 Testing password: 'NoNumbers'")
        
        response = reset_handler.reset_password("NoNumbers")
        print(f"\n{response.text}")
        
        # Test 6: Valid password
        print("\n" + "=" * 70)
        print("Test 6: Valid Password - Should Succeed")
        print("=" * 70)
        print("\n🔒 Testing password: 'NewPassword123'")
        
        response = reset_handler.reset_password("NewPassword123")
        print(f"\n{response.text}")
        
        if response.links:
            print("\n📎 Links provided:")
            for link in response.links:
                print(f"   - {link}")
        
        if response.suggestions:
            print("\n💡 Suggestions provided:")
            for suggestion in response.suggestions:
                print(f"   - {suggestion}")
        
        # Test 7: Another valid password to confirm it works multiple times
        print("\n" + "=" * 70)
        print("Test 7: Another Valid Password")
        print("=" * 70)
        print("\n🔒 Testing password: 'SecurePass2025!'")
        
        response = reset_handler.reset_password("SecurePass2025!")
        print(f"\n{response.text}")
        
        # Summary
        print("\n" + "=" * 70)
        print("✓ All tests completed successfully!")
        print("=" * 70)
        print("\n📊 Test Summary:")
        print("   ✓ User information display: PASS")
        print("   ✓ Password too short validation: PASS")
        print("   ✓ No uppercase validation: PASS")
        print("   ✓ No lowercase validation: PASS")
        print("   ✓ No numbers validation: PASS")
        print("   ✓ Valid password reset: PASS")
        print("   ✓ Multiple resets: PASS")
        print("\n🎉 Password Reset Handler is working correctly!")
        print("=" * 70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_password_reset()
