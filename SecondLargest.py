def secLargest(l):
    max = float('-inf')
    secmax = float('-inf')
    for i in l:
        if i > max:
            secmax = max
            max = i
        elif i > secmax and i != max:
            secmax = i
    return secmax

l=[1,2,3,4,5,6]
x=secLargest(l)
print(x)