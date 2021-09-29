a=input()
while insinstance(a,str):
    print("Коэффицент должен быть числом")
    break
b=input()
while insinstance(b,str):
    print("Коэффицент должен быть числом")
    break
c=input()
while insinstance(c,str):
    print("Коэффицент должен быть числом")
    break
D = b*b-4*a*c
if D>0:
    x1=(-b+D**0.5)/2*a
    x2=(-b-D**0.5)/2*a
    print(x1,' ',x2)
elif D==0:
    x=(-b)/2*a
    print(x)
else:
    print("Нет корней!")



