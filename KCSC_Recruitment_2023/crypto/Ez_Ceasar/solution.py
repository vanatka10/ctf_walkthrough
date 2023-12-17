import string

alphabet = string.ascii_letters + string.digits + "!{_}?"

def decrypt(cipher, key):
    flag = ""
    for i in cipher:
        flag += alphabet[(alphabet.index(i) + key) % len(alphabet)]
        print(flag)
    return flag

def find_key(cipher):
    for key in range(0, 2**256):
        print(key)
        if decrypt(cipher, key).startswith('KCSC{'):
            print(key, decrypt(cipher, key))
            break

find_key('ldtdMdEQ8F7NC8Nd1F88CSF1NF3TNdBB1O')
