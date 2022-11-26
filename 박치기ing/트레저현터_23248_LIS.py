
m,n,k = map(int,input().split())

coin_list = []
for _ in range(k):
    a,b = map(int,input().split())
    coin_list.append((a,b))

coin_list.sort(key=lambda x:x[1])
coin_list.sort(key = lambda x:x[0])

def get_lis_improved(lis_list):
    L = [lis_list[0]]

    for i in range(1, len(lis_list)):
        if L[-1][0] <= lis_list[i][0]:
            if L[-1][1] <= lis_list[i][1]:
                L.append(lis_list[i])
    return L

count = 0
while coin_list:
    del_list = get_lis_improved(coin_list)
    coin_list = list(set(coin_list) - set(del_list))
    coin_list.sort(key=lambda x:x[1])
    coin_list.sort(key = lambda x:x[0])
    count+=1

print(count)