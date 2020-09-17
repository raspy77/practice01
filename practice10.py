

n = int(input("숫자 : "))

a, b = 0, 0
for num in range(n+1):
    if num % 2 == 0:
        a += num
    elif num % 2 == 1:
        b += num
print(max(a, b))

# total = 0
#
# if n % 2 == 0:
#     for num in range(n+1):
#         if num % 2 == 1:
#             continue
#         total += num
# else:
#     for num in range(n+1):
#         if num % 2 == 0:
#             continue
#         total += num
#
# print(total)
