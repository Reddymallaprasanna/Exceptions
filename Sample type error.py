'''program having finally block to re-raise an exception that will be handled by an outer try-except block'''
try:
    print("DIVIDING TWO STRINGS.....")
    try:
        quo="abc"/"def"
        print(quo)
    finally:
        print("THIS IS THE FINALLY BLOCK WHICH WILL BE EXECUTED EVERY TIME..")
except TypeError:
    print("HERE THE TYPE ERROR WHICH IS RAISED IN INNER FINALLY WILL EXECUTED------")