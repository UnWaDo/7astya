from encoder import encode
from decoder import decode

string = input('Введите строку: ')
en_string = encode(string)
print(string)
print(en_string)
print(decode(en_string))
input('Нажмите Enter для выхода из программы . . .')
