anm=["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
year=int(input("輸入西元年："))
a=(year-4)%12
print(anm[a])