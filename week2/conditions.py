try:
    x = int(input("number: "))
except ValueError:
    print("Error: sathvi fail!")
else:
    if x > 0:
        print("x is positive")
    elif x < 0:
        print("x is negative")
    else:
        print("x is 0")
