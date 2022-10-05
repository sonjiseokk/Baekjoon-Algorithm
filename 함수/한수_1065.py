# 문제
# 한수란 표현을 여기서 처음 들어 봤는데

# 한수는 입력된 숫자가 123 이라 가정하면 1, 2, 3 이라는 숫자들이
# 1이라는 공차로 등차수열을 이루므로 한수로 취급한다.

# 따라서 이 한수를 이해한다면 풀이는 쉽다
# 공차를 따로 생성하여 그에 맞는 공차이면 체크하는 식으로 풀이하면 된다.

maximum = int(input())
count = 0
for num in range(1,maximum+1):
    if num <10:
        count+=1
    else:
        list_num = list(map(int,str(num)))
        tol = list_num[1] - list_num[0]
        check = 0
        for i in range(1,len(list_num)):
            if (list_num[i] - list_num[i-1]) == tol:
                check+=1
        
        if len(list_num) -1 == check:
            count+=1 

print(count)
