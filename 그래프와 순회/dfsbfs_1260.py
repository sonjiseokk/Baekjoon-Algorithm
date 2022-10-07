from collections import deque
import sys
input = sys.stdin.readline

# 문제
# DFS와 BFS를 구현하면 되는 문제이다. 개념이 조금 부족한 상태였기에 이 문제를 풀면서 개념을 익혔다.
# 따라서 조건과 풀이는 생략하도록 하겠다. (이전 BFS, DFS와 동일한 로직이나 코드를 다듬은 수준이라)

def dfs(graph,start):
    visited = []

    stack = []
    stack.append(start)
    while stack:
        w = stack.pop()
        if w not in visited:
            visited.append(w)
            stack.extend(reversed(graph[w]))
    return visited

def bfs(graph,start):
    visited = []
    queue = deque([start])
    while queue:
        w = queue.popleft()
        if w not in visited:
            visited.append(w)
            queue.extend(graph[w])
    return visited
n,m,start = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    graph[i].sort()

x = dfs(graph,start)
y = bfs(graph,start)

print(*x)
print(*y)