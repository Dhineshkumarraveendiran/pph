#hgh
null = input()
lo = list(map(int,input().split()))
bl = list(map(bin,lo))
bls1 = sorted(bl,reverse = True)
for i in bls1:
    print(int(i,2))
