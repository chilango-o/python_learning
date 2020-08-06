from random import randint

lower = 1
upper = 100
errChar = "invalid character, let's try again"

def correctChar(input):
    isCorrect = input == 'y' or input == 'n'
    if not isCorrect:
        print(errChar)
    return isCorrect

def update(current_Guess, is_Lower):
    global upper
    global lower
    if is_Lower == 'y':
        upper = current_Guess
    else:
        lower = current_Guess
    return int(((upper-lower)/2)+lower)

def guessGame():
    currentGuess = randint(lower, upper)
    guessed = False
    while not guessed:
        print('is your number', currentGuess, '?')
        foundFeedback = input('(y/n)').lower()
        if correctChar(foundFeedback):
            guessed = foundFeedback == 'y'
            if (guessed):
                print("Great, I won! let's try again some other time")
                print('Bye!')
            else:
                isLower = input('lower? (y/n)').lower()
                if (correctChar(isLower)):
                    currentGuess = update(currentGuess, isLower)

guessGame()