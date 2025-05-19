def ordinalSuffix(number):
    num_string = str(number)
    if num_string[-2:] in ('11', '12', '13'):
        #The reason we need 11 12 and 13 is because they end in 1 2 3 which can make them 11st 12nd 13rd
        return num_string+'th'
    elif num_string[-1] == '1':
        return num_string+'st'
    elif num_string[-1] == '2':
        return num_string+'nd'
    elif num_string[-1] == '3':
        return num_string+'rd'
    else:
        return num_string+'th'

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
