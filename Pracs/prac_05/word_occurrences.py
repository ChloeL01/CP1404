"""
CP1404/CP5632 word occurrences - Chloe Laing

Estimate: 30 mins
Actual: 28 mins
"""

text = input("Text: ")
words = text.split(" ")
words_to_count = {}
for word in words:
    words_to_count[word] = words_to_count.get(word, 0) + 1

max_length = max(len(name) for name in list(words_to_count.keys()))

for name in sorted(words_to_count.keys()):
    print(f"{name:{max_length}} : {words_to_count[name]}")
