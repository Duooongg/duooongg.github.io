#cau a
n= int (input("nhập số nguyên dương n:  "))
sum=0
while n<0:
    n= int (input("nhập số nguyên dương n:  "));
for i in range(1,2*n+2):
    if i%2 !=0:
        sum +=i;
    else :
        sum -=i;
print(sum)
#cau b
sum1=0
for i in range(1,n+1):
    sum1 += 1/i;
print(sum1)
#cau c
a = float(input("nhap he so x2  "))
b = float(input("nhap he so x  "))
c = float(input("nhap he so tu do  "))
if a==0:
    if b==0:
        if c==0: 
            print("phuong trinh co vo so nghiem  ");
        else: print("phuong trinh vo nghiem  ");
    else: 
        x=-b/c
        print(" phuong trinh co 1 nghiem " )
        print(x);
else:
    delta= b*b-4*a*c
    if delta<0:
        print("phuong trinh vo nghiem")
    elif delta==0:
        x= -b/(2*a)
        print("phuong trinh co nghiem kep ", x)
    else:
        x1=(-b+ delta**0.5)/(2*a)
        x2=(-b- delta**0.5)/(2*a)
        print("phuong trinh co 2 nghiem phan biet ",x1,x2)
    
