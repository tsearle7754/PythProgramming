import json
import hashlib
from pathlib import Path
from nicegui import ui
import base64

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password_hash):
        password_hash = hashlib.sha256(password_hash.encode()).hexdigest()
        self.__password = password_hash
        
    def save_user(user, path):
        path = Path(path)
        if path.exists():
            try:
                with path.open("r") as f:
                    data = json.load(f)
                
                if not isinstance(data, dict):
                    data = {}
                    
            except json.JSONDecodeError:
                ui.notify("JSONDecodeError")
                data = {}
        else:
            data = {}
        
        new_entry = {"password_hash": user.password}
        if user.username not in data:
            data[user.username] = []
        data[user.username].append(new_entry)
        
        with path.open("w") as f:
            json.dump(data, f, indent=4)
            
    def load_users(path):
        path = Path(path)
        if path.exists():
            with path.open("r") as f:
                data = json.load(f)
                keys = data.keys()
                usernames = list(keys)
                print(usernames)
        else:
            print([])
    
def save_file(path):
    path = Path(path)
    u = User(input_username.value, input_password.value)
    u.save_user(path)
    ui.notify("Saved!")
    
def show_all(path):
    path = Path(path)
    User.load_users("users.json")

#labels/inputs
input_username = ui.input("Username:")
input_password = ui.input("Password:")
usernames_display = ui.label('')

#buttons
ui.button("Save User", on_click=lambda: save_file("users.json"))
ui.button("Show All Users", on_click=lambda:show_all("users.json"))

ui.run()