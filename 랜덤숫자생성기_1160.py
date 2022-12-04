def mul(n,matrix1,matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= m
    return result

# 2분할
def devide(n,b,matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n,matrix,matrix)
    else:
        tmp = devide(n,b//2,matrix)
        if b%2 == 0:
            return mul(n,tmp,tmp)
        else:
            return mul(n,mul(n,tmp,tmp),matrix)

m, a, c, x0, n, g = map(int,input().split())

x0 %= m 

x1 = ((a*x0)+c) % m
u = [[x0,1],[0,0]]
v = [[a,0],[c,1]]

rst = mul(2,u,devide(2,n,v))

print(rst[0][0]%g)

