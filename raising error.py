try:
    n=100
    print(n**2)
    raise ValueError
except :
    print("Exeption ocurred")