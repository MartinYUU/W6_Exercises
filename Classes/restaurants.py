# 1. Create a new script named restaurants.py. In it, make a class called Restaurant. 
# The __init__() method for Restaurant should store two instance variables: 
# rest_name and food_type. Be sure to include a docstring below the class name to 
# describe the purpose of the class. 
# 2. Add two methods to the class: 
# ∗ The first method should be named describe_rest() and prints the output: 
# [Restaurant name] serves [type of food]. 
# ∗ The second method should be named rest_open() and prints a simple message: 
# [Restaurant name] is open. 
# 3. Create three instances of the class for different types of restaurant. You can use the 
# below examples or create your own:

# 4. Finally, call describe_rest() and rest_open() for each instance.

class Restaurant:
    '''Variety of restaurants'''
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type        

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')

    def rest_open(self):
        print(f'{self.rest_name} is open!')

rest1 = Restaurant("McDonald's", 'Burgers')
rest2 = Restaurant('El Meson', 'Tacos')
rest3 = Restaurant('Taco Bell', "'Tacos'")

rest1.describe_rest()
rest2.describe_rest()
rest3.describe_rest()

rest1.rest_open()
rest2.rest_open()
rest3.rest_open()