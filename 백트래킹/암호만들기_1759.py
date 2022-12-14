import itertools

l,c = map(int,input().split())
pw = list(input().split())

mo = ['a','e','i','o','u']
ja = list(set(pw) - set(mo))
res = []
for password in itertools.combinations(pw, l):
    com = "".join(sorted(password))

    c_mo = sum(com.count(x) for x in mo)
    c_ja = sum(com.count(y) for y in ja)

    if c_ja >= 2 and c_mo >= 1:
        res.append(com)

res.sort()

for x in res:
    print(*x,sep="")
    
