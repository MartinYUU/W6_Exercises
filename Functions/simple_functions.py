#  Write a script named simple_functions.py. In it, define three functions as follows. 
# 2. The first function should be named favorite_things() and include three 
# parameters. 
# ∗ In this function, use print() to display 3 lines listing your name, your favorite movie, 
# and your favorite musician / band. 
# 3. The second should be named why_im_here(). 
# ∗ With this function, display a sentence that describes why you joined this Data 
# Analyst program. 
# 4. The last function should be named favorite_place(), with two parameters. 
# ∗ Use this function to display a sentence that describes one of your favorite places to 
# visit and why. 
# 5. Finally, after you have written the three functions, call each of them with the 
# appropriate arguments. For favorite_place(), call this function twice, using different 
# places each time.

def favorite_things():
    print('My name is Martin\nMy favorite movie is Narnia\nMy favorite band is The Beatles')
    
def why_im_here():
    print('I am here to become a Data Analyst')

def favorite_place(fav_place, reason):
    print(f'One of my favorite places to visit is {fav_place} because {reason}')


favorite_things()
why_im_here()
favorite_place('wakanda', 'wakanda forever')
favorite_place('mars', 'aliens are cool')