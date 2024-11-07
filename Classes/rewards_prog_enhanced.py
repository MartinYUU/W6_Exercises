#     Add a new method called visit_rest() that accepts two inputs: 
# ∗ Prompt for “Name of restaurant: ”. Check if the restaurant is currently in 
# self.restaurants_visited, and if not, add it to the list. 
# ∗ Prompt for “What was the total food bill for this visit?” and convert that to a rewards 
# point amount at a rate of $1 to 1 point. Rewards points should round down to the 
# nearest whole number. Add the points earned to self.rewards_points. Print the 
# output: 
# Points for this visit: ___ 
# Total rewards points earned: ___ 
# Thank you for visiting [name of restaurant]!

cust_list = []
class RewardsProgram:
    '''Rewards program account for a customer'''

    def __init__(self, cust_name, Phone, email ):
        self.cust_name = cust_name
        self.phone = Phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = 0
    
    #prints profile info
    def profile(self):
        print(f'name : {self.cust_name}\nphone: {self.phone}\nEmail: {self.email}')

    # prints thank you message
    def thank_you(self):
        print(f'Thank you {self.cust_name}, for visiting our restaurant!')
    
    # adds profile info to cust list
    def add_to_cust_list(self):
        global cust_list
        cust_list.append((self.cust_name, self.phone, self.email))

    def visit_rest(self):
        rest_visited = input('What is the name of the restaurant you visited?: ')
        if rest_visited not in self.restaurants_visited:
            self.restaurants_visited.append(rest_visited)
        bill_total = float(input('What was the total food bill for this visit?: '))
        visit_points = int(bill_total)
        self.rewards_points += visit_points
        print(f'''Points for visit: {visit_points}
Total rewards points earned: {self.rewards_points}
Thank you for visiting {rest_visited}!''')


customer1 = RewardsProgram("Peter Parker", "773-515-1234", "peter.parker@dailybugle.com")
# customer1.profile()
# customer1.thank_you()
# customer1.add_to_cust_list()

customer2 = RewardsProgram("Natasha Romanoff", "708-875-5618", "natasha@shield.com")
# customer2.profile()
# customer2.thank_you()
# customer2.add_to_cust_list()

customer3 = RewardsProgram("Tony Stark", "312-361-8665", "tony@starkindustries.com")
# customer3.profile()
# customer3.thank_you()
# customer3.add_to_cust_list()

# for i in cust_list:
#     print(i)


customer1.visit_rest()
customer2.visit_rest()
customer3.visit_rest()