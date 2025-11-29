import hashlib
from nicegui import ui

# Make an input box for the filename
filename_input = ui.input("Filename")
# Two labels- first line (or errors) and one for the hash
firstline_label = ui.label('')
hash_label = ui.label('')
# Button to trigger loading
ui.button("Load & Hash File", on_click=lambda: load_and_hash(filename_input.value))

# Write a function that reads the first line
def read_first_line(path):
    with open(path, "r", encoding="utf-8") as f:
        line = f.readline()
        if not line:
            raise ValueError("File empty")
        return line.strip()
    
# Write a function that computes the SHA-256 hash
def compute_sha256(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha.update(chunk)
    return sha.hexdigest()

# Call helpers, update labels, ensure hash only updates when successfully read
def load_and_hash(path):
    # clear labels immediately for good UX
    firstline_label.set_text('')
    hash_label.set_text('')
    try:
        first = read_first_line(path)
    except FileNotFoundError:
        firstline_label.set_text("File not found!")
        return
    except ValueError:
        firstline_label.set_text("File empty")
        return
    
    # success: show first line, then compute hash
    firstline_label.set_text(first)
    
    digest = compute_sha256(path)
    if digest:
        hash_label.set_text(digest)
    else:
        hash_label.set_text("Cannot hash file")
    
ui.run()