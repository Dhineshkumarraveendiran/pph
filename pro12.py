#gf
n,t = map(int,input().split())
n = list(map(int,input().split()))
for i in range(t):
    b ,e = map(int,input().split())
    res = sum(n[b-1:e])
    # print(*n[b-1:e])
    print(res)
