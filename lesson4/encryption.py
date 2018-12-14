text = 'hallo welt, mir gehts gut!'


def encrypt(text):
    result = ''
    for char in text:
        if char in 'aAeEiIoOuU':
            result += 'X'
        else:
            result += char
    return result


encrypted_text = encrypt(text)
print(encrypted_text)
# hXllX wXlt, mXr gXhts gXt!
