def factors(numbers):
    '''returns the greatest common factor of given numbers'''
    mcd = 0
    lastMcd = 0
    for i in range(1, (min(numbers))+1):
        for j in numbers:
            if j%i == 0:
                mcd = i
            else:
                mcd = lastMcd
                break
        lastMcd = mcd
    return mcd

nmb=[]
while True:
    inpt = input('numero (type letter "v" to scape): ')
    if inpt.lower() != 'v':
        try:
            nmb.append(int(inpt))
        except:
            print('invalid character')
    else:
        break

print('the greatest common factor of', nmb, 'is:', factors(nmb))
