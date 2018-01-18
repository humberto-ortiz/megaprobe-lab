import json
import sys
import collections

FILE = sys.argv[1]


#Space is how much space there is amoung each column
maxFields = 13
maxResults = 10

def main():
	print "Getting the data into a Json from %s" % FILE
	f = open(FILE, 'r')
	f = f.read()
	b = json.loads(f)
	
	dataName = str(b.keys()[0])
	#Get the amount of fields in the json
	lengthData = 0
	for x in range(len(b)):
		lengthData = len(b.values()[x])

	lenghtRows = len(b[dataName][0].keys())
	# print lenghtRows
	
	ans = ""
	getOut = ""
	while ans != "e":
		ans = input("Would you like to display ALL the acquired data? y/n: Type e to exit. ")
		if ans == "y":
			print ""
			displayAllData(b,dataName,lengthData, lenghtRows)
		elif ans == "n":
			print ""
			displayChosenData(b,dataName,lengthData,lenghtRows)
		elif ans == "e":
			print "Exiting"
		else: 
			print "Error: choice not aviliable. Please write y/n accordinly."


def displayAllData(b,dataName,lengthData, lenghtRows):
	space = " "
	saveKeys = []
	saveValues = []	
	fieldsNames = []
	#This is to display the Keys, which is going to be the first row
	for x in range(0, maxFields): 
		#To be able to display the columns well, we compare the length of the field's name with the amount of characters
		#in each of its value. If the len(keys[x] < than len(values[x])
		if (len(str(b[dataName][x].keys()[x])) < len(str(b[dataName][x].values()[x]))):
			#then the string space is going to multilied len(values[x]) - len(keys[x])
			space = space * (len(str(b[dataName][x].values()[x])) - len(str(b[dataName][x].keys()[x]))) 
			print b[dataName][x].keys()[x], space,
		else:
			#Else space will be equal to nothing
			space = ""
			print b[dataName][x].keys()[x], space, 
		space = " "
		fieldsNames.append(str(b[dataName][x].keys()[x]))
		# saveKeys.append(b[dataName][x].keys()[x]+ space) 
	print ""

	#Nested for loop for the results
	#Determines the amount of columns
	for i in range(0,lengthData):
		#Determines the amount of rows
		for j in range(0,lenghtRows):
			#Almost the same logic as before, if len(keys[j]) < len(values[j])
			if (len(str(b[dataName][i].keys()[j])) < len(str(b[dataName][i].values()[j]))):
				#There is no space between columns
				space = ""
				print b[dataName][i].values()[j], space,
			#However, if len(keys[j]) >= len(values[j]) 
			else:
				#Space is going to be the total of len(keys[j]) - len(values[i])
				space = space * (len(str(b[dataName][i].keys()[j])) - len(str(b[dataName][i].values()[j])))
				print b[dataName][i].values()[j], space, 
			space = " "	
			# saveValues.append(b[dataName][i].values()[j]+space)
		print ""

	# writeNewFile(saveKeys,saveValues)

def displayChosenData(b,dataName,lengthData, lenghtRows):
	columnChoice = ""
	newChoices = []
	space = " "
	i = 0
	saveKeys = []
	saveValues = []
	fieldsNames = []

	print "These are the aviliable fields in the data: "
	for t in range(0, lenghtRows):
		fieldsNames.append(str(b[dataName][t].keys()[t]))
		print fieldsNames[t]
	print ""
	print "Please write only  the name of the field whose results you wish to display. "
	print "If you're done writing your choices, write s (stop). "
	while columnChoice != "s":
		columnChoice = raw_input("Name of column you wish to display: ")
		if columnChoice in fieldsNames[0:(len(fieldsNames)-1)]: 
			newChoices.append(columnChoice)
		elif columnChoice == "s":
			pass
		else:
			print "That field doesn't seem to be avaliable. Make sure your wrote the wished field correctly. "
		i += 1	
	print ""

	#Chosen columns
	indField = 0

	for y in range (0, len(newChoices)):
		if (len(newChoices[y]) < len(str(b[dataName][y].get(newChoices[y])))):
			space = space * (len(str(b[dataName][y].get(newChoices[y]))) - len(newChoices[y])) 
			print newChoices[y], space, 
		else:
			print newChoices[y], space,
		saveKeys.append(newChoices[y] + space)	
		space = " "
	print ""
	
	for h in range(0,lengthData):
		for k in range(0,len(newChoices)):# 		
			if (len(newChoices[k])) < len(str(b[dataName][h].get(newChoices[k]))):
				#There is no space between columns
				print b[dataName][h].get(newChoices[k]), space, 
			else:
				#Space is going to be the total of len(keys[j]) - len(values[i])
				space = space * ((len(newChoices[k])) - len(str(b[dataName][h].get(newChoices[k]))))
				print b[dataName][h].get(newChoices[k]), space, 
			saveValues.append(str(b[dataName][h].get(newChoices[k])) + space)
			space = " "	
		print ""
	# writeNewFile(saveKeys,saveValues)
	
def writeNewFile(saveKeys,saveValues):
	# print saveValues
	writeFile = raw_input("Would you like to write this data into a txt file? y/n ") 
	if writeFile == "y":
		nameNewFile = raw_input("Okay, please choose a name for the file: ")
		nameNewFile = nameNewFile + ".txt"
		newFile = open(nameNewFile,"w")
		for keys in range(0,len(saveKeys)): 
			newFile.write(saveKeys[keys])
			if keys == (len(saveKeys) - 1):
				for val in range(0,len(saveValues)):
					newFile.write(saveValues[val])
				newFile.write("\n")
			

		newFile.close() 
	elif writeFile == "n":
		print "Fine, bye."
	else:
		print "I don't know that choice."
		

if __name__ == "__main__":
    main()

