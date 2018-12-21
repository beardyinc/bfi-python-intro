# global scope
name = 'franzl'


def hello_name(name):
    def get_firstname(name):
        return 'first ' + name;

    # local scope
    print('hello ' + get_firstname(name))


print(name)
hello_name('karl')
