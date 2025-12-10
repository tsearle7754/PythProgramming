from nicegui import ui
import hashlib
from pathlib import Path
import base64
import json

# functions
def save_note(path):
    hashed = hashlib.sha256(note.value.encode()).hexdigest()
    encoded = base64.b64encode(note.value.encode()).decode()
    
    path = Path(path)
    
    if path.exists():
        try:
            with path.open("r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}
            ui.notify("JSON Error: starting fresh")
    else:
        data ={}
    
    new_entry = {"encoded": encoded, "hashed": hashed}
    if username.value not in data:
        data[username.value] = []
    data[username.value].append(new_entry)
    
    with path.open("w") as f:
        json.dump(data, f, indent=4)
        
    ui.notify("Saved!")

def load_note(path):
    path = Path(path)
    
    try:
        with path.open("r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        ui.notify("JSON Error: starting fresh")
        
    text = ""
    for user, notes in data.items():
        text += f"{user}: {len(notes)} notes\n"
    display.set_text(text)

# inputs
with ui.column().classes('w-1/2 items-center gap-4'):
    username = ui.input("Enter username:")
    note = ui.input("Enter note:")

    # labels
    display = ui.label('')

    # buttons
    with ui.row().classes('gap-4'):
        ui.button("Save Note", on_click=lambda: save_note("notes.json"))
        ui.button("Load Note", on_click=lambda: load_note("notes.json"))