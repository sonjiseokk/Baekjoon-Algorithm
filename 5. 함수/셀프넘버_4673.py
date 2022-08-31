# 문제
# 계산식을 통해 계산된 num을 쭉 나열하되 하나씩만 출력해야 하는 문제

# set 이라는 집합 자료형을 통해 remove 리스트를 따로 만들어두고
# 이를 그대로 차집합 하여 간단하게 해결 가능.

numbers = set(range(1,10001))
remove_num = set()
for num in numbers:
    for n in str(num):
        num+=int(n)
    if num <=10000:
        remove_num.add(num)

self_numbers = numbers - remove_num

for i in sorted(self_numbers):
    print(i)
    

