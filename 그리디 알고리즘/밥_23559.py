import heapq
n,money_limit = map(int,input().split())

taste = []

for i in range(n):
    a,b = map(int,input().split())
    taste.append((a,b))

taste.sort(key=lambda b: (b[0] - b[1]), reverse=True)

ans = sum(i[1] for i in taste)

money_limit -= (1000 * n)

for case in taste:
    if money_limit >= 4000 and case[0] > case[1]:
        money_limit-=4000
        ans-=case[1]
        ans += case[0]
    else:
        break

print(ans)



    
