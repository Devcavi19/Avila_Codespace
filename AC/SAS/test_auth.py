import pytest
import bcrypt
# Assuming the solution is in auth_challenge.py
# We import the functions and the global database dictionary
from AuthenticationandPasswordSecurity_ActivitySol import register_user, login_user, user_database

# Fixture to automatically clear the user_database before each test function
@pytest.fixture(autouse=True)
def clear_db_before_test():
    user_database.clear()
    yield # Allows the test to run
    user_database.clear() # Optional: clear after test too

def test_successful_registration(capsys):
    """Tests if a new user can be registered successfully."""
    register_user("testuser1", "Pass1")
    captured = capsys.readouterr()
    assert "Registration successful\n" == captured.out
    assert "testuser1" in user_database
    # Verify the stored password is a valid bcrypt hash (optional but good)
    assert bcrypt.checkpw(b"Pass1", user_database["testuser1"])

def test_register_existing_user(capsys):
    """Tests that registering a user with an existing username fails."""
    register_user("testuser2", "PassA") # First registration
    capsys.readouterr() # Clear previous stdout capture
    register_user("testuser2", "PassB") # Attempt duplicate registration
    captured = capsys.readouterr()
    assert "Username already exists\n" == captured.out
    # Ensure the original password wasn't overwritten
    assert bcrypt.checkpw(b"PassA", user_database["testuser2"])
    assert not bcrypt.checkpw(b"PassB", user_database["testuser2"])

def test_successful_login(capsys):
    """Tests if a registered user can log in with the correct password."""
    register_user("logUser", "Secret123")
    capsys.readouterr() # Clear registration output
    login_user("logUser", "Secret123")
    captured = capsys.readouterr()
    assert "Login successful\n" == captured.out

def test_login_incorrect_password(capsys):
    """Tests that login fails with an incorrect password."""
    register_user("logUser2", "MyPass")
    capsys.readouterr() # Clear registration output
    login_user("logUser2", "WrongPass")
    captured = capsys.readouterr()
    assert "Incorrect password\n" == captured.out

def test_login_user_not_found(capsys):
    """Tests that login fails if the username does not exist."""
    login_user("ghost", "nopass")
    captured = capsys.readouterr()
    assert "User not found\n" == captured.out
    assert "ghost" not in user_database

def test_username_case_sensitivity_register(capsys):
    """Tests that usernames are treated as case-sensitive during registration."""
    register_user("CaseUser", "Pass1")
    capsys.readouterr() # Clear first registration output
    register_user("caseuser", "Pass2") # Should be treated as a different user
    captured = capsys.readouterr()
    assert "Registration successful\n" == captured.out
    assert "CaseUser" in user_database
    assert "caseuser" in user_database
    assert user_database["CaseUser"] != user_database["caseuser"] # Hashes should differ

def test_username_case_sensitivity_login(capsys):
    """Tests that usernames are treated as case-sensitive during login."""
    register_user("LoginCase", "Pass123")
    capsys.readouterr() # Clear registration output
    login_user("logincase", "Pass123") # Attempt login with incorrect username case
    captured = capsys.readouterr()
    assert "User not found\n" == captured.out

def test_password_case_sensitivity_login(capsys):
    """Tests that passwords are treated as case-sensitive during login."""
    register_user("PassCase", "SensitivePass")
    capsys.readouterr() # Clear registration output
    login_user("PassCase", "sensitivepass") # Attempt login with incorrect password case
    captured = capsys.readouterr()
    assert "Incorrect password\n" == captured.out

def test_special_chars_password(capsys):
    """Tests registration and login with special characters in the password."""
    password_special = "!@#$%^&*()_+=-`~[]{};':\",./<>?"
    register_user("SpecialUser", password_special)
    capsys.readouterr() # Clear registration output
    login_user("SpecialUser", password_special)
    captured = capsys.readouterr()
    assert "Login successful\n" == captured.out

def test_multiple_users_interleaved(capsys):
    """Tests handling multiple users with mixed success/failure logins."""
    register_user("userA", "passA")
    register_user("userB", "passB")
    register_user("userC", "passC")
    capsys.readouterr() # Clear registration output

    login_user("userA", "passA")
    captured_a = capsys.readouterr()
    assert "Login successful\n" == captured_a.out

    login_user("userB", "wrongPassword")
    captured_b = capsys.readouterr()
    assert "Incorrect password\n" == captured_b.out

    login_user("userC", "passC")
    captured_c = capsys.readouterr()
    assert "Login successful\n" == captured_c.out

    login_user("userA", "wrongAgain")
    captured_a2 = capsys.readouterr()
    assert "Incorrect password\n" == captured_a2.out

def test_empty_password_handling(capsys):
    """Tests registration and login with an empty password string."""
    # Bcrypt generally handles empty strings, so this should work if implemented correctly.
    register_user("emptyPassUser", "")
    captured_reg = capsys.readouterr()
    assert "Registration successful\n" == captured_reg.out
    assert "emptyPassUser" in user_database

    login_user("emptyPassUser", "")
    captured_login = capsys.readouterr()
    assert "Login successful\n" == captured_login.out

    login_user("emptyPassUser", " ") # Test login with a space vs empty
    captured_login_fail = capsys.readouterr()
    assert "Incorrect password\n" == captured_login_fail.out

# To run these tests:
# 1. Make sure pytest and bcrypt are installed: pip install pytest bcrypt
# 2. Save the solution code as auth_challenge.py in the same directory.
# 3. Save this test code as test_auth_challenge.py in the same directory.
# 4. Run pytest -v from your terminal in that directory: pytest -v