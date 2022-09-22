def func(a,b,c):
    if (a>=b) and (a>=c):
        print("Наибольшее число =", a)
a=int(input("Число a равно:"))
b=int(input("Число b равно:"))
c=int(input("Число c равно:"))
if (a==b) and (a==c):
    print("Числа равны")
else:
    func(a,b,c)
    func(b,a,c)
    func(c,b,a)
