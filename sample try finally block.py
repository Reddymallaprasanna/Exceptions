#try finally block 
try:
    print("RAISING AN EXCEPTION ---->")
    raise ValueError
finally:
    print("PERFORMMING CLEAN-UP WITH FINALLY---->")