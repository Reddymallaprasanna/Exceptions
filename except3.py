try:
    file=open('exceptions.txt')
    str=file.readline()
    print(str)
except IOError:
    print("<----Error occured due to input--->")
else:
    print("program exected successfully!")