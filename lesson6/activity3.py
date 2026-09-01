def iloveyou(num):
    prime=[True for i in range(num+1)]
    p=2
    while ((p*p)<=num):
        if(prime[p]==True):
            for i in range(p*p,num+1,p):
                prime[i]=False
        p=p+1
    for p in range(2,num+1):
        if prime[p]:
            print("LoveYou",p)
num=int(input("Enter the number: "))
iloveyou(num)