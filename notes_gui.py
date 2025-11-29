import hashlib
from nicegui import ui

# Inputs
filename_input = ui.input("Filename")
content_input = ui.textarea("Write text here")
append_input = ui.input("Append text")

# Labels for results
load_output = ui.label('')
status = ui.label('')
stats_lines = ui.label('')
stats_words = ui.label('')
stats_hash = ui.label('')

# Buttons
ui.button("Save File", on_click=lambda: save_file(filename_input.value, content_input.value))
ui.button("Load File", on_click=lambda: load_file(filename_input.value))
ui.button("Append Line", on_click=lambda: append_line(filename_input.value, append_input.value))
ui.button("Analyze File", on_click=lambda: analyze_file(filename_input.value))

def save_file(path, text):
    try:
        with open(path, "w", encoding='utf-8') as f:
            f.write(text)
            status.set_text("Saved!")
    except Exception as e:
        status.set_text(f"Error saving: {e}")
        
def load_file(path):
    try:
        with open(path, "r", encoding='utf-8') as f:
            data = f.read()
        load_output.set_text(data)
        status.set_text("Loaded!")
    except FileNotFoundError:
        status.set_text("File not found!")
    except Exception as e:
        status.set_text(f"Error saving: {e}")
    
def append_line(path, line):
    try:
        with open(path, "a", encoding='utf-8') as f:
            f.write("\n" + line)
        status.set_text("Line appended!")
    except Exception as e:
        status.set_text(f"Error: {e}")
        
def analyze_file(path):
    try:
        lines = 0
        words = 0
        sha = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha.update(chunk)
        file_hash = sha.hexdigest()
        with open(path, "r", encoding='utf-8') as file:
            for line in file:
                lines += 1
                words += len(line.split())

        stats_hash.set_text(f"SHA256: {file_hash}")
        stats_lines.set_text(f"Lines: {lines}")
        stats_words.set_text(f"Words: {words}")
        status.set_text("Analysis complete!")
    except FileNotFoundError:
        status.set_text("File not found!")
    except Exception as e:
        status.set_text(f"Error analyzing: {e}")
       
ui.run()