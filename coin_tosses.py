import random


def coinToss(num):
	print "Starting the program..."
	heads = 0;
	tails = 0;

	for x in range(1,num+1): 
		message = "Attempt #" + str(x) + ": Throwing a coin... "
		if round(random.random()) == 0: 
			heads += 1 
			message += "It's a head!"
		else: 
			tails += 1
			message += "It's a tail!"
		message += " ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
		print message

	print "Ending the program, thank you!"


coinToss(5000)



