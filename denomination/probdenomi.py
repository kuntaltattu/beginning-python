while True:
	notecount = [0,0,0,0,0,0,0,0,0]
	notes = [2000,500,100,50,20,10,5,2,1]
	l = len(notes)
	amount = int(input("Enter the amount"))
	while (amount >= 0):
		if (amount >= 2000):
			amount -= 2000
			notecount[0] += 1
		elif (amount >= 500 & amount < 2000):
			amount -= 500
			notecount [1] += 1
		elif (amount >= 100 & amount < 500):
			amount -= 100
			notecount [2] += 1
		elif (amount >=50 & amount <100):
			amount -= 50
			notecount [3] += 1
		elif (amount >= 20 & amount <50):
			amount -= 20
			notecount [4] += 1
		elif (amount >= 10 & amount <20):
			amount -= 10
			notecount [5] += 1
		elif (amount >=5 & amount <10):
			amount -= 5
			notecount [6] += 1
		elif (amount >=2 & amount <5):
			amount -= 2
			notecount [7] += 1
		elif (amount >=1 & amount <2):
			amount -= 1
			notecount [8] += 1
	for i in range(l):
		print ("The no of ",notes[i],"rupee notes is ",notecount[i])

		
