


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


def name_game(name):
    yield f'{name}, {name}, bo-b{trunc_name(name)}'
    yield f'Bonana-fanna fo-f{trunc_name(name)}'
    yield f'Fee fi mo-m{trunc_name(name)}'
    yield f'{name}!\n'

tests = [name, 'carly', 'CHARLIE', 'Aidan', 'Braden', 'Billy Bob']

for i in tests:
    for x in name_game(i):
        print(x)