while True:
    try:
        a = float(input("First Number:"))
        b = float(input("Second Number:"))
        print(f"{a} / {b} = {a/b}")
        break
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("The number should not be zero")

    
    



    