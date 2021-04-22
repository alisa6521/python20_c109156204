x=int(input("X軸座標："))
y=int(input("Y軸座標："))
d=0
if x == 0 :
    if y == 0:
        print("該點位於原點")
    elif y > 0:
        d=y**2
        print("該點位於上半平面Y軸上，離原點距離為根號",d)
    else:
        d=y**2
        print("該點位於下半平面Y軸上，離原點距離為根號",d)
elif x > 0:
    if y == 0:
        d=x**2
        print("該點位於右半平面X軸上，離原點距離為根號",d)
    elif y > 0:
        d=x**2 + y**2
        print("該點位於第一象限，離原點距離為根號",d)
    else:
        d=x**2 + y**2
        print("該點位於第四象限，離原點距離為根號",d)
elif x < 0:
    if y == 0:
        d=x**2
        print("該點位於左半平面X軸上，離原點距離為根號",d)
    elif y > 0:
        d=x**2 + y**2
        print("該點位於第二象限，離原點距離為根號",d)
    else:
        d=x**2 + y**2
        print("該點位於第三象限，離原點距離為根號",d)