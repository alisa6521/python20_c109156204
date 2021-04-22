a=input("檢測的字串（end結束）：")
if a == "end":
    print("檢測結束")
else:
    b=input("檢測的單一字元：")
    c=a.count(b)
    print("字元"+b+"出現次數為："+str(c))
