import string

alphabet = string.ascii_letters + string.digits + "!{_}?"
ct = 'ldtdMdEQ8F7NC8Nd1F88CSF1NF3TNdBB1O'  # Replace with your actual ciphertext

def decrypt_caesar(ciphertext, key):
    decrypted_text = ""
    for i in ciphertext:
        decrypted_text += (alphabet[(alphabet.index(i) - key) % len(alphabet)])
    return decrypted_text

def find_key(ciphertext, prefix, alphabet):
    for key in range(len(alphabet)):
        decrypted_text = decrypt_caesar(ciphertext, key)
        if decrypted_text.startswith(prefix):
            return key
    return None

prefix = 'KCSC{'
found_key = find_key(ct, prefix, alphabet)

if found_key is not None:
    print(f"Found key: {found_key}")
    decrypted_flag = decrypt_caesar(ct, found_key)
    print(f"Decrypted flag: {decrypted_flag}")
else:
    print("Key not found.")
