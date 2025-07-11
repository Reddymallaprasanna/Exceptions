'''list comprehension
syntax:
[expresion for var in range() if condition]
'''
#1 4 9 16 .........100
print([n**2 for n in range(1,11)])
# list comprehension with condition
print([x for x in range(1,11) if x%2==0])
#another examples
words=['apple','banana','guava']
print([word.upper() for word in words])