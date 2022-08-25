def sumsquare(l):
    odd_sum=0
    even_sum=0
    for a in l:
        if a%2!=0:
            odd_sum+=(a*a)
        else:
            even_sum+=(a*a)
    return([odd_sum,even_sum])  
list1=[1,3,6,8] 
print(sumsquare(list1))
             