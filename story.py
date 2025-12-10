import string

with open("story.txt", "r") as file:
    text = file.read()
    text = text.lower()
    
for punct in string.punctuation:
    text = text.replace(punct, "")

words = text.split()
    
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
        
with open("word_count.txt", "w", encoding="utf-8") as f:
    for word, counts in count.items():
        file.write(f"{word}: {counts}\n")
        
top_words = sorted(count.items(), key=lambda x: x[1], reverse=True)[:5]

print("Top 5 words:")
for word, count in top_words:
    print(f"{word}: {counts}")