n = int(input())

fcfs = []
for _ in range(n):
    x,y = map(int,input().split())
    fcfs.append([x,y])

start_time = 0
end_time = 0
for search in fcfs:
    end_time = max(end_time,search[1])
    start_time = min(start_time,search[0])

queue = []
count = 0
min_time = end_time
for i in range(end_time+1):
    if min_time == i:
        count+=1
        queue = []
        min_time = end_time
    for j in range(len(fcfs)):
        if fcfs[j][0] == i:
            queue.append(fcfs[j])
            min_time = min(min_time,fcfs[j][1])

print(count)