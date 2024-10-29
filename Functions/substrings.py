# 1. Create a new script file named substrings.py.  
# ∗ Start by working with a variable containing a full name, e.g. name = ‘John Doe’ 
# ∗ Write code to find the space in the name, then extract the first and last name and 
# display the results. Output might look like: 
# Full Name: John Doe 
# First Name: John 
# Last Name: Doe 
# 2. Once you have the code working for one name, test your script with at least three times 
# with different names. The full output (full name, first name, last name) should be 
# printed for each name. Examples: 
# parse_and_display(‘John Doe’) 
# parse_and_display(‘Grace Flores’) 
# parse_and_display(‘JB Oinonen’)

name = 'Mochi Reyes'
full_name = name.split(' ')
first_name = full_name[0]
last_name = full_name[1]

print('Full Name:', name)
print('First Name:', first_name)
print('Last Name:', last_name)