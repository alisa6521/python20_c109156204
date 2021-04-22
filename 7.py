import math
call=input("輸入月租型式及通話時間：")
a=float(call.split(",")[0])
b=float(call.split(",")[1])
c1=[186,386,586,986]
c2=[0.09,0.08,0.07,0.06]
c3=[0.9,0.8,0.7,0.6]
c4=[0.8,0.7,0.6,0.5]
for i in range(0,4):
    if a == c1[i]:
        pay=b*c2[i]
        if pay > c1[i] and (c1[i])*2 >= pay:
            pay=pay*c3[i]
        elif pay > (c1[i])*2:
            pay=pay*(c4[i])       
print("通話費為：",math.ceil(pay))