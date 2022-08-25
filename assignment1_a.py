list1=[2,3,3]
def remdup(l):
    i=0
    lcount=l.count(l[i])
    while i<len(l):
        if lcount>1:
            l.remove(l[i])
        i=i+1       
print(remdup(list1))       