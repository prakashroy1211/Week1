# Login credentials (hardcoded)
USERNAME = "admin"
PASSWORD = "1234"

def login():
    print("Welcome to the Secure Login System")

    try:
        for attempt in range(3):
            user = input("Enter username: ").strip()
            pwd = input("Enter password: ").strip()

            # Error handling for empty or whitespace only as input
            if not user or not pwd:
                print("Username or password cannot be empty.")
                continue

            if user == USERNAME and pwd == PASSWORD:
                print("Login successful!")
                return True
            else:
                print(f"Invalid credentials.")
        
        # After 3 failed attempts
        print("Too many failed attempts. Access denied.")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# --- Main Program ---
if __name__ == "__main__":
    login()