#ghgh
n=int(input())
li=list(map(int,input().split( )))
m=0
u=m
for i in range(0,len(li)):
    if i%2==0:
        u=u+li[i]
    else:
        m=m+li[i]
if u>m:
    print(u)
else:
    print(m)
        
