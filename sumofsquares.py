def sumofsquares(n):
    def square(x):
        v=x*x
        return(v)
    for i in range(1,n):
        for j in range(1,n):
            if square(j) + square(i)==n:
                return(True)
            else:
                j=j+1    
        i=i+1
    else:
        return(False)
print(sumofsquares(289))

    