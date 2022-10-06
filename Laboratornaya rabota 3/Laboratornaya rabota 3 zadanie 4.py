n=int(input("Введите натуральное число:"))
var_1=str()
i=1
var_2=str()
var_3=str()
while i<=n:
    if i==1:
        var_1=var_1 + str(i)
        var_3=" " * (n-i) + var_1 + " " * (n-i)
        i=i+1
        print(var_3)
    else:
        var_1=var_1 + str(i)
        var_2=str(i-1)+var_2
        var_3=" " * (n-i) + var_1 + var_2 + " " * (n-i)
        i=i+1
        print(var_3)