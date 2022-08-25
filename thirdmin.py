def thirdmin(l):
  (mymin,mysecondmin,mythirdmin) = (1000000,1000000,1000000)
  for i in range(len(l)):
      min=[]
      for j in range(len(l)):
        if l[j]<l[i]:
            min.append(l[i])
        j=j+1
      i=i+1
  (min[0],min[1],min[2])=(mymin,mysecondmin,mythirdmin)

  return(mythirdmin)
l=[465,90,986,906]
print(thirdmin(l))
