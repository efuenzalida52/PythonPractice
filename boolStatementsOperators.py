# Booleans, statements, and operators oh my!
# Practicing Booleans, comparision operators, if statements

###############
## Booleans  ##
###############

#A = True   # Booleans are there own data type do NOT put them in quotes or...  
#B = 'True' #it becomes a string data type!

#########################################
## Bools w/ comparision operators (c.)
#######################################
#print(2 > 3)  # return false, > is a comparision operator
#print(3 > 2)  # return true
#print(2 == 3) # return false, == is the equals c. operator
#print(3 == 3) # return true
#print(2 != 3) # return true, != is the not equal to c. operator

#print(4 >= 3) # return true, >= is the greater than or equal to c.operator
#print(3 >= 3)
#print(4 <= 3) # return false, <= is the less than or equal to  c. operator
#print(3 <= 3)

# There are six total comparision operators: >,<, ==, !=, >=, <=


##############################
## If & else if Statements  ##
##############################

#create/defining variables
num1 = 100
num2 = 500
bigmsg = '{} is bigger than {}!'.format(num1,num2)
smlmsg = '{} is smaller than {}!'.format(num1,num2)
equal = '{} and {} are equal!'.format(num1,num2)

if num1 > num2:                       #if the statement is true print it works
    print(bigmsg)
elif num2 > num1:
    print(smlmsg)
else:
    print(equal)

# if (condition):
#   execute this code thing
# elif (condition):
#   execute this code
# else:
#   do this thing
    


    




