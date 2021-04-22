person=int(input("小明身上有幾元："))
sell=int(input("販賣機有幾種飲料："))
list1=[]
for i in range(0,sell):
    drink=int(input())
    list1.append(drink)
sum1=0
for j in range(0,sell):
    if person>= list1[j]:
        sum1=sum1+1

print(sum1)