##ncr
n=5
r=3

def fact(n):
    prod = 1
    for i in range(1, n + 1):
        prod = prod * i
    fact = prod
    print(fact)
    return fact
print(f"factorial of 5 is {fact(5)}")
ncr=fact(n)/(fact(n-r)*fact(r))
print(f"ncr={ncr}")








#prod=1
#for i in range(1,n+1):
 #   prod=prod*i
#print(prod)

#prod=1
#for i in range(1,r+1):
 #   prod=prod*i
#print(rfact)
