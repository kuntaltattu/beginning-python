#version2
import math

def divideIntoParts(amount, denominations, filterZeroes = False):
    accumulator = amount
    result = []
    for denomination in sorted(list(set(denominations)), reverse = True):
        # `a // b` stands for truncating division, same as `int(a / b)`
        # we create a tuple of denomination and count for easier display
        countInfo = (denomination, (accumulator // denomination))
        result.append(countInfo)
        # equivalent to `accumulator = accumulator % denomination`
        accumulator = int(math.fmod(accumulator, denomination))
    return filter(lambda item: (filterZeroes and item[1] > 0), result)

string = input("Enter the denominations")
notes = list(map(lambda x: int(x), string.split(" ")))
print(notes)
maxDenominationDigits = max(map(lambda x: len(str(x)), notes))

while True:
    amount = int(input("Enter the amount: "))
    dividedAmount = divideIntoParts(amount, notes )
    printed = False
    for denomination, count in dividedAmount:
        printed = True
        print("The number of ₹{:<{width}d} notes is {:d}".format(denomination, count, width = maxDenominationDigits))
    if not printed:
        print ("Sorry")
    if input("Repeat? Y/N: ").lower() == 'n':
        break
