def backtrack(x,start,operator):
    global tmp1, tmp2
    if operator == 0:
        x += num[start]
    elif operator == 1:
        x -= num[start]
    elif operator == 2:
        x *= num[start]
    elif operator == 3:
        x = int(x / num[start])
    else:
        pass

    if sum(move) == 0:
        tmp1 = max(tmp1,x)
        tmp2 = min(tmp2,x)
        return
    
    
    for i in range(4):
        if move[i] > 0:
            move[i] -= 1
            backtrack(x,start+1,i)
            move[i] +=1
            

n = int(input())

num = list(map(int,input().split()))
move = list(map(int,input().split()))

tmp1 = -10e9
tmp2 = 10e9

backtrack(num[0],0,5)

print(tmp1)
print(tmp2)

