#sjkfskf
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if(a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
	print("yes")
else:
	print("no")
