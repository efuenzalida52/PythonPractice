##############################################################
#MiniProject: The silly security system                  #####
##############################################################
#Computer will ask if user is on the list of known users.   ##
#if user is it will welcome user and                        ##
#ask user if they would like to be removed                  ##
#from the list. If the user if not recognized computer      ##
#will ask if they would like to be added to list.           ##
##############################################################

#Define Variable(s)
known_users = ['Collin','Joel',
               'Abi','Elizabeth',
               'Brian','Lucy',
               'Anakin','Ronan']

while True :
    print('Hello I am Bouncer Bot.')
    name = input('What is your name so I can see if you are on the list? :').strip().capitalize()
    helloMsg_T =('Hello {}, I see your name here!').format(name)
    helloMsg_F =('Hello {}, your name is not here.').format(name)
    
    if name in known_users:
        print(helloMsg_T) #could also do print('Hello {}'.format(name))
        remove = input('would you like to be removed from the list (y/n)?: ').strip().lower()

        if remove == 'y' or remove == 'yes':
            known_users.remove(name)
            print(known_users)
            print()
            
        elif remove == 'n' or remove == 'no':
            print('okay, you have not been removed.')


    else:
        print(helloMsg_F)
        print('{}, you are not on the list.'.format(name))
        add = input('Would you like to be added to the list (y/n)?:'.strip().lower())

        if add == 'yes' or 'y':
            known_users.append(name) #puts entered at end of list
            print(known_users)
            
        elif add == 'n' or add == 'no':
             print('okay, you have not been added.')

        print(known_users)

