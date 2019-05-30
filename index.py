from robots.text import Robot
import pprint

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
    content = {}
    content['search_term'] = input('Type a Wikipedia search term: ')
    content['prefix'] = ask_and_return_prefix()

    robot = Robot()
    wikipedia_content = robot.fetch_content_from_wikipedia(content)
    content['source_content_original'] = wikipedia_content['content']
    content['source_content_sanitized'] = robot.sanitize_content(content['source_content_original'])
    content['sentences'] = robot.break_content_into_sentences(content['source_content_sanitized'])
    pprint.pprint(content)


if __name__ == '__main__':
    start()
