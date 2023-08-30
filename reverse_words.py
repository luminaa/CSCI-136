def reverse_words(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return(" ".join(words))


word1 = "Hello world"
word2 = "Python is fun"
print(reverse_words(word1))
print(reverse_words(word2))