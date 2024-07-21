# cau a
a= int (input("nhập số nguyên dương a:  "))
sum=0
while a<=0:
    a= int (input("nhập số nguyên dương a:  "));
while a %10 !=0 :
    sum+= a%10 
    a //=10;
print(sum)
#cau b
n= int (input("nhập số nguyên dương n:  "))
while n<=0:
    a= int (input("nhập số nguyên dương n:  "));
sum1=0;
for i in range (1,int(n)+1):
    if n%i==0 :
        sum1 +=i;
print(sum1)
# cau c
x= int (input("nhập số nguyên dương x:  "))
while x<=0:
    x= int (input("nhập số nguyên dương x:  "));
y= int (input("nhập số nguyên dương y:  "))
while y<=0:
    y= int (input("nhập số nguyên dương y:  "));
z= int (input("nhập số nguyên dương z:  "))
while z<=0:
    z= int (input("nhập số nguyên dương z:  "));
if x+y>z and x+z>y and y+z>x:
    if x==y==z:
        print("xyz tao thanh tam giac deu  ");
    elif x == y != z or x==z!=y or y==z!=x:
        print("xyz tao thanh tam giac can  ");
    elif x*x==y*y+z*z or y*y==x*x+z*z or z*z==x*x+y*y:
        print("xyz tao thanh tam giac vuong  ");
    elif x*x<y*y+z*z or y*y<x*x+z*z or z*z<x*x+y*y:
        print("xyz tao thanh tam giac nhon  ");
    elif x*x>y*y+z*z or y*y>x*x+z*z or z*z>x*x+y*y:
        print("xyz tao thanh tam giac tu  ");
else :
    print("xyz khong tao thanh tam giac   ");

