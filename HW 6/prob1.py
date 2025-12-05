while True:
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as f:
            data = f.read()
        break
    except FileNotFoundError:
        print("File doesn't exist. Try again.")
        
characters = len(data)
words = len(data.split())
lines = len(data.splitlines())
print(f"Number of characters: {characters}")
print(f"Number of words: {words}")
print("Number of lines: {lines}")

word = input("Enter a word to search: ")
word_count = 0
for w in words:
    if w == word.lower():
        word_count += 1
    print("There are {word_count} occurrences of {word} in {filename}.")
    
replace = input("Replace? (y/n)")
if replace.lower() == "y":
    replacement = input("Enter a replacement string: ")
    new_text = data.replace(word, replacement)
    with open(filename, "w") as f:
        f.write(new_text)
    print(f"All occurances of {word} were replaced with {replacement}.")
else:
    print("No replacement performed.")