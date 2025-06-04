factorial = lambda x: 1 if x == 0 else  x * factorial(x - 1)
number = int(input("Enter a number: "))
print(f"The fcatorial of {number} is {factorial(number)}")
