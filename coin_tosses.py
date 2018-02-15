import random


def coinToss(num):
	print "Starting the program..."
	#set the heads and tails to zero
	heads = 0;
	tails = 0;

	#loop from one to num
	for x in range(1,num+1):
		#start building the output string 
		message = "Attempt #" + str(x) + ": Throwing a coin... "

		#flip the coin
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



