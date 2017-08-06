def nestedList():
    l = []
    for _ in range(int(input())):
        l.append([input(), float(input())])
    i = 0
    secminlist = []
    min = secmin = float('inf')
    while i < len(l):
        if l[i][1] < min:
            secmin, min = min, l[i][1]
        elif l[i][1] < secmin:
            secmin = l[i][1]
        i = i + 1
    i = 0
    while i < len(l):
        if l[i][1] == secmin:
            secminlist.append(l[i][0])
        i = i + 1
    secminlist.sort()
    for name in secminlist:
        print(name)

nestedList()

'''
user input: use string within " "
5
"Harry"
37.21
"Berry"
37.21
"Tina"
37.2
"Akriti"
41
"Harsh"
39
'''