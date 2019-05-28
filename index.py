def ask_and_return_prefix():
    _prefixes = {
        1: 'Who is',
        2: 'What is',
        3: 'The history of'
    }
    _DEFAULT = "This option don't exist. Try again!"

    while True:
        print('Option: ')
        for value in _prefixes:
            print(f'{value} - {_prefixes[value]}')
        _option = int(input('Chose one option: '))

        if _prefixes.get(_option):
            return _prefixes.get(_option)
        print(_DEFAULT)


def start():
    constant = {}
    constant['searchTerm'] = input('Type a Wikipedia search term: ')
    constant['prefix'] = ask_and_return_prefix()

    print(constant)


if __name__ == '__main__':
    start()
