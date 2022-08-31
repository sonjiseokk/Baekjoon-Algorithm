import math

max = 246913

check_list = [True for _ in range(max+1)]

a = int(math.sqrt(max))
for x in range(2, a + 1):
    if check_list[x] == True:
        j = 2
        while x * j <= max:
            check_list[x*j] = False
            j+=1
    check_list[0] = False
    check_list[1] = False

while True:
    num = int(input())
    if num == 0:
        break
    
    min_input = num
    max_input = 2*num
    count = 0
    for i in range(min_input+1,max_input+1):
        if check_list[i] == True:
            count +=1

    print(count)


