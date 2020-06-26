word = input()

snake_case_word = ""
for letter in word:
    if letter.isupper():
        snake_case_word += ("_" + letter.lower())
    else:
        snake_case_word += letter
print(snake_case_word)
