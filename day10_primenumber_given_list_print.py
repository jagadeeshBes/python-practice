a=[1,2,3,4,5,6,7,8]
b=[] 
for i in a:
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        b.append(i)
print(b)

        