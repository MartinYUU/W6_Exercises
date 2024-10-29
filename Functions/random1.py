import random

list_of_strings = ['hi', 'how', 'are', 'you', '?']
list_of_nums = [1, 2, 3, 4, 5, 6, 8, 9]

print(random.randint(1, 10))
print(random.random())
print(random.choice(list_of_strings))
print(random.choices(list_of_nums, k = 3))
print(random.sample(list_of_nums, k = 4))
# shuffle does not return a value
random.shuffle(list_of_strings)
print(list_of_strings)
