import hashlib
from nicegui import ui

filename_input = ui.input("Filename")

# 3 labels
first_line = ui.label('')
num_words = ui.label('')
hash_file = ui.label('')
ui.button("Analyze File", on_click=lambda: analyze(filename_input.value))

# Button behavior
def get_first_line(path):
    # open in text mode
    with open(path, "r", encoding="utf-8") as f:
        first = f.readline()
        if first == '':
            raise ValueError("empty")
        return first.strip()
            
def count_words(path):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    # split() - any whitespace and extra spaces
    return len(data.split())

def compute_sha256(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha.update(chunk)
    return sha.hexdigest()
        
def analyze(path):
    first_line.set_text('')
    num_words.set_text('')
    hash_file.set_text('')
    try:
        first = get_first_line(path)
    except FileNotFoundError:
        first_line.set_text("File not found!")
        return
    except ValueError:
        first_line.set_text("File is empty")
        return
    
    first_line.set_text(first)
    
    try:
        words = count_words(path)
        num_words.set_text(str(words))
    except Exception:
        num_words.set_text("Cannot count words")
        
    digest = compute_sha256(path)
    if digest:
        hash_file.set_text(digest)
    else:
        hash_file.set_text("Cannot hash file")
        
ui.run()