n, k = map(int,input().split())

store = []
for _ in range(n):
    store.append(list(map(int,input().split())))

can_pick_w = []
for _ in range(k):
    can_pick_w.append(int(input()))

store.sort(key=lambda x:x[1],reverse=True)

res = 0
for can_w in can_pick_w:
    for j_w in range(len(store)):
        if can_w >= store[j_w][0]:
            res+=store[j_w][1]
            store[j_w][1] = 10e9
            break

print(res)
