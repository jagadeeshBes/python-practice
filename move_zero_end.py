a=[0,10,3,0,11,23]
b=[]
c=[]
for i in a:
    if(i != 0):
        b=b+[i]
    elif(i==0):
        c=c+[i]
d=b+c
print(d)