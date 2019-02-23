i = 0
with open('tabId.csv', r) as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	while reader:
		tabId[i] = reader
		i+=1
		print tabIdS