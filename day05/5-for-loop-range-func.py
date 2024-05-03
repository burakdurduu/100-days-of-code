result = 0
for i in range(0, 101):
    result += i
print(result)

total = 0
for i in range(0, 101, 2):
    total += i
print(total)

total2 = 0
for i in range(0, 101):
    if i % 2 == 0:
        total2 += i
print(total2)
