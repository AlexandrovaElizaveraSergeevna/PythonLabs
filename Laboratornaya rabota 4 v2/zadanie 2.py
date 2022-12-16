l=[1, 7, 4, 2, 5, 8, 9, 6, 4, 3, 5, 9, 0]
def func(l):
    b=[]
    for i in range(1, len(l)):
        if l[i]>l[i-1]:
            b.append(l[i])
    print(b)
func(l)