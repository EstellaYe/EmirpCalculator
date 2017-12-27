####
#	Joseph Allen jallen6@ramapo.edu
#	CMPS 367-01 SI 17
#	Homework 1
#
#	Assignment: Calculate the first N emirp numbers, where N is a positive number that the user provides as input. 
#
#	Status:
#		Program completes task as described
#
#	Notes: 
#		The isPrime function needed to have special case handling for the number 4 due to the range being exclusive. While it causes an extra check on all calls to the function, it is a constant time addition.
#		
#		The reason I choose to use a printBuffer variable and function instead of using print() with no linebreak at the end was that it allowed me more control over how the data was printed. Which was a little overkill
#			for this assignment, however it would allow for much more dynamic printouts if that were to be needed. In addition, I choose to format all numbers to have three digits. That could be easily changed to be empty
#			spaces before or after the number, but I found the leading zeros looked nicer in the output columns. 
#
#		Program assumes input will be able to be parsed as an int, but does validate that it is number that meets the parameters. 
#
# 		



#Required Fuction
#Function takes a value and checks if it is prime, and returns a boolean
def isPrime(value):

	#If 4, return false
	if value == 4:
		return False

	#loop through all numbers between 2 and half of input, seeing if its divisible.
	for i in range(2, value // 2):
		if value % i == 0:
			return False
	
	#If loop is exited, that means it is prime	
	return True
	
	
#Required Function
#Function takes in a number, reverses the order of digits, and returns an int
def reverse(value):
	#Cast to string, and intialize the reversedString variable
	value = str(value)
	reversedString = ""
	
	#Loop backwards through value storing the current char into reversedString
	for i in value[::-1]:
		reversedString += i
		
	#return it as an int	
	return int(reversedString)
	
#Non-Required function
#This function is responsible for taking a number that meets all requirements, and formats it ready to be printed
#It assumes all output will be done up to three digit numbers, so it adds leading zeros to that point, and then 4 spaces after the number	
def updatePrintBuffer(value):

	#Logic to see how many zeros are needed to make the number 3 digits
	if value < 10:
		leadingZeros = "00"
	elif value < 100:
		leadingZeros = "0"
	else:
		leadingZeros = ""
		
	#The whitespaces after all numbers
	whiteSpace = "\t" 
	
	#Concatinate into one string and return
	toReturn = leadingZeros + str(value) + whiteSpace
	return toReturn
	
#
###Main Program Flow starts here
#	

#Flag for input loop
gettingInput = True

#Get a postive number from the user
while gettingInput:
	emirpsToFind = int(input("Please enter a postive number:  "))
	
	if emirpsToFind <= 0:
		print("Input is not valid")
	else:
		gettingInput = False

#intialize all variables		
emirpsFound = 0 #counter for found
checking = 2 #counter for what number we are checking, starting at 2, the first prime
numbersInPrintBuffer = 0 #counter for amount of numbers currently waiting to be printed
printBuffer = "" #Intialization of print buffer.

#While looking for all the emirps user requested
while emirpsFound < emirpsToFind:
	#check if current number is prime
	currentIsPrime = isPrime(checking)
	if currentIsPrime:
		#if current is prime, check if its reverse is prime
		reverseIsPrime = isPrime(reverse(checking))
		if reverseIsPrime:
			#If both are true, then number is an emirp
			#add to counter, and enqueue into print buffer
			emirpsFound += 1
			printBuffer += updatePrintBuffer(checking)
			numbersInPrintBuffer += 1
			
			#If the print buffer is full and need to be printed
			if numbersInPrintBuffer >= 5:
				#Print the buffer, and reset
				print(printBuffer)
				printBuffer = ""
				numbersInPrintBuffer = 0
	#Add to next number to count
	checking +=1
	
#If anything is in buffer when loop finishes, print it out
if numbersInPrintBuffer > 0:
	print(printBuffer)
	#Reset buffer
	printBuffer = ""
	numbersInPrintBuffer = 0
