# 문제 
# 각 케이스 별로 점수들이 주어지고 이들의 평균이상이 몇퍼센트인지 계산하는 문제
# avg를 구한 후 단순 비교를 통해 확률을 구할 수 있음

maximum = int(input())

for i in range(maximum):
    user_input_case = list(map(int, input().split()))
    case_num = user_input_case[0]
    case_sum = sum(user_input_case[1:])
    case_avg = case_sum / case_num
    count = 0
    for x in user_input_case[1:]:
        if case_avg < x:
            count +=1
    
    case_rate = (count / case_num * 100)  
    print('%.3f%%' %case_rate)