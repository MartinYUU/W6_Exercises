# 3. Use a combination of functions from all three models to create calculations that will 
# support the following output: 

# _Experimenting with a subset of integers 1-100: 
# Sum of 75 sample values from 1 to 100: ____ 
# Average of 75 sample values: ____ 
# Median of 75 sample values: ____ 

# _Experimenting with a superset of 200 values, integers 1-100: 
# Average of 200 values: ____ 
# Median of 200 values: ____ 
# Mode of 200 values: ____ 
# Standard deviation of 200 values: ____ 
# Variance of 200 values: ____ 

# _Modeling a random circle: 
# Radius = __, area = ____ (rounded up to the nearest integer) 
# Radius = __, area = ____ (rounded down to the nearest integer) 
# ∗ Include the printed headers beginning with an underscore and line breaks in your 
# output. For line breaks, use print('\n') 
# ∗ You will likely want to create additional variables to use in each step of your 
# calculations – don’t try to do the whole calculation in the print line! 
# ∗ If you need a reminder of how to calculate the area of a circle, in math the formula is 
# usually written as: 
# area = π(r2) 
# where π is the symbol for pi and r represents radius, which must be squared. You’ll 
# need to translate this into a Python expression for pi times radius squared.

import random 
import math 
import statistics 

vals1_100 = range(1,100) 
vals_sample = random.sample(range(1, 100), 75) 
vals_choices = random.choices(range(1, 100), k = 200)
radius = random.randint(3,10)  
pi = math.pi


print('\n_Experimenting with a subset of integers 1-100: ')
print('Sum of 75 sample values from 1 to 100:', math.fsum(vals_sample))
print('Average of 75 sample values:', statistics.mean(vals_sample))
print('Median of 75 sample values:', statistics.median(vals_sample))

print('\n_Experimenting with a superset of 200 values, integers 1-100: ')
print('Average of 200 values:', statistics.mean(vals_choices))
print('Median of 200 values:', statistics.median(vals_choices))
print('Mode of 200 values:', statistics.mode(vals_choices))
print('Standard deviation of 200 values:', statistics.stdev(vals_choices))
print('Variance of 200 values:', statistics.variance(vals_choices))

print('\n_Modeling a random circle: ')
print(f'radius = {radius}, area = {math.ceil(2 * pi * radius)} (rounded up to the nearest integer)')
print(f'radius = {radius}, area = {math.floor(2 * pi * radius)} (rounded down to the nearest integer)')