import time
from cs591Utilities import *

'''
Constructs a signal given a list of tuples signifying key presses
'''
def constructSignal(beatList, duration=5):

	signal = [0] * SR * duration

	for i in range(len(beatList)):

		# get values from tuple
		downKey = beatList[i][0]
		downTime = beatList[i][1]
		upDown = beatList[i][2]

		# only make a beat if it is a down action (beginning of a beat)
		if(upDown == 1):

			keyUp = findKeyUp(i, downKey, beatList)

			upKey = keyUp[0]
			upTime = keyUp[1]

			beatDuration = upTime - downTime

			# signal with an ASR filter applied
			beat = getBeat(downKey, beatDuration)

			signal = addBeatToSignal(beat, downTime, signal)


	# write to wav file
	writeWaveFile("recordedSignal.wav", signal)

	return signal


'''
Finds first instance of a key release of a given key
'''
def findKeyUp(downIndex, downKey, beatList):

	for i in range(downIndex, len(beatList)):

		key = beatList[i][0]
		time = beatList[i][1]
		upDown = beatList[i][2]

		# if it is same key and is the up action
		if(downKey == key and upDown == 0):
			return beatList[i]


'''
Makes a signal given the key and apply ASR fileter
'''
def getBeat(key, duration):

	if(key == 0):
		freq = 440
	elif(key == 1):
		freq = 500
	elif(key == 2):
		freq = 30
	elif(key == 3):
		freq = 40
	elif(key == 4):
		freq = 50
	elif(key == 5):
		freq = 60
	elif(key == 6):
		freq = 70
	elif(key == 7):
		freq = 80
	else:
		freq = 90

	spectrum = (freq, 1.0, 0)

	X = makeSignal([spectrum], duration)


	A = .1
	S = (duration - A) * .2
	R = (duration - A - S) * .8
	L = 1
	H = R * .3

	return applyASR(X, A, S, L, R, H)


def applyASR(X,A,S,L,R,H):
	Y = [0] * len(X) 
	A = A * SR      # convert seconds to sample numbers
	S = S * SR
	R = R * SR    
	for k in range(len(X)):
		if (k < A):
			Y[k] = int(X[k]*L*k/A)
		elif (k < A+S):
			Y[k] = int(X[k]*L)
		elif (k < A+S+R):
			Y[k] = int(X[k]*(L*(2.0**(-(k-A-S)/(SR*H)))))
		else:
			Y[k] = 0
	return Y


def addBeatToSignal(beat, offset, signal):

	sampleOffset = offset * SR

	for i in range(sampleOffset, len(beat) + sampleOffset):

		signal[i] = signal[i] + beat[i-sampleOffset]


	return signal



'''
Will modify the pitch of a given singal by some scale
and will return that newly modified beat for use
'''
def modifyPitch(beat, scale):

	pass



'''
Tests
'''
constructSignal([(0, 0, 1), (0, 2, 0), (1, 3, 1), (1, 5, 0)])
