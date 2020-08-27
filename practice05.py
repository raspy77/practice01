

l = [10, 12, 14, 15, 17, 18, 19, 20, 25, 30, 32, 33, 37, 40, 42, 44, 46, 50]
cnt = 0
sum = 0
for number in l:
    if number % 3 == 0:
        cnt += 1
        sum += number

print(sum)
print(cnt)