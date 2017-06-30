notecount = [0,0,0,0,0,0,0,0,0]
notes = [2000,500,100,50,20,10,5,2,1]
# Cool Python Trivia (and painful gotcha) #1:
# `&` is the bitwise AND operator which operates on integers,
# not the logical AND operator which operates on booleans (which is `and` in Python and `&&` in C-like languages, e.g. Java).
# However, booleans in Python are also integers (0 = False, 1 = True), but integers are not booleans, 
# which is why one doesn't get an error if `&` is used in place of `and` in `if` conditions - it just misbehaves silently.
l = len(notes)
# Forgot reminders about proper prompts? e.g. end the prompt text with `: ` or a newline?
amount = int(input("Enter the amount"))
while (amount > 0):
	if (amount >= 2000):
		amount -= 2000
		notecount [0] += 1
	# Cool Python Trivia #2:
	# `x >= a and x < b` in Python can be written equivalently as `a <= x < b`.
	# Other reasonable variations of the comparison operators may also be used in the above format.
	# I leave a mix of both to illustrate that this actually works.
	elif (500 <= amount < 2000):
		amount -= 500
		notecount [1] += 1
	elif (100 <= amount < 500):
		amount -= 100
		notecount [2] += 1
	elif (50 <= amount < 100):
		amount -= 50
		notecount [3] += 1
	elif (20 <= amount < 50):
		amount -= 20
		notecount [4] += 1
	elif (amount >= 10 and amount < 20):
		amount -= 10
		notecount [5] += 1
	elif (amount >= 5 and amount < 10):
		amount -= 5
		notecount [6] += 1
	elif (amount >= 2 and amount < 5):
		amount -= 2
		notecount [7] += 1
	elif (amount >= 1 and amount < 2):
		amount -= 1
		notecount [8] += 1
for i in range(l):
	# Try string formatting using the `format` method for the below one,
	# refer `properDenominations.py` if you get stuck.
	print ("The no of ",notes[i],"rupee notes is ",notecount[i])
