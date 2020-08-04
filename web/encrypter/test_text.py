from encoder import encode
from decoder import decode

import re


regexp = re.compile('[/\\0134678_\-@\*\=\<\>]')
f = open(r'test.txt', encoding='utf-8')
string = ''
for line in f:
    string += line
f.close()

comp_string = regexp.sub('#', string)
t = regexp.sub('#', comp_string)

while (t != comp_string):
    comp_string = t
    t = regexp.sub('#', comp_string)

comp_string = str.upper(comp_string)

en_string = encode(string)
dec_string = decode(en_string)
print('Исходная строка: '+string)
print('Зашифрованная строка: '+en_string)
print('Дешифованная строка: '+dec_string)
print('\n')
print('Строка сравнения: '+comp_string)
print('Результат сравнения: '+str(comp_string == dec_string))
input('Нажмите Enter для выхода из программы . . .')
