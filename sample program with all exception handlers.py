'''write a program that prompts the user to enter a number and print its square 
perform exceptional handling for KeyboardInterrupt'''
try:
    n=int(input("enter a number:"))
    s=n*n
    print(s)
    
except KeyboardInterrupt:
    print("program has been intrrupted")