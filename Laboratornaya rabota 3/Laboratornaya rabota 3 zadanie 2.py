var=list()
a=int(input("Сколько чисел вы хотите ввести? "))
i=0
while i<a:
    b=int(input("Заполните массив: "))
    var.append(b)
    i=i+1
print("Количество нулей =", var.count(0))