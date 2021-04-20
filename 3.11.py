t=float(input("lai suat tiet kiem la:"))
n=int(input("nhap so von ban dau:"))
k=int(input("nhap so thang gui:"))


def benefit(t,n,k):
    tienlai=n*(t/100)*k
    print("so tien lai la:",tienlai)
    tong=n+tienlai
    print("tong so tien lai la:",tong)
benefit(t,n,k)

