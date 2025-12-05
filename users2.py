import hashlib

try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    with open("users_hashed.txt", "r") as file:
        for line in file:
            parts = line.split(",")
            hash_username = parts[0].strip()
            hash_password = parts[1].strip()
            input_password_hash = hashlib.sha256(password.encode()).hexdigest()
            
            if username == hash_username:
                if input_password_hash == hash_password:
                    print("Access granted")
                else:
                    print("Access denied")
                break
        else:
            raise ValueError("User not found")
            
            
except ValueError as e:
    print(e)
    
except Exception as e:
    print("Error:", e)