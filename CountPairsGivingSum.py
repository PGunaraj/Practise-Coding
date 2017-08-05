
def countPairs(l,sum):
    dict={}
    count=0
    li = [x for x in l if x != 0]
    i=0
    while i < len(li):
        if li[i] in dict.values():
            count=count+1
            i=i+1
        else:
            dict[i]=sum-li[i]
            i=i+1
    return count


l=[-1,7,-2,8,5,1]
sum=6
x=countPairs(l,sum)
print(x)