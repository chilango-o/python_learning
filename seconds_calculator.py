def calcSec():
    """ A function that calculates a given number of seconds (user_seconds)
    and outputs that value in Hour-minute-second format
    """
    user_seconds = int(input('cuantos segundos? '))
    hours = user_seconds // 3600 #integer division between the given seconds and the number of seconds in 1 hour (calculation of the whole hrs in the given seconds)
    reminder_hours = (user_seconds % 3600) # The remainder of seconds of the hour division (modulus operation)
    minutes = reminder_hours // 60 # the whole minutes in the seconds given
    reminder_seconds = reminder_hours % 60 # the number of whole seconds of the total given
    print('hours:', hours, 'minutes:', minutes, 'seconds:', reminder_seconds)

calcSec()