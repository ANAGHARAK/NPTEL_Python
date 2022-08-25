def min3(x,y,z):
  if x <= y:
    if x <= z:
      minimum = x
  if y<=x:
    if y<=z:
      minimum = y
  if z<=x:
    if z<=y:
      minimum = z  
  return(minimum)

print(min3(89,2,90))