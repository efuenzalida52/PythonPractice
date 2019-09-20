# Project: Hello!                                                                 #
# Description: Create a program that asks user for inputs and outputs their input #
###################################################################################


#Ask user for name                    
name = input('What is your name? : ') #saves user input to variable 
#print(name)                           #outputs saved user input check

#Ask user for age
age = input('How old are you? : ') #saves user input to variable
print(age)                         #outputs saved user input check
print(type(age))                   # NOTE: input always saves as string

#Ask user for city
city = input('what city do you live in? : ')#saves user input to variable
#print(city)                                 #outputs saved user input check

#Ask user what they enjoy
enjoy = input('what do you enjoy doing? : ') #saves user input to variable

#Ask user for adjective
adj = input('give me an adjective: ')#saves user input to variable

#Create output text
#NOTE places numbered place holders in {} assigns that index number.
#however you have to do auto or manual, cannot do both in one!
string= "Hello {}! You are {} years old and live in {}. You enjoy {}; that's {}!"
output= string.format(name,age,city,enjoy,adj)

#print output to screen
print(output)
