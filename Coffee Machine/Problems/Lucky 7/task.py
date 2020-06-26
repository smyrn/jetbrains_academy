n = int(input())
input_list = []

for _x in range(n):
    input_list.append(int(input()))

for num in input_list:
    if num % 7 == 0:
        print(num ** 2)
