
word = 'python world'
word_with_dashes = '______ _____'

entered_letter = input('Enter the letter: ' + word_with_dashes + ': ')
while entered_letter.isdigit() or entered_letter.upper()==entered_letter.lower() or len(entered_letter)>1:
    entered_letter = input('Enter only the letter: ')
st = ''
while word !=word_with_dashes:
    if entered_letter in word_with_dashes:
        print("Letter already exists.")
    elif entered_letter not in word:
        print('Agilli ol')
    for x in range(len(word)):
        if entered_letter == word[x]:
           st=st + entered_letter
        else:
           st += word_with_dashes[x]
    word_with_dashes = st
    st = ''
    entered_letter = input('Enter the letter: ' + word_with_dashes + ': ')
