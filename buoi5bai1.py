dict={
    202361222:3.3,
    202362332:2.0,
    202361234:3.5,
    202343234:1.9
}
count=0
for i in dict:
    if dict[i]>=3.0 and dict[i]<=3.5:
        count+=1
print("so sinh vien co diem tongg ket trong doan [3.0,3.5] la:",count)
dict[2023567489] = 3.2
xoa=[]
for ma_sv,diem in dict.items():
    if diem < 2.0:
        xoa.append(ma_sv)
for ma_sv in xoa:
    dict.pop(ma_sv)
for ma_sv,diem in dict.items():
    print(ma_sv,diem)