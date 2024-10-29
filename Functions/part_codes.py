# 2. Create a script that parses a part code in the following format: 
# supplier:productcode-size 
# Examples: 
# ACME:123-L Part #123, size large, supplied by Acme 
# DI:12345-M Part #12345, size medium, supplied by DI 
# ACE:1-12 Part #1, size 12, supplied by Ace 
# 3. Sketch your ideas for the functions below on a piece of paper: 
# get_supplier_code()  returns all characters before the : 
# get_product_num()  returns all characters between the : and - 
# get_size()  returns all characters after the - 
# Perform initial code review of each other’s ideas with a classmate. Then, code each 
# function. 
# 4. Once you have your functions ready, create variables to hold the three example part 
# codes from above. Call all three functions for each part code and display the results. 
# ∗ CHALLENGE: Try creating a variable that contains all three part codes as a list. How 
# can you get your script to work with this list input?  
# 5. Remember to commit changes when you are done!

#created order info variables first
order_info1 = 'ACME:123-L Part #123, size large, supplied by Acme'
order_info2 = 'DI:12345-M Part #12345, size medium, supplied by DI'
order_info3 = 'ACE:1-12 Part #1, size 12, supplied by Ace'

# created this function first. it will add characters to a string return every character
# in the given string until ir reaches the first ':' then breaks the loop and then returns the final string
def get_supplier_code(order_info):
    code = ''
    for i in order_info:
        if i != ':':
            code += i
        elif i == ':':
            break
    return code
    

# I created this function second (took much longer ). it follows similar logic in that it starts with a 
# blank string and adds character to that string as the for loop parses the order info string as long 
# as the current character is between : and -. the function then breaks the loop and returns the result   
def get_product_num(order_info):
    between = False # used for condition in first elif statement
    pnum = ''
    for i in order_info:
        if i == ':':
            between = True
        elif i == '-' and between ==True:
            between == False
            break
        elif between == True:
            pnum += i 
    return pnum


# created this function last. I again used a boolean variable to determine if the for loop 
# has reached the character - . once it has it adds every remaing character in the order_info string
# to the size string and then returns the ending size string
def get_size(order_info):
    after_char = False
    size = ''
    for i in order_info:
        if i == '-':
            after_char = True
        elif after_char == True:
            size += i
    return size


# testing first function
print(get_supplier_code(order_info1))
print(get_supplier_code(order_info2))
print(get_supplier_code(order_info3))
# testing second function
print(get_product_num(order_info1))
print(get_product_num(order_info2))
print(get_product_num(order_info3))   
# testing third function
print(get_size(order_info1))
print(get_size(order_info2))
print(get_size(order_info3))
