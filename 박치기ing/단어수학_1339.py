n = int(input())

a = input()
b = input()
sub = ['A','B','C','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
if len(a) < len(b):
    length = len(b)
    plus = len(b) - len(a)
    a = ('#' * plus) + a
else:
    length = len(a)
    plus = len(a) - len(b)
    b = ('#' * plus) + b

def compare(long_num,short_num):
    for i, x in enumerate(long_num):
        if short_num[i] == '#':
            long_num[i]