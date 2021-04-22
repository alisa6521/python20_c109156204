a=input("輸入一組四位數字為：")
list1=[]
b=0
c=''
for i in range(0,4):
    b=int(a[i])    
    b=(b+7)%10    
    list1.append(b)
b=list1[0]
list1[0]=list1[2]
list1[2]=b

b=list1[1]
list1[1]=list1[3]
list1[3]=b

for j in range(0,4):
    c=c+str(list1[j])
print("輸出加密後的數字為："+c)