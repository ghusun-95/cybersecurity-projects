#فكرة المشروع:
#أداة بسيطة لإدارة الحسابات وكلمات المرور عبر الترمينال (CLI)، 
#تستخدم خوارزمية التجزئة (SHA-256 Hashing) لتشفير وحماية كلمات المرور.


import hashlib
import getpass
import json
import os
import re

# اسم الملف الذي ستُحفظ فيه البيانات تلقائياً
DATA_FILE = "users.json"

def load_users():
    """Load accounts from file if it exists"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_users(users_data):
    """Save accounts to file"""
    with open(DATA_FILE, "w") as file:
        json.dump(users_data, file, indent=4)

def is_strong_password(password):
    """Check password strength requirements"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, "Strong password!"

def create_account(users):
    username = input("Enter your desired username: ")
    
    if username in users:
        print("Error: Username already exists!")
        return

    password = getpass.getpass("Enter your desired password: ")
    
    # التحقق من قوة كلمة المرور
    is_valid, message = is_strong_password(password)
    if not is_valid:
        print(f"Password Error: {message}")
        return

    # تشفير كلمة المرور وتخزينها
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    
    # حفظ التحديثات في الملف فوراً
    save_users(users)
    print("Account created and saved successfully!")

def login(users):
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # المطابقة
    if username in users and users[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    # تحميل الحسابات عند بداية تشغيل البرنامج
    users = load_users()

    while True:
        choice = input("\nEnter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account(users)
        elif choice == "2":
            login(users)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
    