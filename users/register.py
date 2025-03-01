from helpers import is_valid_email, is_valid_phone, is_strong_password, load_database, save_database
from users.user import User

def register():
    print("\nRegister")
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    phone = input("Enter your phone: ").strip()

    if not is_valid_email(email):
        print("Invalid email format.")
        return None
    if not is_valid_phone(phone):
        print("Invalid phone number format.")
        return None
    if not is_strong_password(password):
        print("Password must be at least 8 characters long.")
        return None
    
    user = User(first_name, last_name, email, password, phone)
    data = load_database()
    data["users"].append(user.to_dict())
    save_database(data)
    print("Registered successfully!")
    return user
