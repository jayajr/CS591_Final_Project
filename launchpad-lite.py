import pygame, time

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
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

# ----- Library -----
library = []
trumpet = pygame.mixer.Sound('Trumpet.wav')
library.append(trumpet)



# ----- Miscellaneous -----
SR = 44100
done = False
recording = True
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
               if event.key == pygame.K_r:
                   recording = True
                   record_time = time.time()
        
        
        # Recording
        if recording is True:
            event_time = time.time()
            if event.type == pygame.KEYDOWN:
                # Stop Recording
                if event.key == pygame.K_r:
                    recording = False
                    
                # Launch Sounds
                if event.key == pygame.K_q:
                    Q.append([0, event_time - record_time, 1])
                    library[0].play()
                if event.key == pygame.K_w:
                    Q.append([1, event_time - record_time, 1])
                if event.key == pygame.K_e:
                    Q.append([2, event_time - record_time, 1])
                if event.key == pygame.K_a:
                    Q.append([3, event_time - record_time, 1])
                    pygame.mixer.music.load('Trumpet.wav')
                if event.key == pygame.K_s:
                    Q.append([4, event_time - record_time, 1])
                if event.key == pygame.K_d:
                    Q.append([5, event_time - record_time, 1])
                if event.key == pygame.K_z:
                    Q.append([6, event_time - record_time, 1])
                if event.key == pygame.K_x:
                    Q.append([7, event_time - record_time, 1])
                if event.key == pygame.K_c:
                    Q.append([8, event_time - record_time, 1])
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    Q.append([0, event_time - record_time, 0])
                    library[0].stop()
                if event.key == pygame.K_w:
                    Q.append([1, event_time - record_time, 0])
                if event.key == pygame.K_e:
                    Q.append([2, event_time - record_time, 0])
                if event.key == pygame.K_a:
                    Q.append([3, event_time - record_time, 0])
                if event.key == pygame.K_s:
                    Q.append([4, event_time - record_time, 0])
                if event.key == pygame.K_d:
                    Q.append([5, event_time - record_time, 0])
                if event.key == pygame.K_z:
                    Q.append([6, event_time - record_time, 0])
                if event.key == pygame.K_x:
                    Q.append([7, event_time - record_time, 0])
                if event.key == pygame.K_c:
                    Q.append([8, event_time - record_time, 0])
            
        print(Q)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)


        pygame.draw.rect(gameDisplay, green,(150,450,100,50))
        pygame.draw.rect(gameDisplay, black,(550,450,100,50))


        pygame.display.update()
        clock.tick(15)

