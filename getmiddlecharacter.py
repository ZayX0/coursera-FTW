def get_middle(s):
    numChar = len(s)

# If number of letters is even, divide by 2, split from middle number

    if numChar % 2 == 0:
        splitEven = list(s)
        middleChar = numChar / 2

# Grab index number of character in list to join back together

        finalMaybe = (splitEven[int(middleCharE - 1):int(middleCharE + 1)])
        final = finalMaybe[0] + finalMaybe[1]
        return final
    else:
        middleChar = numChar / 2

get_middle('testing')
