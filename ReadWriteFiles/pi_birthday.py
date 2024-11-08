with open('pi_million_digits.txt', 'r') as f:
    # print(f.readline())
    pi_lines = f.readlines()
#print(pi_lines)

b_day = input('What is your birthday in the format mmddyy?: ')
bday_found = None
for i in pi_lines:
    if b_day in i:
        print('Your birthday is in the first million digits of pi')
        bday_found = 1
        break
# only Prints if the loop finishes -- No bday found
else :
    print('“Sorry, your birthday was not found in the first million digits of pi')

# print(pi_lines[0:2])

pi_string = ''
for i in pi_lines:
    pi_string += i.strip()

# modified becuase I used for else earlier 
if bday_found == 1:
    birthday_position = pi_string.index(b_day) - 1
    # we do -1 because index 0 is assigned to 3, index 1 is assigned to .
    # and index 2 is assigned to the first digit of pi. therefor we only need to 
    # subtract 1 from the index to start counting the digits starting from 1
    print(f'Your birthday begins at decimal place {birthday_position}')
