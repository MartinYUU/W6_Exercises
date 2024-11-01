# Next, create a function called trunc_name to create a truncated version of the name 
# for using in the song. 
# ∗ Consider how to account for inputs that might use different capitalization. The 
# function output should always be in lower case. 
# ∗ You will need to implement some if/elif/else logic to account for differences in 
# names beginning with a vowel, one consonant, or two consonants. For instance, 
# here is what the truncated output should be for each of the following examples: 
# Ann : ann  Dan : an  Stan : an 
# 5. Print the output to test your function with different name inputs. When you are 
# satisfied with your trunc_name function, comment out the print line. 
# 6. Define another function called name_game(). This will be a generator function. 
# ∗ Create a separate yield statement for each line of the name game, e.g.: 


# will be used to find the first vowel in a name
vowels = ['a', 'e', 'i', 'o', 'u']

name = input('what is your name? :')

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
    elif name[1] == 'f':
        yield f'{name}, {name}, bo-{trunced_name}'
        yield f'Banana-fanna fo-{trunced_name}'
        yield f'Fee fi mo-m{trunced_name}'
        yield f'{name}!\n'
    elif name[2] == 'm':
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

