a=int(input("輸入一正整數："))
if a %2 ==0 and a % 11 == 0 and a % 5 != 0 and a % 7 != 7:
    print("%d為新公倍數？YES"%a)
else:
    print("%d為新公倍數？NO"%a)