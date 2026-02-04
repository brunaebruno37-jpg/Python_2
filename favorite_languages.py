from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

'''for name, language in favorite_languages.items():
    print(f'{name.title()} linguagem favorita é {language.title()}.')
'''

from random import randint

x = randint(1, 6)


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)
    
die = Die()

for dado in range(10):
    print(die.roll_die())

    