#trey finally block 
try:
    print("RAISING BEXCEPTION-->")
    raise ValueError
except:
    print("EXCEPTION CAUGHT-->")
finally:
    print("PERFORMING CLEAN-UP WITH FINALLY--->")