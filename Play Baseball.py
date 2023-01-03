#201911202 류기범 PlayBaseball ㅇ

import random

answer = random.sample(range(0,10),3)

print(answer)

count = 0

while True:
    strike = 0
    ball = 0
    user = input("세자리 숫자를 입력하시오: ")
    user_list = list(map(int, user))
    num1 = int(user_list[0])
    num2 = int(user_list[1])
    num3 = int(user_list[2])
    if answer[0] == num1:
        strike += 1
    elif answer[0] == num2 or answer[0] == num3:
        ball += 1
    if answer[1] == num2:
        strike += 1
    elif answer[1] == num1 or answer[1] == num3:
        ball += 1
    if answer[2] == num3:
        strike += 1
    elif answer[2] == num1 or answer[2] == num2:
        ball += 1
    count += 1
    print("Strike:", strike,"Ball:", ball)
    if strike == 3:
        break
print('You Win!')
print("You have played",count,"times.")
