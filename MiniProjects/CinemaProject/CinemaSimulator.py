################################
## Cinema Simulator
################################
#range of films, pick film, check age,seats available

movies = {"Finding Dory":[3,5], #age (3), seats available (5)
          "Bourne":[18,5],
          "Harry Potter":[13,5],
          "Ghost Busters":[10,5]
         }
print(movies)
print()
while True:
    choice = input('What film would you linke to watch?: ').strip().title()

    if choice in movies:
        age = int(input("How old are you?: ").strip())
        if age >= movies[choice][0]: #check age
            num_seats = movies[choice][1]
            if num_seats > 0:  #check enough seats
                movies[choice][1]= movies[choice][1]- 1
                print('enjoy the film')
            else:
                print('Sorry no seats left!')
        else:
            print('you are not old enough to see this movie.')
    else:
        print('film not available.')
        
