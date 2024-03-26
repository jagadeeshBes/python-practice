a='python'
split=list(a)
b=input("enter string")
replace=input("enter stripng")
for i in range(len(split)):
    if(b in split[i]):
        split[i]=replace
print(''.join(split))
    
