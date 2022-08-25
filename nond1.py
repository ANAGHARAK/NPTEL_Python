def repeated(l):
    x=0
    new=[]
    for i in range(len(l)):
        if l.count(l[i])>1 and l[i] not in new:
            x=x+1
            new.append(l[i])
        i=i+1
    return(x)  
print(repeated(["the","higher","you","climb","the","further","you","fall"]))    