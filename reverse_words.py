def reverse_words(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return(" ".join(words))

print(reverse_words("Hello world"))
print(reverse_words("Python is fun"))