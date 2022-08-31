m,n = map(int,input().split())

count = 0
for _ in range(m):
    user_input = list(input())
    start = user_input[0]
    if start == 'B':
        temp = 'W'
    else:
        temp = 'B'
    for i in range(n):
        start = user_input[i]
        if start == 'B' and temp == 'B':
            temp = 'W'
            count +=1
        elif start == 'W' and temp == 'W':
            temp = 'B'
            count +=1
        else:
            if start == 'B':
                temp = 'B'
            else:
                temp = 'W'

print(count)

#BBBBBBBBBBBBBBBBBBBBBBW
#BWBWBWBWBWBWBWBWBWBWBWB