import math

def divideIntoParts(amount, denominations, filterZeroes = False):
    accumulator = amount
    result = []
    for denomination in denominations:
        # `a // b` stands for truncating division, same as `int(a / b)`
        # we create a tuple of denomination and count for easier display
        countInfo = (denomination, (accumulator // denomination))
        result.append(countInfo)
        # equivalent to `accumulator = accumulator % denomination`
        accumulator = int(math.fmod (accumulator, denomination))
    return filter(lambda item: (filterZeroes and item[1] > 0), result)

notes = [2000,500,100,50,20,10,5,2,1]
maxDenominationDigits = max(map(lambda x: len(str(x)), notes))

while True:
    amount = int(input("Enter the amount: "))
    dividedAmount = divideIntoParts(amount, notes, True)
    printed = False
    for denomination, count in dividedAmount:
        printed = True
        print("The number of ₹{:<{width}d} notes is {:d}".format(denomination, count, width = maxDenominationDigits))
    if not printed:
        print ("Sorry")
    if input("Repeat? Y/N: ") == 'N' == 'n':
        break
