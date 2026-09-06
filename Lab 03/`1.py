text = " machine learning is powerful machine learning helps analyze data data science uses machine learning" 
text = text.lower()
words = text.split()

wordFreq = {}
for word in words:
    if word in wordFreq:
        wordFreq[word] += 1
    else:
        wordFreq[word] = 1

print("Word Frequencies:")
for word, count in wordFreq.items():
    print(f"\n{word}: {count}")

highestFreq = max(wordFreq, key = wordFreq.get)
print(f"\nMost Frequently Used Word: {highestFreq}")

uniqueWords = set(words)
print(f"\nUnique words: {uniqueWords}")

repeated_words = {word: count for word, count in wordFreq.items() if count > 1}
print(f"\nWords Appearing More Than Once:")
for word, count in repeated_words.items():
    print(f"{word}: {count}")
