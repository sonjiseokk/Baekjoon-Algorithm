import sys

input = sys.stdin.readline
case = int(input())

for _ in range(case):
    n = int(input())
    tmp = 1
    employee = []

    for i in range(n):
        employee.append(tuple(map(int,input().split())))

    employee.sort()
    min_two = employee[0][1]
    for i in range(1,n):
        if min_two > employee[i][1]:
            min_two = employee[i][1]
            tmp+=1

    print(tmp)
