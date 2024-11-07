#  Create a copy of your restaurants.py script and rename it food_truck.py. At the bottom 
# of the script following the Restaurant class creation and object initialization, define a 
# new child class named FoodTruck. Remember to include the name of the parent 
# class in parentheses in the class definition, and include a docstring to describe the 
# child class. 
# 2. Define the __init__() method to take in the information required in the parent 
# Restaurant class, and use the super() function to call the .__init__ method from the 
# parent class. 
# 3. Add two new attributes to the __init__() method specific to the child class: 
# ∗ self.private_bookings with a default value of ‘N’ 
# ∗ self.truck_location with a default value of an empty string 
# 4. Add a method called accepts_private_bookings() that prompts for an input 
# with “Does this food truck accept private bookings? Y/N ” and updates the value of 
# self.private_bookings. Then print the appropriate message: “This food truck currently 
# accepts [or does not accept] private bookings.” 
# 5. Add a method called relocate_truck() that prompts the user to enter the truck’s current 
# location (street address and city). Print the output, “Truck is currently located at 
# [address, city]”

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

class FoodTruck(Restaurant):
    '''Child class of Restaurant'''
    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)
        self.private_bookings = 'N'
        self.truck_location = ''
    
    def  accepts_private_bookings(self):
        pb = input('Does this food truck accept private bookings? (Y/N): ')
        if pb.upper() == 'Y':
            self.private_bookings = 'Y'
            print('This food truck currently accepts private bookings.')
        elif pb.upper() == 'N':
            print('This food truck currently  does not accept private bookings.')
        else:
            print('Invalid entry try again.')

    def relocate_truck(self):
        location = input('What is the current loaction of the food truck?(street address and city): ')
        self.truck_location = location
        print(f'Truck is currently located at {self.truck_location}')

truck1 = FoodTruck('I Scream Sundae', 'Ice cream')

truck1.accepts_private_bookings()
truck1.relocate_truck()