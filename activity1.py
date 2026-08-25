num = int(input("Enter a number to check if its an Armstrong Number: "))

sum = 0
temp = num
total_digits=len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** total_digits
    temp //= 10

if sum == num:
    print(num, "is an Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")
