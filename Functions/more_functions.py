# 2. The first should be named display_mailing_label(), with five parameters: 
# name, address, city, state and zip. In the function, use print() statements to format and 
# display the data as you would on an address label. 

# 3. The second function should be named add_numbers() with one parameter defined 
# to accept any number of arguments, each argument being an integer. Add the given 
# arguments together and display the result using the following format: 
# number [+ number2 + number3  …] = result 

# 4. The third function should be named display_receipt() and accept two 
# parameters: total_due and amount_paid. Compute and display the change due in the 
# following format: 
# Total Due: $_____ 
# Amount Paid: $_____ 
# Change Due: $____ 
# If the amount paid is less than the total due, display a message indicating the 
# remaining balance to be paid. 

# 5. When you have defined each function: 
# ∗ Call display_mailing_label() at least twice with data for two different people. 
# ∗ Call add_numbers() three times with one number, two numbers, and your choice of 
# however many numbers. 
# ∗ Call display_receipt() three times. The first time, overpay the bill. The second time, 
# pay the bill exactly. The third time, underpay the bill.

def display_mailing_label(name, address, city, state, zip):
    print(f'{name}\n{address}\n{city} {state} {zip}')


def add_numbers(*args):
    #adds all arguments
    total = sum(args)

    # empty string to collect all numbers
    numbers = ''
    for i, arg in enumerate(args):
        numbers += str(arg)
        if i < len(args) - 1:  # adds + in betweeen every number
            numbers += ' + ' 
    print(f'{numbers} = {total}')


def display_receipt(ttl_due, amt_paid):
    change_due = amt_paid - ttl_due
    if change_due < 0:
        print(f'Insufficient funds! You still owe ${ttl_due - amt_paid : .2f}')
    elif change_due >= 0:
         print(f'Total Due:   ${ttl_due:.2f}\n'
               f'Amount Paid: ${amt_paid:.2f}\n'
               f'Change Due:  ${change_due:.2f}')

# test first function
display_mailing_label('Jeff Rogers', '3125 N big st', 'New York', 'NY', '55861')
display_mailing_label('Harry Potter', '934 S Train st','Dumbletown', 'OR', '19717' )
print('')

# test aecomds function
add_numbers(10)
add_numbers(10, 25)
add_numbers(10, 25, 35, 66, 75)
print('')

# test third functions
display_receipt(10.25,15.00)
display_receipt(50, 50)
display_receipt(27.36, 20)
