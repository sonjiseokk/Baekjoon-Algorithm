def backtrack(depth,idx):
    global diff
    if depth == n// 2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start+= matrix[i][j]
                elif not visited[i] and not visited[j]:
                    link += matrix[i][j]
        
        diff = min(diff,abs(start-link))
        return
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            backtrack(depth+1,i+1)
            visited[i] = False

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

visited = [False] * n
diff = int(10e9)
backtrack(0,0)

print(diff)