import re
import json

def load_database():
    with open("database.json", "r") as file:
        return json.load(file)

def save_database(data):
    with open("database.json", "w") as file:
        json.dump(data, file, indent=4)

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    pattern = r'^(\+20|0)1[0-9]{9}$'
    return re.match(pattern, phone) is not None

def is_strong_password(password):
    return len(password) >= 8
