


# will be used to find the first vowel in a name
vowels = ['a', 'e', 'i', 'o', 'u']
name = ''
while name == '':
    name = input('Name? ').strip().lower()
    if name == '':
        print('You must enter a name.')


while len(name) < 2:
    print('Name must be at least 2 letters long')
    name = input('Name? ').strip().lower()

while True:
    num_name = False  
    for i in name:
        if i.isdigit() == True:  
            num_name = True
            break 
    if num_name == False:  
        break  
    print('Your name must have no numbers.')
    name = input('Name? ').strip().lower()

def trunc_name(name):
    name = name.lower()
    game_name = ''
    first_vowel_pos = 0
    for i in name:
        if i in vowels:
            first_vowel_pos = name.find(i)
            break
    game_name = name[first_vowel_pos:]
    return game_name

# included special rules for b, f, m
def name_game(name):
    name = name.lower()
    trunced_name = trunc_name(name)
    if name[0] == 'b':
        yield f'{name}, {name}, bo-{trunced_name}'
        yield f'Banana-fanna fo-f{trunced_name}'
        yield f'Fee fi mo-m{trunced_name}'
        yield f'{name}!\n'
    elif name[0] == 'f':
        yield f'{name}, {name}, bo-{trunced_name}'
        yield f'Banana-fanna fo-{trunced_name}'
        yield f'Fee fi mo-m{trunced_name}'
        yield f'{name}!\n'
    elif name[0] == 'm':
         yield f'{name}, {name}, bo-b{trunced_name}'
         yield f'Banana-fanna fo-f{trunced_name}'
         yield f'Fee fi mo-{trunced_name}'
         yield f'{name}!\n'
    else:
        yield f'{name}, {name}, bo-b{trunced_name}'
        yield f'Banana-fanna fo-f{trunced_name}'
        yield f'Fee fi mo-m{trunced_name}'
        yield f'{name}!\n'

tests = [name, 'carly', 'CHARLIE', 'Aidan', 'Braden', 'Billy Bob']

for i in tests:
    for x in name_game(i):
        print(x)



# 7. In the sample script above, why is the first loop using “pass” in the except block, where 
# the error is being caught? What’s the logic behind this? Add a comment to the bottom 
# of your script with your explanation. 
# -- pass was used because , if the exceptiom was not raised, then the input has all numerical
# characters meaning the input was invlaid and th eloop continues reprompting for a new name
#  and if the exception is raised, then pass ignors it meaning the input has letters. However, 
# This does not handle a mix of int and letters


# 8. In the second and third loops, what does the statement raise SystemExit(0) 
# mean? Why do you think this is used instead of break? Add a comment to the bottom 
# of your script with your thoughts.
# I believe SystemExit(0) was used to terminate the entire program and not just 
# exit the loop.