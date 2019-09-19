# testing out a simple python command.
# This will print 7*7 in the shell when ran.
print(7*7)
# after the first line above is ran it will print the following 'Hello'
print('Hello')
print() #creating a line breaks
print()

###############################
## Using variables in python ##
###############################
number = 7 #creating variables
string = 'Hello World!'

print(number)
print(type(number)) #type() tells you what data type the parameter is
print()
print()
print((string) + ' is a ...')
print(type(string))
#python is dynamically typed language which means you can overwrite
#previously defined variables with a completely different data type.
string = 77
print ('now the variable string is a...')
print (type(string))
