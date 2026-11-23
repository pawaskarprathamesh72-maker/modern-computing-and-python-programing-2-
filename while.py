n=int(input("enter the number:"))
psum=nsum=z_count=0
while(n!=-1):
    if(n>0):
        psum+=n
    elif(n<0):
        nsum+=n
    else:
        z_count+=1
    n=int(input("enter the number:"))
print(f"sum of positive number:{psum}")
print(f"sum of negative number:{nsum}")
print(f"number of zero:{z_count}")