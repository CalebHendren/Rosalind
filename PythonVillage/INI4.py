a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
total = 0

for number in range(a, b + 1):
    if number % 2 != 0:
        total = total + number
print("The sum of odd numbers is:", total)