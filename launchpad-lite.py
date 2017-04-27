import pygame, time
from cs591Utilities import *
from math import pi,sin,floor

pygame.init()
pygame.mixer.init()

white = 255,255,255
black = 0,0,0
green = 0,255,0

scale = 2
size = screen_width, screen_height = 160 * scale, 120 * scale
#background = pygame.image.load("bg_raw.png")
#background = pygame.transform.scale(background, (160 * scale, 120 * scale))

gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('Launchpad-Lite')

clock = pygame.time.Clock()

# ----- Library -----
def createSineWave(freq, ampl, pha, dur):
    out = list()
    for sample in range(floor(44100 * dur)):
        out.append( (2**15 - 1) * ampl * sin (freq * 2 * pi * sample/44100 + pha))
    return out

X = createSineWave(440, 1, 1, 1)
writeWaveFile("0.wav", X)

X = createSineWave(440*9/8, 1, 1, 1)
writeWaveFile("1.wav", X)

X = createSineWave(440*5/4, 1, 1, 1)
writeWaveFile("2.wav", X)

X = createSineWave(440*3/2, 1, 1, 1)
writeWaveFile("3.wav", X)

X = createSineWave(440*5/3, 1, 1, 1)
writeWaveFile("4.wav", X)

X = createSineWave(440*2, 1, 1, 1)
writeWaveFile("5.wav", X)

X = createSineWave(440*2*9/8, 1, 1, 1)
writeWaveFile("6.wav", X)

X = createSineWave(440*2*5/4, 1, 1, 1)
writeWaveFile("7.wav", X)

X = createSineWave(440*2*3/2, 1, 1, 1)
writeWaveFile("8.wav", X)


library = []

zero = pygame.mixer.Sound('0.wav')
one = pygame.mixer.Sound('1.wav')
two = pygame.mixer.Sound('2.wav')
three = pygame.mixer.Sound('3.wav')
four = pygame.mixer.Sound('4.wav')
five = pygame.mixer.Sound('5.wav')
six = pygame.mixer.Sound('6.wav')
seven = pygame.mixer.Sound('7.wav')
eight = pygame.mixer.Sound('8.wav')

library.append(zero)
library.append(one)
library.append(two)
library.append(three)
library.append(four)
library.append(five)
library.append(six)
library.append(seven)
library.append(eight)

# ----- Miscellaneous -----
SR = 44100
done = False
recording = False
record_time = -1

Q = [0] # List of lists [[KEY, Time, Up/Down], [KEY,Time,Up/Down]] etc
S = [0] * SR * 5 # 5 second blank signal


# ===== ===== Main Program Loop ===== =====
while not done:
    # Event Handling
    for event in pygame.event.get():
       # Not Recording        
        if recording is False:
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_1:
                   recording = True
                   record_time = time.time()
        
        
        # Recording
        if recording is True:
            event_time = time.time()
            if event.type == pygame.KEYDOWN:
                # Stop Recording
                if event.key == pygame.K_2:
                    recording = False
                    
                # Launch Sounds
                if event.key == pygame.K_q:
                    Q.append([0, event_time - record_time, 1])
                    library[0].play()
                if event.key == pygame.K_w:
                    Q.append([1, event_time - record_time, 1])
                    library[1].play()
                if event.key == pygame.K_e:
                    Q.append([2, event_time - record_time, 1])
                    library[2].play()
                if event.key == pygame.K_a:
                    Q.append([3, event_time - record_time, 1])
                    library[3].play()
                if event.key == pygame.K_s:
                    Q.append([4, event_time - record_time, 1])
                    library[4].play()
                if event.key == pygame.K_d:
                    Q.append([5, event_time - record_time, 1])
                    library[5].play()
                if event.key == pygame.K_z:
                    Q.append([6, event_time - record_time, 1])
                    library[6].play()
                if event.key == pygame.K_x:
                    Q.append([7, event_time - record_time, 1])
                    library[7].play()
                if event.key == pygame.K_c:
                    Q.append([8, event_time - record_time, 1])
                    library[8].play()
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    Q.append([0, event_time - record_time, 0])
                    library[0].stop()
                if event.key == pygame.K_w:
                    Q.append([1, event_time - record_time, 0])
                    library[1].stop()
                if event.key == pygame.K_e:
                    Q.append([2, event_time - record_time, 0])
                    library[2].stop()
                if event.key == pygame.K_a:
                    Q.append([3, event_time - record_time, 0])
                    library[3].stop()
                if event.key == pygame.K_s:
                    Q.append([4, event_time - record_time, 0])
                    library[4].stop()
                if event.key == pygame.K_d:
                    Q.append([5, event_time - record_time, 0])
                    library[5].stop()
                if event.key == pygame.K_z:
                    Q.append([6, event_time - record_time, 0])
                    library[6].stop()
                if event.key == pygame.K_x:
                    Q.append([7, event_time - record_time, 0])
                    library[7].stop()
                if event.key == pygame.K_c:
                    Q.append([8, event_time - record_time, 0])
                    library[8].stop()
            
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        gameDisplay.fill(white)
