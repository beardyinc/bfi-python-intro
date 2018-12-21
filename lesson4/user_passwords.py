user_database = {
    'user1': 'asdf023098asdfljasl;dk09823j',
    'user2': 'asfdla098213pokasd0-f921pj',
    'user3': 'lkeruip32pmpoj230;b;k;l34'
}

print('all users: ', user_database.keys())

print('all passwords: ', user_database.values())

if 'user2' in user_database.keys():
    print(' user2 has an account')

for u, p in user_database.items():
    print('user ', u, ' password: ', p)
