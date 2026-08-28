num = int(input("Enter a number to check if it is a palindrome: "))
temp=num
rev=0
while temp > 0:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp //= 10
if num == rev:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")