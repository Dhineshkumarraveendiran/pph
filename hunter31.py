#r
a=int(input())
li=list(map(int,input().split( )))
b=1
for i in li:
    b=b*i
if b<0:
    print(b*(-1))
else:
    print(b)
