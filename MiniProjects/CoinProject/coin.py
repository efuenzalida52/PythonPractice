#Mini Project: Make a coin

import random
class DollarCoin:

#self = specific instance of this class
    def __init__(self, rare=False): #init = constructor
       self.rare = rare

       if self.rare:
           self.value= 1.25
       else:
           self.value = 1.00
        
       self.color = "gold"
       self.num_edges = 1
       self.diameter= 22.5 #mm
       self.thickness = 3.15 #mm
       self.heads= True

#rust method: changes coins color upon rust.
    def rust(self):
       self.color = 'greenish'

#clean method: changes coin color back to default color
    def clean(self):
        self.color = 'gold'
        
#flip a coin
        
    def flip(self):
        heads_options =[True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self): #deconstructor
        print("Coin Spent!") #print when coin is destroyed
