group=input("組數為：")
a=0
g=int(group)
list1=[]
list2=[250,175]
sum1=0
for i in range(0,g):
    list1.append([])
    a=input("第"+str(i+1)+"組：")
    a1=a.split(" ")[0]
    a2=a.split(" ")[1]
    list1[i].append(a1)
    list1[i].append(a2)

for j in range(0,g):
    sum1=sum1+ int(list1[j][0])*list2[0] + int(list1[j][1])*list2[1]
    print("第"+str(j+1)+"組應收費用："+str(sum1))
    sum1=0
