#q
n1=int(input())
li=list(map(int,input().split( )))
for i in range(0,n1-1):
    
    for j in range(i+1,n1):
        a=li[i]+li[j]
        if a in li:
            if li[i]!=li[j] and li[i]<li[j]:
                print(li[i],li[j],a)
