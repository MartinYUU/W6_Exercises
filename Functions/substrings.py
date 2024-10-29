# 1. Create a new script file named substrings.py.  
# ∗ Start by working with a variable containing a full name, e.g. name = ‘John Doe’ 
# ∗ Write code to find the space in the name, then extract the first and last name and 
# display the results. Output might look like: 
# Full Name: John Doe 
# First Name: John 
# Last Name: Doe 


# name = 'Mochi Reyes'
# full_name = name.split(' ')
# first_name = full_name[0]
# last_name = full_name[1]

# print('Full Name:', name)
# print('First Name:', first_name)
# print('Last Name:', last_name)


#################################################### CHALLENGE ############################################################

name = 'Megan Thee Stalion'
full_name = name.split(' ')

if len(full_name) == 1:
    print ('Name:', full_name[0])
elif len(full_name) == 2:
    print(' Full Name:', name +"\n " \
          'Frist Name:', full_name[0]+ "\n", \
          'Last Name:', full_name[1]
          )
elif len(full_name) == 3:
    print(' Full Name:', name +"\n " \
          'Frist Name:', full_name[0]+ "\n", \
          'Middle Name:', full_name[1] + "\n", \
          'Last Name:', full_name[2]
          )
