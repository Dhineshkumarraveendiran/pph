# q
n=int(input())
li1=list(map(int,input().split( )))
li2=list(map(int,input().split( )))
li3=[]
for i in range(0,n):
    w=li1[i]+li2[i]
    li3.append(w)
print(*li3)
