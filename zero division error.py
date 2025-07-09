'''sytax=

try:
    stmts
    stmt
except ExceptioName:
'''
# program to handle zero division error
nume=int(input("Enter the numerator:"))
deno=int(input("Enter the denominator:"))
try:
    quo=nume/deno
    print("Quotient:",quo)
except ZeroDivisionError:
    print("<----------Denominaor cannot bo zero---------->")
