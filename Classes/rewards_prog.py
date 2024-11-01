# 1. Create a new script named rewards_prog.py. In it, make a class called 
# RewardsProgram. Be sure to include a docstring below the class name to describe 
# the purpose of the class. The __init__() method for RewardsProgram should store 
# the following instance variables: 
# ∗ cust_name for customer name 
# ∗ phone for customer phone 
# ∗ email for customer email 
# 2. Add two methods to the class: 
# ∗ The first method should be named profile() and prints the output: 
# Name: [customer name] 
# Phone: [customer phone] 
# Email: [customer email] 
# ∗ The second method should be named thank_you() and prints the message:  
# Thank you, [name], for visiting our restaurant! 
# ∗ The third method should be named add_to_cust_list(). This should add the 
# customer’s name, phone, and email as a tuple to a list named cust_list, which 
# should be global in scope. (Where should this variable be created to ensure that 
# running this method adds to it and doesn’t overwrite any existing values?) 
# 3. Create three instances of the class, making up sample data for three different 
# customers. For each customer, run the profile(), thank_you(), and add_to_cust_list() 
# methods. 
# 4. Finally, print the contents of cust_list to confirm that all customers have been added.
cust_list = []
class RewardsProgram:
    '''Rewards program account for a customer'''

    def __init__(self, cust_name, Phone, email ):
        self.cust_name = cust_name
        self.phone = Phone
        self.email = email
    
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

customer1 = RewardsProgram("Peter Parker", "773-515-1234", "peter.parker@dailybugle.com")
customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()

customer2 = RewardsProgram("Natasha Romanoff", "708-875-5618", "natasha@shield.com")
customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()

customer3 = RewardsProgram("Tony Stark", "312-361-8665", "tony@starkindustries.com")
customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()

for i in cust_list:
    print(i)