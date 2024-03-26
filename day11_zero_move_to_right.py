value=[1,0,2,0,0,1]
for i in range(len(value)):
    for j in range(1,len(value)):
        if(i>j):
            value[i],value[j]=value[j],value[i]
        elif(j>i):
             value[j],value[i]=value[i],value[j]
print(value)

