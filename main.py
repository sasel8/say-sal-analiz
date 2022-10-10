import math

n = int (input("son değer girin"))
x = math.pi/5
p=1
s=1
f=1
sine=1
for i in range (n,n+1,20):
    sine=sine*-1
    p=pow(x,i)
    f=f*i*(i-1)
    s=s+sine*p/f
gercek=math.cos(x)
kesme=gercek-s
print(f"Yaklasik Deger: {s}")
print(f"Gercek deger {gercek}")
print(f"kesme hatası: {kesme}")