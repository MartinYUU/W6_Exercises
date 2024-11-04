# 1. Create a copy of your restaurants.py script and rename it restaurants_enhanced.py. 
# 2. Add a default attribute to the __init__() method for self.number_served = 0 and 
# another default attribute for self.customer_ratings = []  
# 3. Add a method called add_num_served() that accepts an input for “How many 
# customers served today?” and adds that amount to the self.number_served attribute. 
# 4. Add a method called print_num_served() that prints the output: 
# [Restaurant name] has served [number] customers 
# 5. Add a method for customer_rating() that accepts an input of integers 1-5 for 
# “How would you rate your experience today on a scale of 1-5 (5 being excellent)?” Add 
# that number to the list of  self.customer_ratings, and print the statement “Your rating 
# was ___. The average rating for this restaurant is ___” (You can calculate the average 
# using the sum of the ratings list, divided by the list length.) 
# 6. Test your new methods: 
# ∗ For each of your example restaurants, run print_num_served() to check the initial 
# value. Then run add_num_served() a few times, inputting different values. Finally, 
# run print_num_served() again to check the updated balance. 
# ∗ For each of your example restaurants, run customer_rating() several times, 
# inputting a different rating each time. Confirm that the average rating updates 
# appropriately each time. 
# ∗ For customer_rating(), try inputting a few “incorrect” values, like the number 6, a 
# decimal number such as 2.5, and a word/phrase such as “5 stars!


class Restaurant:
    '''Variety of restaurants'''
    def __init__(self, rest_name, food_type,number_served = 0, customer_ratings = []):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = number_served
        self.customer_ratings = customer_ratings

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')

    def rest_open(self):
        print(f'{self.rest_name} is open!')

    def add_num_served(self):
        num_served = int(input('How many customers served today?: '))
        self.number_served += num_served

    def print_num_served(self):
        print(f'{self.rest_mame} has served {self.number_served} customers!')

    def customer_rating(self):
        rating = int(input('How would you rate your experience today on a scale of 1-5 (5 being excellent)?: '))
        self.customer_ratings.append(rating)
        print(f'Your rating # was {rating}. The average rating for this restaurant is {sum(self.customer_ratings)/len(self.customer_ratings)}')
    

rest1 = Restaurant("McDonald's", 'Burgers')
rest2 = Restaurant('El Meson', 'Tacos')
rest3 = Restaurant('Taco Bell', "'Tacos'")

rest1.describe_rest()
rest2.describe_rest()
rest3.describe_rest()

rest1.rest_open()
rest2.rest_open()
rest3.rest_open()

# 6. Test your new methods: 
# ∗ For each of your example restaurants, run print_num_served() to check the initial 
# value. Then run add_num_served() a few times, inputting different values. Finally, 
# run print_num_served() again to check the updated balance. 
# ∗ For each of your example restaurants, run customer_rating() several times, 
# inputting a different rating each time. Confirm that the average rating updates 
# appropriately each time. 
# ∗ For customer_rating(), try inputting a few “incorrect” values, like the number 6, a 
# decimal number such as 2.5, and a word/phrase such as “5 stars!

