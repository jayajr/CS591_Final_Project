import pygame
from cs591Utilities import *
from math import *


def createSineWave(freq, ampl, pha, dur):
    out = list()
    for sample in range(floor(44100 * dur)):
        out.append( (2**15 - 1) * ampl * sin (freq * 2 * pi * sample/44100 + pha))
    return out

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

def createBellWave(f1, duration=1):
    f2=f1*2.8
    index=6.0
    A=0.1
    S=0.1
    L=1.0
    R=duration-0.2
    H=0.5

    a = floor(44100*A)
    A1 = 1    
    A2 = f2 * index
    SR = 44100
    indexControl = index/(SR*(A+S+R));    
    
    duration = A + S + R
    
    wav = createSineWave(f1, 1.0, 0, A+S+R)
    
    phase = 0.0
    newFreq = f1
    for sample in range( floor(duration * SR ) ):
        if (sample > a):
            freqIncr = A2 * np.sin(2 * np.pi * f2 * sample / SR)  # modulating signal
            oldFreq = newFreq
            newFreq = f1 + freqIncr
            phase +=  2 * pi * (sample / SR) * (oldFreq - newFreq)      
            wav[sample] = A1 * MAX_AMP * np.sin(2 * np.pi * newFreq * sample / SR + phase)
        else:
            continue
        index -= indexControl
        
    applyASR(wav, A, S, L, R, H)

    return wav


def initLibrarySine():
	X = createSineWave(440, 0.1, 1, 1)
	writeWaveFile("s0.wav", X)

	X = createSineWave(440*9/8, 0.1, 1, 1)
	writeWaveFile("s1.wav", X)

	X = createSineWave(440*5/4, 0.1, 1, 1)
	writeWaveFile("s2.wav", X)

	X = createSineWave(440*3/2, 0.1, 1, 1)
	writeWaveFile("s3.wav", X)

	X = createSineWave(440*5/3, 0.1, 1, 1)
	writeWaveFile("s4.wav", X)

	X = createSineWave(440*2, 0.1, 1, 1)
	writeWaveFile("s5.wav", X)

	X = createSineWave(440*2*9/8, 0.1, 1, 1)
	writeWaveFile("s6.wav", X)

	X = createSineWave(440*2*5/4, 0.1, 1, 1)
	writeWaveFile("s7.wav", X)

	X = createSineWave(440*2*3/2, 0.1, 1, 1)
	writeWaveFile("s8.wav", X)


	library = []

	zero = pygame.mixer.Sound('s0.wav')
	one = pygame.mixer.Sound('s1.wav')
	two = pygame.mixer.Sound('s2.wav')
	three = pygame.mixer.Sound('s3.wav')
	four = pygame.mixer.Sound('s4.wav')
	five = pygame.mixer.Sound('s5.wav')
	six = pygame.mixer.Sound('s6.wav')
	seven = pygame.mixer.Sound('s7.wav')
	eight = pygame.mixer.Sound('s8.wav')

	library.append(zero)
	library.append(one)
	library.append(two)
	library.append(three)
	library.append(four)
	library.append(five)
	library.append(six)
	library.append(seven)
	library.append(eight)

	return library;


def initLibraryBell():

	X = createBellWave(440/2)
	writeWaveFile("b0.wav", X)

	X = createBellWave(440*9/8/2)
	writeWaveFile("b1.wav", X)

	X = createBellWave(440*5/4/2)
	writeWaveFile("b2.wav", X)

	X = createBellWave(440*3/2/2)
	writeWaveFile("b3.wav", X)

	X = createBellWave(440*5/3/2)
	writeWaveFile("b4.wav", X)

	X = createBellWave(440*2/2)
	writeWaveFile("b5.wav", X)

	X = createBellWave(440*2*9/8/2)
	writeWaveFile("b6.wav", X)

	X = createBellWave(440*2*5/4/2)
	writeWaveFile("b7.wav", X)

	X = createBellWave(440*2*3/2/2)
	writeWaveFile("b8.wav", X)


	library = []

	zero = pygame.mixer.Sound('b0.wav')
	one = pygame.mixer.Sound('b1.wav')
	two = pygame.mixer.Sound('b2.wav')
	three = pygame.mixer.Sound('b3.wav')
	four = pygame.mixer.Sound('b4.wav')
	five = pygame.mixer.Sound('b5.wav')
	six = pygame.mixer.Sound('b6.wav')
	seven = pygame.mixer.Sound('b7.wav')
	eight = pygame.mixer.Sound('b8.wav')

	library.append(zero)
	library.append(one)
	library.append(two)
	library.append(three)
	library.append(four)
	library.append(five)
	library.append(six)
	library.append(seven)
	library.append(eight)

	return library;