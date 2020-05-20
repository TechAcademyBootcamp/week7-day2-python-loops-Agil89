word = input("Enter the word: ")
d = {}
for x in word:
    if x not in d:
        d[x] = 1
    else:
        d[x] = d[x] + 1
print(d)