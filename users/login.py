from helpers import load_database

def sign_in():
    print("\nSign In")
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    
    data = load_database()
    users = data["users"]
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Signed in successfully!")
            return user
    print("Invalid credentials. Please try again.")
    return None
