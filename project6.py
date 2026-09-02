def sieve(num):
    prime=[True for i in range(num+1)]
    p=2
    while ((p*p)<=num):
        if(prime[p]==True):
            for i in range(p*p,num+1,p):
                prime[i]=False
        p=p+1
    for p in range(2,num+1):
        if prime[p]:
            if p > 10:
                print(p)
num=100
sieve(num)