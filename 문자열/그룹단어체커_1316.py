# 문제
# 간단하게 한다면 더 간단하게 할 수 있는 문제이기에 조금 아쉬움

# 1. 입력을 받아서 각 문자가 연속되어 나타나는 즉, aaba 이런 식으로 나오지 않는 그룹 단어를 찾아야한다.
# 2. temp를 통해 반복문 i-1의 문자를 추적하고, check_list를 통해 중복 입력을 찾아낸다.
# 3. 플래그를 통해 주어진 여러 문자열을 전부 카운팅을 할 수 있도록 했다.

user_max = int(input())

sum = 0

for i in range(user_max):
    user_input = input()
    check_list =[]  
    for x in user_input:
        if x not in check_list:
            check_list.append(x)
            temp = x
        else:
            if x in check_list and temp != x:
                exe_flag = 0
                break
            temp = x
        exe_flag=1
    
    sum += exe_flag

print(sum)
    
