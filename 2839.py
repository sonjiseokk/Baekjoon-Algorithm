
num = int(input())

sum = 0
fifth = num // 5

if num % 3 == 0:
    count = num //3

del_fifth = num - (fifth * 5)
if del_fifth == 3:
    sum = fifth + 1
elif del_fifth == 0:
    sum = fifth
else:
    third = num // 3
    fifth -=1
    if fifth == -1:
        sum = -1
    else:
        fifth_num = num
        fifth_num -= fifth * 5
        fifth_third = fifth_num // 3
        if fifth_num % 3 == 0:
            if (fifth_third + fifth) > third:
                sum = third
            else:
                sum = fifth_third + fifth  
        else:
            if num % 3 != 0:
                sum = -1
            else:
                sum = third

print(sum)
