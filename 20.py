inf=[["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
num=input("輸入查詢學號為：")
for i in range(0,6):
    if num==inf[i][0]:
        print("學生資料為："+str(inf[i][0]),str(inf[i][1]),str(inf[i][2]))
        break
    else:
        continue