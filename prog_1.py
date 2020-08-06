something = ''
phrase = ''
while something != '\end':
    something = input('input something: ')
    if something != '\end':
        if something.startswith(('wh', 'how')):
            phrase = phrase + something.capitalize() + '? '
        else:
            phrase = phrase + something.capitalize() + '. '
print()
print(phrase)