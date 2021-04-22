inf=[["123","456","9000"],["456","789","5000"],["789","888","6000"],["336","558","10000"],["775","666","12000"],["566","221","7000"]]
n=int(input("輸入查詢組數N為："))
list1=[]
for i in range(0,n):
    list1.append([])
    a=input()
    a1=a.split(" ")[0]
    a2=a.split(" ")[1]
    list1[i].append(a1)
    list1[i].append(a2)
    
print()

for j in range(0,n):
    for k in range(0,6):
        if list1[j][0]==inf[k][0] and list1[j][1]==inf[k][1]:
            print(inf[k][2])
            break
        else:
            if k!=5:
                continue
            else:
                print("error")  