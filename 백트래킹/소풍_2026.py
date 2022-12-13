k, n, f= map(int,input().split())

relation = [[] for _ in range(n+1)]
for _ in range(f):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

res = []
def find_friends(cur, friends):
    global res
    if res:
        return
    if len(friends) == k:
        res = sorted(friends)
        return
    for i in range(cur+1, n+1):
        if not visited[i]:
            for num in friends:
                if num not in set(relation[i]):
                    break
            else:
                visited[i] = True
                find_friends(i, friends+[i])
for i in range(1, n+1):
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    find_friends(i, [i])
    if res:
        break

if not res:
    print(-1)
else:
    for x in res:
        print(x)
