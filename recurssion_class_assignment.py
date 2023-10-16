a = [1,3,5,6,7,10]

def summation(lst):
    if len(lst) == 1:
        return lst[0]
    n = lst.pop()
    return n + summation(lst)

print(summation(a))


def pow(x,y):
    if y == 0:
        return 1
    return x * pow(x,y-1)

print(pow(2,3))