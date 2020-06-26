scores = input().split()
# put your python code here
score = 0
incorrect = 3
for each in scores:
    if each == 'C':
        score += 1
    if each == 'I':
        incorrect -= 1
        if incorrect == 0:
            print("Game over")
            break
else:
    print("You won")
print(score)
