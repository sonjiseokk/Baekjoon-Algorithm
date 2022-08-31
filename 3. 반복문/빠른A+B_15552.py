# 문제
# sys.stdin.readline을 이용하여 빠르게 문자열을 읽어오는 문제
# sys.stdin.readline을 여기서 처음 접했기에 추가함.

import sys
len_input = int(sys.stdin.readline())

sum = []
for i in range(len_input):
    a,b = map(int, sys.stdin.readline().split())
    sum.append(a+b)

for i in range(len_input):
    print(sum[i])