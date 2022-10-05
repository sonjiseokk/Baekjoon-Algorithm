# 문제
# a층의 b호는 a-1층 b호까지를 합친 수를 가지고 있다.

# 조건 1. 입력 층 인원을 구하려면 밑에 층의 인원을 알고 있어야 한다.

# 0층을 구현해둔 뒤, temp 리스트를 해당 호 인원이 아닌 누적 순으로 담는다.
# temp_floor를 temp로 교체해서 층을 계속 올라간다.
# 해당 층에 맞는 a층의 b호 인원 수가 출력된다.

test_case = int(input())

for i in range(test_case):
    floor = int(input())
    num = int(input())

    #0층 구현
    temp_floor =[]
    for tem in range(1,num+1):
        temp_floor.append(tem)
    
   
    for i in range(floor):
        temp =[]
        for j in range(num):
            x = sum(temp_floor[:j+1])
            temp.append(x)
        temp_floor = temp
    
    print(temp_floor[num-1])

        
        
