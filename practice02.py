

a = int(input('수를 입력하세요'))
# if (a/2) - (a/2) == 0:
#     print('짝수')
# else: a % 2 != 0:

if a % 2 == 0:
    print('짝수')
else:
    print('홀수')

#while
while True:
    i = input('정수를 입력하세요')
    if i == 'quit':
        break
    if i.isdigit() is False:
        break

    i = int(i)
    print('짝수' if i % 2 == 0 else '홀수')
