a = [1,2,3,4,-5,6,-1,-9]
b=[]
c=[]
for i in a:
    if(0<i):
        b=[i]+b
      
    elif(0>i):
        c=[i]+c
     
print(b)
print(c)