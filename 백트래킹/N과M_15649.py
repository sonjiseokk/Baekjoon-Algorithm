def backtrack():
    if len(result) == m:
        print(' '.join(map(str,result)))
        return
    for i in range(1,n+1):
        if i not in result:
            result.append(i)
            backtrack()
            result.pop()
n,m = map(int,input().split())
result = []
arr = []
backtrack()


# n,m = list(map(int,input().split()))
 
# s = []
 
# def dfs():
#     if len(s)==m:
#         print(' '.join(map(str,s)))
#         return
    
#     for i in range(1,n+1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()
 
# dfs()