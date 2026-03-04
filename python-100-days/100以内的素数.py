from operator import truediv
num=0
for n in range(2,101):
    bool_prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            bool_prime=False
            break
    if bool_prime:
        print(n)
        num+=1
print(num)