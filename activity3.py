def is_power4(n):
    if n == 1:
        return True
    if n % 4 != 0:
        return False
    else:
        return is_power4(n//4)

input("is_power4 divides by 4 - n==1 returns True  remainder returns False. Press Enter")
print("  is_power4(16) = True")
print("  is_power4(12) = False")

n = int(input("Enter a number (try 60 or 48): "))
guess = input("What is is_power4(" + str(n) + ")? ")
input("is_power4 has two stops - n==1 is True  remainder or n<=0 is False. Press Enter")
print("  is_power4(" + str(n) + ") = " + str(is_power4(n)) + "  your guess: " + guess)