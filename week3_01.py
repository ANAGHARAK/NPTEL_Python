def remdup(l):
    L=[]
    for i in l:
        if i not in L:
            L.append(i)
    return(L)
list1=[2,3,3]
print(remdup(list1))   