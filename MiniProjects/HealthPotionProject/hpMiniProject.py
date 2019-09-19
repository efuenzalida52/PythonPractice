#####################################
## Mini Project: Health potion     ##
##                                 ##
## Description: Create a character ##
## who has 'x' amount of health.   ##
## this character recieves/ drinks ##
## a health potion that increases  ##
## thier health by a random amount ##
#####################################

#imports
import random #so I don't have to create a random number from scratch
              #I am importing a library/module to help 

#defining variables
health = 50 #creating base amount of health character has
potion_health = random.randint(25,50) #gives potion a random value between 25 & 50
difficulty = 1 #sets diffcultly, which will effect how uch health they recieve
               # from a potion. (1= easy, 2= medium, 3 = hard)

health = health + potion_health #re-assigning variable to equal
                                #current health value + potion value

#print(health) #checking how code has changed

#print(potion_health) #inital check

potion_health = potion_health/difficulty #re-assigning variable

#print(potion_health) #post inital check

potion_health = int(random.randint(25,50)/difficulty) #re-assigning variable

print(potion_health)
