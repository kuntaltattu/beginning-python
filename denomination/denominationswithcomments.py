notes = [2000,500,100,50,20,10,5,2,1]
l = len(notes)
amount = int(input("Enter the amount"))
for i in range(l):
	count = 0
	# The amount may not to be exactly divisible by all (especially larger) denominations, account for that.
	if (amount%notes[i]) == 0:
		count += int(amount/notes[i])
	print ("The no of ",notes[i]," rupee notes are ",count)
	amount -= notes[i] * count
