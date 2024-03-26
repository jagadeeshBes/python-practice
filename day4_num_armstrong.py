a=int(input("enter"))
c=0
while(a>0):
    f=a%10
    c=c+(f*f*f)
    a=a//10
print(c)
    