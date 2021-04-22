a=int(input("輸入一個度數（正整數）："))
pay1,pay2=0,0
if a >= 121 :
    pay1=pay1+ (120*2.1)
    pay2=pay2+ (120*2.1)
    if a >= 331 :
        pay1=pay1+(210*3.02)
        pay2=pay2+(210*2.68)
        if a >=501:
            pay1=pay1+(170*4.39)
            pay2=pay2+(170*3.61)
            if a>=701:
                pay1=pay1+(200*4.97)+ (a-700)*5.63
                pay2=pay2+(200*4.01)+ (a-700)*4.5
            else:
                pay1=pay1+((a-500)*4.97)
                pay2=pay2+((a-500)*4.01)
        else:
            pay1=pay1+((a-330)*4.39)
            pay2=pay2+((a-330)*3.61)
    else:
        pay1=pay1+ ((a-120)*3.02)
        pay2=pay2+ ((a-120)*2.68)
else:
    pay1=a*2.1
    pay2=a*2.1

if a <=0:
    print("不用繳納")
else:
    print("Summer months：%4.2f"%(pay1))
    print("Non-Summer months：%4.2f"%(pay2))

