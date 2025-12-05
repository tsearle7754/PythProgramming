import hashlib

with open("users.txt", "r") as file:
    lines = file.readlines()

with open("hashed.txt", "w") as f:
    for line in lines:
        parts = line.split(",")
        username = parts[0]
        password = parts[1]
        hash = hashlib.sha256(password.strip().encode()).hexdigest()
        
        f.write(f"{username},{hash}\n")
        
print("Total users: ", len(lines))