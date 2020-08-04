from web.encrypter.encoder import get_code

char_1 = {'6': 'Б', '8': 'В', '3': 'З', '0': 'О', '<': 'С', '7': 'Т', '\\': 'У', '4': 'Ч', '*': 'Я'}

char_2 = {'1': {'<': 'К', '*': 'Р' }, '>': {'1': 'Ж', '<': 'Х' }, '/': {'4': 'А','\\': 'Л', '7': 'П'}, '-': {'1': 'Ъ', '=': 'Э', '8': 'Ф' }, '_': {'1': 'Г', '/': 'Д' }}

char_3 = {'1-': {'1': 'Н', '0': 'Ю' }, '/_': {'\\': 'М' , '1': 'Ц'}, '1@': {'1': 'Ы', '*': 'Ь'}}

char_star = {'1=': ['Е', 'Ё'], '/_/': ['И', 'Й']}

char_long = {'1_1_1*': 'Ш', '1_1_1_': 'Щ'}

def star(string, i):
    if len(string) == 2+i:
        return char_star[string[0:2+i]][0]
    elif (len(string) < 5+i) and (string[2]!='*'):
        return char_star[string[0:2+i]][0]
    elif (len(string) < 5+i) and (string[2+i]=='*'):
        return char_star[string[0:2+i]][1]
    elif (len(string) >= 5+i) and (string[2+i]=='*') and (string[2+i:5+i]!='*/1'):
        return char_star[string[0:2+i]][1]
    else:
        return char_star[string[0:2+i]][0]
        
    
def get_char(string):
    if string[0] in char_1.keys():
        return char_1[string[0]]
    elif string[0] in char_2.keys():
        if string[1] in char_2[string[0]].keys():
            return char_2[string[0]][string[1]]
        elif (string[0:2] in char_3.keys()) and (string[2] in char_3[string[0:2]].keys()):
            return char_3[string[0:2]][string[2]]
        elif string[0:2] in char_star.keys():
            return star(string, 0)
        elif (len(string) >= 3) and (string[0:3] in char_star.keys()):
            return star(string, 1)
        elif (len(string) >= 6) and (string[0:6] in char_long.keys()):
            return char_long[string[0:6]]
        else:
            return string[0]
    else:
        return string[0]

def decode(string):
    code = get_code()
    a = len(string)
    decoded = ''
    while(a):
        ch = get_char(string[len(string)-a:])
        if ch in code.keys():
            a -= len(code[ch])
        else:
            a -= 1
        decoded += ch

    return decoded

