def factorial(n):
    if n == 1 or n == 0:
     return 1
    else:
        return n * factorial(n - 1)

while True:   
    try:        
        number = int(input("\nEnter a number:   "))
        print(f"{factorial(number)}")
    except Exception as e:
        print(e)
        print("Retry")
        
          