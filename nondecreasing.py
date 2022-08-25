def nondecreasing(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    for i in range(len(l)):
        
        for j in range(i,len(l)):
            if l[j]<l[i]:
                return(False)
            else:
                j=j+1
        i=i+1
    else:
        return(True)

l=[2,4,1]           
print(nondecreasing(l))