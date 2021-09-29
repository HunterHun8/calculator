x =[]
Smax=0
n = int(input())
for i in range(n):
    x.append(int(input()))
for g in range (len(x)):
    if x[g]<0:
        print("Длина должна быть положительной!")
        break
for i in range(len(x)):
    for j in range(i+1, len(x)):
        for k in range(j+1, len(x)):
            a=x[i]
            b=x[j]
            c=x[k]
            if a+b>c and a+c>b and c+b>a:
                p=(a+b+c)/2
                S=(p*(p-a)*(p-b)*(p-c))**0.5
                if S>Smax:
                    Smax=S
print(Smax)

