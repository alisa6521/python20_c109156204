m=int(input("輸入階層值M："))
n=1
i=1
while(n<=m):
    n=n*i
    i=i+1
print("超過M為%4d的最小階層為：%2d"%(m,i-1))