numberRange = [0, 16, 17, 18.5, 25, 30, 35, 40]
statusRange = ['Severe Thinness', 'Moderate Thinness', 'Mild Thinness','Normal', 'Overweigth', 'Obesse class I', 'Obesse class II', 'Obesse class III']
originalArraysLength = len(numberRange)

def calcBMI(weight, height):
    """ function to calculate the Body mass index (BMI)

    Args:
        weigth (float): the weigth in kilograms
        height (float): the height in meters

    Returns:
        float: the Body mass index (BMI) calculated
    """
    return weight/height**2

""" 
def calcBmiRange(bmi):
    if bmi < 16:
        return 'Severe Thinness'
    elif bmi >= 16 and bmi < 17:
        return 'Moderate Thinness'
    elif bmi >= 17 and bmi < 18.5:
        return 'Mild Thinness'
    elif bmi >= 18.5 and bmi < 25:
        return 'Normal'
    elif bmi >= 25 and bmi < 30:
        return 'Overweigth'
    elif bmi >= 30 and bmi < 35:
        return 'Obesse class I'
    elif bmi >= 35 and bmi < 40:
        return 'Obesse class II'
    elif bmi > 40:
        return 'Obesse class III'

 """

def calcBmiRange(bmi):
    """function to calculate the category for a given BMI

    Args:
        bmi (float): the calculated BMI from calcBMI()

    Returns:
        string: the caption of the corresponding category
    """
    number_range = [16, 17, 18.5, 25, 30, 35, 40]
    status_range = ['Moderate Thinness', 'Mild Thinness','Normal', 'Overweigth', 'Obesse class I', 'Obesse class II']

    if bmi < 16:
        return 'Severe Thinness'
    for i in range(len(number_range)-1):
        if bmi >= number_range[i] and bmi < number_range[i+1]:
            return status_range[i]
    if bmi > 40:
        return 'Obesse class III'
    
def calcBmiRangeRecursive(bmi, numberRange, statusRange):
    # global originalArraysLength
    arraysLength = len(numberRange)
    # print('\n--- Nivel de recursion: ', arraysLength - originalArraysLength, ' ---')
    # print(numberRange)
    # print(statusRange)
    if arraysLength == 1:
        return statusRange[0]
    elif bmi >= numberRange[0] and bmi < numberRange[1]:
            return statusRange[0]
    else:
        return calcBmiRangeRecursive(bmi, numberRange[1:arraysLength], statusRange[1:arraysLength])

print('\nBMI calculator')
weight = float(input('\nwhats you weight in kg? '))
height = float(input('whats you height in m? '))
bmi = calcBMI(weight, height)
bmi_range = calcBmiRange(bmi)
bmiRangeRecursive = calcBmiRangeRecursive(bmi, numberRange, statusRange)
print('\nyour BMI is:', round(bmi, 1))
print('your STATUS is:', bmi_range, '\n')
print('your Recursive STATUS is:', bmiRangeRecursive, '\n')
