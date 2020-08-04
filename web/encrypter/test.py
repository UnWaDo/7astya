from encoder import encode
from decoder import decode

string = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
en_string = encode(string)
print(string)
print(en_string)
print(decode(en_string))
input('Нажмите Enter для выхода из программы . . .')
