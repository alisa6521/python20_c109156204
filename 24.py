a1=input("請輸入考試次數及學生數：")
a2=input("每次考試所佔的比率：")
test=a1.split(" ")
per=a2.split(" ")
list3=[]
list4=[]
tt=int(test[0]) #考試次數
stu=int(test[1]) #學生數量

for i in range(0,stu): #建立分數的資料
    list3.append([])
    a=input()
    for j in range(0,tt):
        b=int(a.split(" ")[j])
        list3[i].append(b)
sum1=0
for k in range(0,stu):
    for l in range(0,tt):
        sum1=sum1+int(list3[k][l])*float(per[l])
    
avg=float(sum1/stu)
print("全班的總平均值為：%3.2f"%(avg))
