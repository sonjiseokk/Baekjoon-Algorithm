# 글로벌 일케 말고 할수있는게 있지 않을까?
global count
count = 0
all_list = []
def menoi(num,fromis,to,other):
    global count
    if num == 0:
        return
    else:
        menoi(num-1,fromis,other,to)
        all_list.append([fromis,to])
        count = count + 1
        menoi(num-1,other,to,fromis)


max_num = int(input())

menoi(max_num,1,3,2)

print(count)

for x in all_list:
    print(*x)
