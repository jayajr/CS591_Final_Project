import pygame, time, os
from pygame.locals import *
from cs591Utilities import *
from audioProcessing import *
from math import pi,sin,floor

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
flags = DOUBLEBUF

white = 255,255,255
black = 0,0,0
green = 0,255,0

scale = 6
size = screen_width, screen_height = 160 * scale, 120 * scale
background = pygame.image.load("square.jpg")
background = pygame.transform.scale(background, (160 * scale, 120 * scale))

gameDisplay = pygame.display.set_mode(size, flags)
gameDisplay.set_alpha(None)
pygame.display.set_caption('Launchpad-Lite')

clock = pygame.time.Clock()

# ----- Library -----

def createSineWave(freq, ampl, pha, dur):
    out = list()
    for sample in range(floor(44100 * dur)):
        out.append( (2**15 - 1) * ampl * sin (freq * 2 * pi * sample/44100 + pha))
    return out

X = createSineWave(440, 0.1, 1, 1)
writeWaveFile("0.wav", X)

X = createSineWave(440*9/8, 0.1, 1, 1)
writeWaveFile("1.wav", X)

X = createSineWave(440*5/4, 0.1, 1, 1)
writeWaveFile("2.wav", X)

X = createSineWave(440*3/2, 0.1, 1, 1)
writeWaveFile("3.wav", X)

X = createSineWave(440*5/3, 0.1, 1, 1)
writeWaveFile("4.wav", X)

X = createSineWave(440*2, 0.1, 1, 1)
writeWaveFile("5.wav", X)

X = createSineWave(440*2*9/8, 0.1, 1, 1)
writeWaveFile("6.wav", X)

X = createSineWave(440*2*5/4, 0.1, 1, 1)
writeWaveFile("7.wav", X)

X = createSineWave(440*2*3/2, 0.1, 1, 1)
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


# ----- Button Display Class -----
class button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("square.jpg")
        self.image = pygame.transform.scale(self.image, (floor(screen_width/6), floor(screen_height/6)))
        self.rect = self.image.get_rect()


# ----- Class Init -----
b_list = pygame.sprite.Group()

b_1 = button()
b_1.rect.x = screen_width/5
b_1.rect.y = screen_height/6
b_list.add(b_1)

b_2 = button()
b_2.rect.x = screen_width/5*2
b_2.rect.y = screen_height/6
b_list.add(b_2)

b_3 = button()
b_3.rect.x = screen_width/5*3
b_3.rect.y = screen_height/6
b_list.add(b_3)

b_q = button()
b_q.rect.x = screen_width/5
b_q.rect.y = screen_height/6*2
b_list.add(b_q)

b_w = button()
b_w.rect.x = screen_width/5*2
b_w.rect.y = screen_height/6*2
b_list.add(b_w)

b_e = button()
b_e.rect.x = screen_width/5*3
b_e.rect.y = screen_height/6*2
b_list.add(b_e)

b_a = button()
b_a.rect.x = screen_width/5
b_a.rect.y = screen_height/6*3
b_list.add(b_a)

b_s = button()
b_s.rect.x = screen_width/5*2
b_s.rect.y = screen_height/6*3
b_list.add(b_s)

b_d = button()
b_d.rect.x = screen_width/5*3
b_d.rect.y = screen_height/6*3
b_list.add(b_d)

b_z = button()
b_z.rect.x = screen_width/5
b_z.rect.y = screen_height/6*4
b_list.add(b_z)

b_x = button()
b_x.rect.x = screen_width/5*2
b_x.rect.y = screen_height/6*4
b_list.add(b_x)

b_c = button()
b_c.rect.x = screen_width/5*3
b_c.rect.y = screen_height/6*4
b_list.add(b_c)

# ----- Miscellaneous -----
SR = 44100
done = False
recording = False
record_time = -1

Q = [] # List of tuples [(KEY, Time, Up/Down), (KEY,Time,Up/Down)] etc
S = [0] * SR * 5 # 5 second blank signal

roundedrect1 = 0, 0, scale, scale

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

                if event.key == pygame.K_3:
                    playback.play()
        
        
        # Recording
        if recording is True:
            event_time = time.time()
            if event.type == pygame.KEYDOWN:
                # Stop Recording
                if event.key == pygame.K_2:
                    recording = False
                    #for i in range(len(Q)):
                    #    print(Q[i])

                    constructSignal(Q)
                    playback = pygame.mixer.Sound("recordedSignal.wav")
                    #playback.play()
                    Q=[]
                    
                # Launch Sounds
                if event.key == pygame.K_q:
                    Q.append((0, event_time - record_time, 1))
                    library[0].play(loops=-1)
                if event.key == pygame.K_w:
                    Q.append((1, event_time - record_time, 1))
                    library[1].play(loops=-1)
                if event.key == pygame.K_e:
                    Q.append((2, event_time - record_time, 1))
                    library[2].play(loops=-1)
                if event.key == pygame.K_a:
                    Q.append((3, event_time - record_time, 1))
                    library[3].play(loops=-1)
                if event.key == pygame.K_s:
                    Q.append((4, event_time - record_time, 1))
                    library[4].play(loops=-1)
                if event.key == pygame.K_d:
                    Q.append((5, event_time - record_time, 1))
                    library[5].play(loops=-1)
                if event.key == pygame.K_z:
                    Q.append((6, event_time - record_time, 1))
                    library[6].play(loops=-1)
                if event.key == pygame.K_x:
                    Q.append((7, event_time - record_time, 1))
                    library[7].play(loops=-1)
                if event.key == pygame.K_c:
                    Q.append((8, event_time - record_time, 1))
                    library[8].play(loops=-1)
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    Q.append((0, event_time - record_time, 0))
                    library[0].stop()
                if event.key == pygame.K_w:
                    Q.append((1, event_time - record_time, 0))
                    library[1].stop()
                if event.key == pygame.K_e:
                    Q.append((2, event_time - record_time, 0))
                    library[2].stop()
                if event.key == pygame.K_a:
                    Q.append((3, event_time - record_time, 0))
                    library[3].stop()
                if event.key == pygame.K_s:
                    Q.append((4, event_time - record_time, 0))
                    library[4].stop()
                if event.key == pygame.K_d:
                    Q.append((5, event_time - record_time, 0))
                    library[5].stop()
                if event.key == pygame.K_z:
                    Q.append((6, event_time - record_time, 0))
                    library[6].stop()
                if event.key == pygame.K_x:
                    Q.append((7, event_time - record_time, 0))
                    library[7].stop()
                if event.key == pygame.K_c:
                    Q.append((8, event_time - record_time, 0))
                    library[8].stop()
            
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    gameDisplay.blit(background, [0,0])  
    b_list.draw(gameDisplay)
    pygame.display.flip()

        #end event type
    #end for event in pygame.event.get
#end while done