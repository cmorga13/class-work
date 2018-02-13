def count (word, letter) :
    total = 0
    for letter in word:
        if letter == letter:
            total = total +1
    return (total)

word = raw_input("Enter word: ")
letter = raw_input("Enter letter: ")

answer = count(word, letter)

print(answer)