from lesson4.encryption import encrypt, decrypt

text = 'das ist mein TEXT, der ERSETZT werden soll      '
encr = encrypt(text)
print(encr)

print(decrypt(encr))