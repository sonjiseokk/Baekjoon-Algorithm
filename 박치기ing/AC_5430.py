# t = int(input())

# for i in range(t):
#     move = list(input())
#     arr_len = int(input())
#     arr = list(input().split(','))

arr = '[1,2,3,4]'
arr = arr.split(',')
arr[0] = ''
arr[-1] = ''


print(arr)