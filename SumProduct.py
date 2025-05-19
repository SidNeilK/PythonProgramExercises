def calculateSum(numbers):
    if len(numbers)==0:
        return 0
    total=0
    for i in range(len(numbers)):
        total+=numbers[i]
    return total

def calculateProduct(numbers):
    if len(numbers)==0:
        return 1
    total=1
    for i in range(len(numbers)):
        total*=numbers[i]
    return total

assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840

