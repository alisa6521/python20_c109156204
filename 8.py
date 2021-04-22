a=int(input("輸入第一行正整數為："))
b=(input("第二行中數列中的數字為："))
list1=[]

for i in range(0,10):
    j=str(i)
    e=b.count(j)
    list1.append(e)
max1=max(list1)
if max1<=1:
    print("每個數字剛好只出現1次")
else:
    for k in range(0,10):
        if list1[k]==max1:
            print("最大出現次數的數字為：",k)
            print("出現次數為：",max1)
        else:
            continue        
          
