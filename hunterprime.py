#hgh
j=int(input())
li1=[]




for n in range(0,l):
   
   if n>1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
          li1.append(n)
print(*li1)
