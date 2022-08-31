#이게 왜 시간초과나는지 모르겠음 아마 true한번 도는거 차이인거같은데?
import math

num = int(input())

check_list = [True for _ in range(num+1)]

a = int(math.sqrt(num))
for x in range(2, a + 1):
    if check_list[x] == True:
        j = 2
        while x * j <= num:
            check_list[x*j] = False
            j+=1
check_list[0] = False
check_list[1] = False

sosu_list = []
for i in range(num+1):
    if check_list[i] == True:
        sosu_list.append(i)

index_sosu = 0
result = []
while num > 1:
    if num % sosu_list[index_sosu] == 0:
        num = num // sosu_list[index_sosu]
        result.append(sosu_list[index_sosu])
    else:
        index_sosu+=1

for p in result:
    print(p)