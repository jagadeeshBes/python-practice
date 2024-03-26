a=[1,2,3,4,5]
b=a[0]
for i in range(1,len(a)):
    a[i-1]=a[i]
a[len(a)-1]=b
print(a)
