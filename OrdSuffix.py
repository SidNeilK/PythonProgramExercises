def ordinalSuffix(number):
    num_str = str(number)
    if num_str[-2:] in ('11', '12', '13'):
        return num_str + 'th'
    elif num_str[-1] == '1':
        return num_str + 'st'
    elif num_str[-1] == '2':
        return num_str + 'nd'
    elif num_str[-1] == '3':
        return num_str + 'rd'
    else:
        return num_str + 'th'

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