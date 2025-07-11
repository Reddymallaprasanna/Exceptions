''' write a program that prints natural numbers rasie an exception after printing first 30 numbers'''
n=0
while True:
    try:
        n=n+1
        if n==31:
            raise StopIteration
    except StopIteration:
        
        break
    else:
        print(n,end="  ")