a=[1,2,3,4,5]
b=a[0]
c=a[1]
for i in range(3,len(a)-2):
    print(i)
    a[len(a)-2-3]=a[i]
    
a[len(a)-2]=b
a[len(a)-1]=c

print(a)