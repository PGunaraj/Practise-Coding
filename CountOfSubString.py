#method 1: brute force (character by character comparision)
def count_substring(string, sub_string):
    l=len(sub_string)
    i=0
    count=0
    for ch in range(0,len(string)):
        j=ch
        while i<l and j<len(string) and string[j]==sub_string[i]:
            if i==l-1:
                count=count+1
                i=-1
            else:
                j=j+1
                i=i+1
        i=0
    return count

#method 2: using string comparision
def count_substring2(string, sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1): #check all possible pairs of string equal to length of sub string
        if string[i:i+len(sub_string)]==sub_string: #string comparision
            count+=1
    return count

print(count_substring("ABCDCDC","CDC"))
print(count_substring2("ABCDCDC","CDC"))