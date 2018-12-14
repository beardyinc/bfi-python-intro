text = ['heute', 'ist', 'es', 'draußen', 'sehr', 'kalt']

for ch in text:
    if 'ß' in ch:
        print('-- error, illegal character found: ', ch)
        ch = ch.replace('ß', 'ss')
        print('within the if: ', ch)
    print('after the if: ', ch)
