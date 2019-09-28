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

    def rust(self):                     #rust method: changes coins color upon rust.
       self.color = self.rusty_color

    def clean(self):                #clean method: changes coin color back to default color
        self.color = self.clean_color

    def __del__(self): #deconstructor
        print("Coin Spent!") #print when coin is destroyed
  
    def flip(self):
        heads_options =[True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value > 1.00:
            return "${} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value*100))

class Penny(Coin):
    def __init__(self):
        data= {
            "original_value": 0.01,
            "clean_color": "bronze",
            "rusty_color": "blue-greenish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
            }
        super().__init__(**data)#super = parent class


class Nickel(Coin):
    def __init__(self):
        data= {
            "original_value": 0.05,
            "clean_color": "nickle",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
            }
        super().__init__(**data)


class Dime(Coin):
    def __init__(self):
        data= {
            "original_value": 0.10,
            "clean_color": "tin",
            "rusty_color": None, #as an example of ploymorphisim we are going to pretend dime doesn't rust
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
            }
        super().__init__(**data)
        
    def rust(self): #polymorphisim example in the works
        self.color = self.clean_color
    def clean(self):
        self.color= self.clean_color #this is not nesscarry since it's being inherited        

class Quarter(Coin):
    def __init__(self):
        data= {
            "original_value": 0.25,
            "clean_color": "silver",
            "rusty_color": "brownish",
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5.00
            }
        super().__init__(**data)

class Half_Dollar(Coin):
    def __init__(self):
        data= {
            "original_value": 0.50,
            "clean_color": "silver",
            "rusty_color": "blue",
            "num_edges": 9 ,
            "diameter": 24.5,
            "thickness": 1.78,
            "mass": 8.00
            }
        super().__init__(**data)

#made up coin 
class Third_Dollar(Coin):
    def __init__(self):
        data= {
            "original_value": 0.75,
            "clean_color": "platinum",
            "rusty_color": "red-brown",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
            }
        super().__init__(**data)

class Dollar_Coin(Coin):
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

#madeupcoin
class Two_Dollar(Coin):
    def __init__(self):
        data= {
            "original_value": 2.00,
            "clean_color": "turquoise",
            "rusty_color": "rose pink",
            "num_edges": 1,
            "diameter": 28.4,
            "thickness": 2.50,
            "mass": 12.00 #mm
            }
        super().__init__(**data)#super = parent class

#List of class functions I just created
coins = [Penny(), Nickel(), Dime(), Quarter(), Half_Dollar(),
         Third_Dollar(), Dollar_Coin(),Two_Dollar()]

#loop through the list I just made and pull this data I am specifying
for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter,
                 coin.thickness, coin.num_edges, coin.mass]

string =("{}- Color: {}, value: {}, diameter(mm): {}, "
        "thickness(mm): {}, number of edges: {}, mass(g): {}".format(*arguments))
print(string)
