n=int(input("Введите натуральное число:"))
var_1=str()
i=1
var_2=str()
var_3=str()
b=str()
c=int()
for a in range(1,n+1):
    b=b+str(a)
c=len(b)
while i<=n:
    c=c-len(str(i))
    if i==1:
        var_1=var_1 + str(i)
        var_3=" " * (c) + var_1
        i=i+1
        print(var_3)
    else:
        var_1=var_1 + str(i)
        var_2=str(i-1)+var_2
        var_3=" " * (c) + var_1 + var_2
        i=i+1
        print(var_3)