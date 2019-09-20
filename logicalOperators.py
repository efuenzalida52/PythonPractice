#Practice with logical operators
#logical operators can be used in if statements

not True      # is False
not False     # is True

not 2 < 3     # statement is true- not true = false
not 3 > 1     # statement is true- not true = false
not 4 == 3    # statement is false- not false = true

x = 10
y = 20

if not y < x:
    print('it works!')

################
# AND operator #
################

A = 10
B = 5

if A >= 10 and B > 1:
    print('it worked')

#####
# not & and
#####
if not (A > 10 and B > 1):    #False & False + not = true
    print('it worked')

###############
# OR operator #
###############
#declare vars
C = 5
D = 1
if C > 1 or D > 1:         #if one or more of conditions are true it passes
    print('yay it works!')
# re-assign var 
D = 5
if C > 1 or D > 1:
    print('yay! it worked!')

if not (C > 100 or D > 100):
    print('this also works')


#declare/re-assign vars
C = 6
D = 2

# if one or more set or statements is true, print the thing
if(C > 5 and D > 5)or (C > 1 and D > 1):
    print('one or more statements was true!')
    
#nothing should happen due to not condition
if not ((C > 5 and D > 5)or (C > 1 and D > 1)):
    print('one or more statements was true!') 
