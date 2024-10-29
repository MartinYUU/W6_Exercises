import datetime 

# 2. Define a variable called today that represents the current date and time using 
# datetime.datetime.now()  
# ∗ Using the .strftime() method, identify the following pieces of information and 
# print the output: 
# Today is [day of week], [month] [day], [year]

# 3. Define a variable for your birthday using datetime.date(). 
# ∗ Again using the .strftime() method, create the following output: 
# My birthday is MM/DD/YYYY

# 4. Define a variable for ninety_d which will be used to represent the date 90 days from 
# today.  
# ∗ Set the value of this variable to add the following values: 
# today + datetime.timedelta(days=90)  
# ∗ Again using the .strftime() method as needed, print the following output: 
# 90 days from today is [month] [day], [year]

# 5. Define a variable for dinner_time using datetime.time(). 
# ∗ Again using the .strftime() method, create the following output: 
# Let’s meet for dinner at HH:MM PM

today_date = datetime.datetime.now()
print(today_date.strftime("Today is %A, %B %d, %Y"))

my_bday = datetime.date(1998, 9, 20)
print(my_bday.strftime("My birthday is %m/%d/%Y"))

ninety_d = datetime.datetime.now() + datetime.timedelta(days = 90)
print(ninety_d.strftime("90 days from today is %B %d, %Y"))

dinner_time = datetime.time(18, 30)
print(dinner_time.strftime("Let's meet for dinner at %I:%M %p"))