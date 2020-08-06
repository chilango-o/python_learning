phrase = ''
suffix = ''
interrogatives = ('wh', 'how')

while True:
    something = input('input something: ')

    if something == '\end': break
    
    suffix = '?' if something.lower().startswith(interrogatives) else '.'
    phrase += something.capitalize() + suffix + ' '

print(phrase)