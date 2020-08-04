def get_code():
    f = open('/home/ubuntu/7astya/web/encrypter/code.txt', encoding='utf-8')

    r_lines = ''
    for line in f:
        r_lines+=line
    f.close()
    lines = r_lines.split('\n')
    code = {}
    for line in lines:
        if len(code)>=33:
            break
        k, v = line.split(' — ')
        code[k]=v
    return code

def encode(string):
    string = str.upper(string)
    code = get_code()
    encoded = ''
    for i in string:
        if i in code.keys():
            encoded+=code[i]
        elif i in '/\\0134678_-@*=<>':
            encoded+='#'
        else:
            encoded+=i
    return encoded

