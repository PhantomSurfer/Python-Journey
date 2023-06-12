#Word Counter
from collections import Counter
file = open("sample.txt", "r", encoding="utf-8-sig")

word_count={}

for word in file.read().lower().replace('.', '').replace(',', '').replace('!', '').split():
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

print("These are the words that appear more than once in the paragraph:")
for item in word_count.items():
    print("word: {} \t count: {}".format(*item))

file.close()