def encrypt(plaintext):
    vocals = 'aAeEiIuUoO'
    result = ''
    space = ' '

    for cur_char in plaintext:

        if cur_char in vocals:
            # do something here!!
            result += 'X'
        elif cur_char == space:
            result += 'Y'
        else:
            result += cur_char

    return result


def decrypt(encryptedText):
    return encryptedText.replace('Y', ' ')
