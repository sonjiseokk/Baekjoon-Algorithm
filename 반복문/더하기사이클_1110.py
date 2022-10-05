# 문제
# 정해진 사이클을 통해 입력받은 숫자들 돌리고 
# 원래 숫자로 돌아오는 사이클의 횟수를 구하는 문제
# 두 자리수 케이스를 구분하고 sum이 value와 같아질 때 까지 무한루프를 돌리면 해결 가능

value = int(input())
count = 0
new_value = value
while (1):
    if new_value < 10:
        sum = 0 + new_value
        new_value = (new_value * 10) + sum
        count+=1

    else:
        two_digit = new_value // 10
        one_digit = new_value % 10
        sum = (two_digit + one_digit) % 10
        new_value = (one_digit * 10) + sum
        count+=1
    if new_value == value:
        break

print(count)