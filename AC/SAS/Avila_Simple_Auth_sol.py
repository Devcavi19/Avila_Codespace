import bcrypt
import sys

# In-memory database to store users and their hashed passwords
user_database = {}

def register_user(username, password):
    
    """Register a new user with the given username and password, storing a hashed version of the password in the database."""
    
    if username in user_database:
        print("Username already exists")
        return

    # Convert password to bytes (required by bcrypt)
    password_bytes = password.encode('utf-8')
    
    # Hash the password with bcrypt (automatically generates salt)
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    
    # Store the user in the database
    user_database[username] = hashed_password
    print("Registration successful")

def login_user(username, password):
    
    """Authenticate a user by checking the provided username and password against stored credentials."""
    
    if username not in user_database:
        print("User not found")
        return
    
    # Convert password to bytes for verification
    password_bytes = password.encode('utf-8')
    
    # Check if the provided password matches the stored hash
    if bcrypt.checkpw(password_bytes, user_database[username]):
        print("Login successful")
    else:
        print("Incorrect password")

def process_commands(file_path=None):
    
    """Process authentication commands from standard input or a file, where file_path is an optional path to a file containing commands."""
    
    if file_path:
        # Read commands from the specified file
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # First line contains the number of commands
            n = int(lines[0].strip())
            
            # Process each command
            for i in range(1, n + 1):
                command = lines[i].strip().split(maxsplit=2)
                
                operation = command[0]
                username = command[1]
                password = command[2]
                
                if operation == "REGISTER":
                    register_user(username, password)
                elif operation == "LOGIN":
                    login_user(username, password)
    else:
        # Read from standard input
        # Read the number of commands
        n = int(input().strip())
        
        # Process each command
        for _ in range(n):
            command = input().strip().split(maxsplit=2)
            
            operation = command[0]
            username = command[1]
            password = command[2]
            
            if operation == "REGISTER":
                register_user(username, password)
            elif operation == "LOGIN":
                login_user(username, password)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If a file path is provided as a command-line argument, use it
        process_commands(sys.argv[1])
    else:
        # Otherwise, read from standard input
        process_commands()