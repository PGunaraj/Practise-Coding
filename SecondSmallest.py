import sys;

def secondSmallest(li):
    if len(li)<2:
        return 0
    else:
        min=sys.maxint
        secmin=sys.maxint
    for i in li:
        if i<min:
            secmin=min
            min=i
        elif i<secmin and i!=min:
            secmin=i
    if secmin!=sys.maxint:
        return secmin
    else:
        return "No Second Minimum"

l=[1,1]
x=secondSmallest(l)
print(x)