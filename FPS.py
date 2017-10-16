## This program was deeloped to intake CSV files converte from Acq 
## then calculate T-scores for FPS probes

import math
import csv

## Initializing lists and variables by data type
## (trigger event and FPS values) for data matrix organization

def dataOrg():

	channelList = []
	fpsList = []

	## Open CSV file. 
	with open("DevonTest.csv") as csvfile:
		reader = csv.reader(csvfile, delimiter = "\t")

		## Go through each row and convert values into
		## readable integers
		for row in reader:
			rowS = str(row)
			
			newRow=rowS.split("t")

			##c reate a list of the FPS channel values
			## o be used later for appending trigger indeces
			fpsTrigger = newRow[9]
			realFT = int(fpsTrigger[:-1])
			channelList.append(realFT)

			## do the same thing for FPS physio values, to be
			## pulled later with the realFT indeces
			fpsChannel = newRow[15]
			realFC = float(fpsChannel[:-1])
			fpsList.append(realFC)

		return channelList, fpsList

## Look for trigger values and append their position
## in a new list

def trackFPS(channelL):
	tracker = []
	x=0

	for i in channelL:
		x+=1
		if i == 5:
			tracker.append(x)

	## split the tracked indexed values into 1 second samples
	## This creates a new list of the initial FPS channel trigger
	## for each startle event
	
	trackYa = tracker[0::1000]

	return trackYa

def calAverage(fpsYay, trackYay):
	averageList = []
	maxList = []
	preSP = []
	maxSP=[]
	s=0
	m=0


	## Go back .5 seconds from each startle probe event trigger
	## and append the average of that second to new list

	for q in trackYay:
		for l in range(499):

			preSP.append(fpsYay[q-l])
			
		averageFPS = sum(preSP)/len(preSP)
		averageList.append(averageFPS)

	## Go forward 1.2 seconds from each startle probe even trigger
	## and append the maximum FPS value to new list

	for v in trackYay:
		m+=1200

		for b in range(1200):

			maxSP.append(fpsYay[v+b])
		newMax = (maxSP[s:m])
		s+=1200
		maxStartle = max(newMax)

		maxList.append(maxStartle)

	return averageList, maxList

## Caculate the difference between the maxiumum FPS
## and mean baseline and append to new list

def finalCalc(averageYay, maxYay):
		m=0
		yay=[]

		for g in range(24):

			final=maxYay[g]-averageYay[g]
			
			m+=1
			print (final)
			yay.append(final)

		return (yay)


def fpsTrigg():

	beginChannel, beginFPS = dataOrg()
	beginTracker = trackFPS(beginChannel)
	#print (beginTracker)
	averageFin, maxFin = calAverage(beginFPS, beginTracker)
	#print (averageFin, maxFin)
	finalYay = finalCalc(averageFin, maxFin)
	#print (finalYay)

fpsTrigg()



