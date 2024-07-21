f0=0
f1=1
n= int (input("nhập số nguyên dương n:  "))
while n<=0:
    n= int (input("nhập số nguyên dương n:  "));
if n==1: 
    print(f0);
elif n==2: 
    print(f0,f1);
else:
    print(f0,f1)
    for i in range(1,n-1):
        f2=f1+f0
        f0=f1
        f1=f2
        print(f2)
