#handlig multiple exceptions
try:
    num=int(input("Enter a number::"))
    print(num**3)
except (KeyboardInterrupt):
    print("You should have entered a data without interrupting the compiler::")
except (ValueError):
    print("Enter numer only::")
print("program terminated")
print("BYE")