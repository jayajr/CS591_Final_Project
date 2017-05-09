import time
from cs591Utilities import *
from math import floor
from scipy.interpolate import interp1d

'''
Constructs a signal given a list of tuples signifying key presses
'''
def constructSignal(beatList, ASR = False, pitch = False, pitchF = 1.0):

	signal = [0] * SR * 5

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
			beat = getBeat(downKey, beatDuration, ASR, pitch, pitchF)

			signal = addBeatToSignal(beat, downTime, signal)


	# write to wav file
	for i in range(len(signal)):
		signal[i] /= 2

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
def getBeat(key, duration, ASR, pitch, pitchF):

	if(key == 0):
		freq = 440
	elif(key == 1):
		freq = 440*9/8
	elif(key == 2):
		freq = 440*5/4
	elif(key == 3):
		freq = 440*3/2
	elif(key == 4):
		freq = 440*5/3
	elif(key == 5):
		freq = 440*2
	elif(key == 6):
		freq = 440*2*9/8
	elif(key == 7):
		freq = 440*2*5/4
	else:
		freq = 440*2*3/2

	spectrum = (freq, 1.0, 0)

	X = makeSignal([spectrum], duration)

	if ASR is True:
		A = .1
		S = (duration - A) * .2
		R = (duration - A - S) * .8
		L = 1
		H = R * .3

		X = applyASR(X, A, S, L, R, H)
	
	if pitch is True:
		X = modifyPitch(X, pitchF)

	return X


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

	sigSize = len(signal)
	beatSize = len(beat)
	sampleOffset = floor(offset * SR)
	
	if beatSize + sampleOffset > sigSize:
		A = [0]*beatSize*2
		signal.extend(A)

	for i in range(beatSize):
		signal[sampleOffset + i] += beat[i]


	return signal



'''
Will modify the pitch of a given singal by some scale
and will return that newly modified beat for use
'''
def modifyPitch(X, P):
    W = 100
    Wf = W + 5

    Xstretched = []

    for start in range(0,len(X)-W,W):
        Tf = range(start,start+Wf)   # sample nums for interpolation
        Tnew = np.arange(start,start+W, 1/P)   # interpolated sample points
        f = interp1d(Tf,X[start:start+Wf],kind='cubic') # must interpolate over extended window
        Z = [f(x) for x in Tnew]     # signal over interpolated points
        Xstretched.extend(Z)
           
    return Xstretched


'''
Tests
'''
#constructSignal([(0, 0.4141, 1), (0, 1.9232, 0), (1, 3.5, 1), (1, 4.32, 0)])
