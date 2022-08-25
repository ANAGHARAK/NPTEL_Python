def transpose(m):
    ans=list()
    for i in range(len(m[0])):
        a=[]
        for j in range(len(m)):
            a.append(m[j][i])
        ans.append(a)
    return(ans)
list1=[[1,2,3,4],[5,6,7,8]]
print(list1)   
print(transpose(list1))