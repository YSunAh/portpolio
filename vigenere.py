
def vigenere_encrypt( helloworld , key ):
    if key == '':
        key = 'sky'

    output_text = ""
    key_len = len(key)
    index = 0
    for letter in input_text:
        if letter == ' ':
            output_text+= ' '
            continue
        pos = index % key_len
        ordi = ord(letter) + ord(key[pos])
        output_text += chr(ordi)
        index+=1
    return output_text

def vigenere_decrypt( helloworld , key):
    if key == '':
        key = 'sky'
    output_text = ""

    key_len = len(key)
    index= 0
    for letter in input_text:
        if letter == ' ':
            output_text+= ' '
            continue
        pos = index % key_len
        ordi =  ord(letter) - ord(key[pos])
        output_text+= chr(ordi)
        index+=1
    return output_text
