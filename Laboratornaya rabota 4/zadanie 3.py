l=[2, 7, 1, 6, 4, 8, 0, 5, 8, 9]
def func(l):
    max=l[0]
    min=l[0]
    for i in range(1, len(l)):
        if l[i]>l[i-1]:
            max=l[i]
        if l[i]<l[i-1]:
            min=l[i]
    l[l.index(max)]=min
    l[l.index(min)]=max
    print(l)
func(l)