import random
import bisect

n , c = map(int,input().split())
color = list(map(int,input().split()))
color.insert(0,-1)
m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    ans = -1
    for i in range(50):
        j = random.randint(0, 2147483647) % (b-a+1) + a
        k = color[j]
        cnt = bisect.bisect_left(color,b) - bisect.bisect_right(color,a)
        if cnt > (b-a+1)//2:
            ans = k; 
            break
    
    if ans < 0 :
        print('no')
    else:
        print('yes',ans)


	
