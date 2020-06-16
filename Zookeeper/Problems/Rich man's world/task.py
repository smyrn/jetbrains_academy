balance = float(input())
years = 0

while balance < 700000:
    balance += balance * 0.071
    years += 1

print(years)
