sub=["國文","英文","微積分","體育","程式設計"]
score=[]
b=[]
sum1=0
for i in range(0,5):
    a=int(input(sub[i]+"："))
    sum1=sum1+a
    score.append(a)
    b.append(a)
score.sort(reverse=True) #reverse=True由大排到小，默認是小排到大

avg=float(sum1/5)
max0=score[0] #抓最高
max1=int(b.index(max0))
min0=score[-1] #最低
min1=int(b.index(min0))

print("平均分數：%2.2f"%avg)
print("最高分科目："+str(sub[max1])+str(max0)+"分")
print("最低分科目："+str(sub[min1])+str(min0)+"分")