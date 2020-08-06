def average(a, b):
    """function for averaging two numbers

    Args:
        a (int): some integer number
        b (int): some integer number

    Returns:
        int: the average of 'a' and 'b' numbers
    """
    return (a+b)/2

def square_root(num, low, high):
    """function to calculate the square root of a number

    Args:
        num (int): the number to know its square root
        low (int): the lowest number between the square root is expected
        high (int): the highest number between the square root is expected
    """
    for i in range(120):
        guess = average(low, high)
        if guess**2 == num:
            break
        elif guess**2 > num: #guess lower
            high = guess
        else:
            low = guess
    print(guess)

for i in range(1, 26):
    square_root(i, 1, 5)