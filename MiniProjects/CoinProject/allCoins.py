#All the coins
import random

class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.heads = heads
        self.is_rare = rare
        self.is_clean = clean

        if self.is_rare:
            self.value = self.original_value*1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

#rust method: changes coins color upon rust.
    def rust(self):
       self.color = self.rusty_color

#clean method: changes coin color back to default color
    def clean(self):
        self.color = self.clean_color

    def __del__(self): #deconstructor
        print("Coin Spent!") #print when coin is destroyed

#flip a coin  
    def flip(self):
        heads_options =[True, False]
        choice = random.choice(heads_options)
        self.heads = choice



class DollarCoin(Coin):
    def __init__(self):
        data= {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
            }
        super().__init__(**data)#super = parent class

        

