import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start):
    global count 
    result = []
    
    answer[start] = count
    for v in graph[start]:
        if answer[v]:
            continue
        count +=1
        dfs(v)
    return


n,m,start = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for lst in graph:
    lst.sort()
count = 1
answer = [0] * (n+1)
a = dfs(start)

for x in answer[1:]:
    print(x)