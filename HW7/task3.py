# 3. Створити context manager який буде фарбувати колір виведеного тексту

# https://www.skillsugar.com/how-to-print-coloured-text-in-python

# Приклад:

# print('\033[93m', end='')
# print('aaa')
# print('bbb')
# print('\033[0m', end='')
# print('ccc')

# with colorizer('red'):
#     print('printed in red')
# print('printed in default color')


from colors_settings import colors


class colorizer:

    def __init__(self, color):
        self.color = colors.get(color, colors['end'])

    def __enter__(self):
        print(self.color, end='')

    def __exit__(self, type_, value, traceback):
        print(colors['end'], end='')


print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')


with colorizer('red'):
    print('printed in red')
print('printed in default color')

with colorizer('green'):
    print('printed in green')

with colorizer('magenta'):
    print('printed in magenta')

with colorizer('cyan'):
    print('printed in cyan')
print('printed in default color')
