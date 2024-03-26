a="aabbbcccc"
b=list(a)
s=""
count1=count2=count3=0
for i in b:
    if(i=="a"):
        count1+=1
        e=i+str(count1)
    elif(i=="b"):
        count2+=1
        f=i+str(count2)
    elif(i=="c"):
        count3+=1
        g=i+str(count3)
s=e+f+g+s
print(s)
    
