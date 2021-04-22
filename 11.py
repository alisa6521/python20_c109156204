in1=input("請輸入月和日：")
a0=int(in1.split(" ")[0])
a1=int(in1.split(" ")[1])
list1=[[1,21,"Aquarius","Capricorn"],[2,19,"Pisces","Aquarius"],[3,21,"Aries","Pisces"],[4,21,"Taurus","Aries"],[5,22,"Gemini","Taurus"],[6,22,"Cancer","Gemini"],[7,23,"Leo","Cancer"],[8,24,"Virgo","Leo"],[9,24,"Libra","Virgo"],[10,24,"Scorpio","Libra"],[11,23,"Sagittarius","Scorpio"],[12,22,"Capricorn","Sagittarius"]]

for i in range(0,12):
    if a0==list1[i][0]:
        if a1 >=list1[i][1]:
            print("星座為：",list1[i][2])
        else:
            print("星座為：",list1[i][3])
