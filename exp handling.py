try:
    file=open('exceptions.txt')
    str=file.readline()
    print(str)
except IOError:
    print("<----Error occured due to input--->")
except ValueError:
    print("<---couldnot convert into intger--->")
except:
    print("<---Uexpetd Error--->")