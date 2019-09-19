###################################################################
## This file is a refesher of some basic functionaitly in python ##
###################################################################

#Arithmetic ,Float refresher
print(2+3) #should return five
print(100-50) #should return fifty
print(100+20-80) #return 40
print(7*7)#return 49
print(2/4)# should return 0.5 - this is a float/decimal
print(10/5) #return 2.0

#########
#Modulo: find the remainder of division
#########
5 % 3 # modulo operator is % sign

# above should return 2 because 3 goes into 5 once and has a remainder of 2.

#######################################
## Order of operations:              ##
## Mathmatical operations use BODMAS ##
## order system.                     ##
## The closer to 'B' the higher the  ##
## priority.                         ##
## B - brackets ()                   ##
## O - order [squaring, cubing,etc]  ##
## D - division                      ##
## M - multiplication                ##
## A - addition                      ##
## S - subtration                    ##
#######################################

print(2 * 5 -1) # would return 9 instead of expected 8
print(2 * (5-1)) # returns 8
