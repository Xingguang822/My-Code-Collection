
def gcd(a:int,b:int)->int:
    while b!=0:
        a,b=b,a%b
    return b

def lcm(a:int,b:int):
    return a*b//gcd(a,b)

x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
print("GCD of",x,"and",y,"is",gcd(x,y))
print("LCM of",x,"and",y,"is",lcm(x,y))