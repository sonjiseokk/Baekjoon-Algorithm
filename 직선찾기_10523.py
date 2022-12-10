import random
n = int(input())
p = int(input())
dot = []
temp = 'impossible'
if n == 1:
    temp = "possible"

else:
    if n*p%100 == 0:
        want = n*p//100
    else:
        want = n*p//100 + 1

    for _ in range(n):
        dot.append(list(map(int,input().split())))

    def cnt(a,b):
        ret = 0
        for i in range(n):
            ret += (b[1] - a[1]) * (dot[i][0] - a[0]) == (dot[i][1] - a[1]) * (b[0]-a[0])
        return ret

    for i in range(150):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        while (a==b):
            b = random.randint(0,n-1)
        if cnt(dot[a],dot[b]) >= want:
            temp = 'possible'
            break

print(temp)

"""
int cnt(p x, p y){
	int ret = 0;
	for(auto i : v){
		ret += (y.y - x.y)*(i.x - x.x) == (i.y - x.y)*(y.x - x.x);
	}
	return ret;
}

int main(){
	rd = mt19937((unsigned)chrono::steady_clock::now().time_since_epoch().count());
	uniform_int_distribution<int> ran(0, n-1);

	for(int loop=0; loop<150; loop++){
		int a = ran(rd);
		int b = ran(rd);
		while(a == b) b = ran(rd);
		if(cnt(v[a], v[b]) >= want){
			cout << "possible"; return 0;
		}
	}
	cout << "impossible";
}
"""