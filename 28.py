ans=input()
suma=0
sumb=0
test=input()
while test != "0000":    
    for i in range(0,4):
        for j in range(0,4):
            if test[i]==ans[j]:
                if i==j:
                    suma=suma+1            
                else:                   
                    sumb=sumb+1
    
    print("%1dA%1dB"%(suma,sumb))
    suma=0
    sumb=0    
    test=input()       