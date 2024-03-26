def compretion(pre):
    s=""
    count=1
    for i in range(1,len(pre)):
        if(a[i]==a[i-1]):
            count+=1
        else:
            s+=a[i-1]
            s+=str(count)
            count=1
        if(count<0):
            return s
a="aaabbccjac"
print(compretion(a))