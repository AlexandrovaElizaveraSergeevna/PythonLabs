l = [7, 2, 9, 3, 6, 1, 5, 0, 4, 6]
def func(l):
    b=[]
    for i in range(0, len(l), 2):
        b.append(l[i])
    print(b)
func(l)
