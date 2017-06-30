notes = [2000,500,100,50,20,10,5,2,1]
l = len(notes)
while True:
	amount = int(input("Enter the amount"))
	for i in range(l):
		count = 0
		if (amount%notes[i]) == 0:
			count += int(amount/notes[i])
		print ("The no of ",notes[i]," rupee notes are ",count)
		amount -= notes[i] * count
