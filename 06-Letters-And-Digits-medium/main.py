word = input("Enter the word: ")

count_of_digits = 0
count_of_letters = 0
for x in word:
    if x.isdigit():
        count_of_digits = count_of_digits +1
    elif x.lower()!=x.upper():
        count_of_letters = count_of_letters + 1
print(count_of_letters," ",count_of_digits)
