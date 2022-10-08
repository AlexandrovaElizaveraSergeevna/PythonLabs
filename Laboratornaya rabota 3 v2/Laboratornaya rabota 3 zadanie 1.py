var=list()
i=0
c=0
while i<10:
    a=int(input("Заполните массив: "))
    var.append(a)
    i=i+1
for b in var:
    c=c+b
print("Сумма всех чисел =", c)