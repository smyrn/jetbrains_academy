total = 0
counter = 0

while True:
    num = input()
    if num == '.':
        break
    counter += 1
    total += int(num)

print(total / counter)
