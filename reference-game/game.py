import sys, random, pygame
pygame.init()

scale = 6
size = screen_width, screen_height = 160 * scale, 120 * scale
background = pygame.image.load("bg_raw.png")
background = pygame.transform.scale(background, (160 * scale, 120 * scale))

white = 255,255,255
black = 0,0,0
green = 0,255,0

screen = pygame.display.set_mode(size)

#--------------Sprites Classes---------------------------

class giles(pygame.sprite.Sprite):
    def __init__(self ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("giles_trimmed.png")
        self.image = pygame.transform.scale(self.image, (15 * scale, 20 * scale))
        self.rect = self.image.get_rect()

class A(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("a.png")
        self.image = pygame.transform.scale(self.image, (7 * scale, 7 * scale))
        self.rect = self.image.get_rect()
    def update(self):
        if ticks <= 20000:
            self.rect.x -= 10
        if ticks > 20000 and ticks <= 40000:
            self.rect.x -= 20
        if ticks > 40000 and ticks <= 60000:
            self.rect.x -= 30
        if ticks > 60000:
            self.rect.x -= 60

class F(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("f.png")
        self.image = pygame.transform.scale(self.image, (7 * scale, 7 * scale))
        self.rect = self.image.get_rect()
    def update(self):
        if ticks <= 20000:
            self.rect.x -= 10
        if ticks > 20000 and ticks <= 40000:
            self.rect.x -= 20
        if ticks > 40000 and ticks <= 60000:
            self.rect.x -= 30
        if ticks > 60000:
            self.rect.x -= 60
            
class player(pygame.sprite.Sprite):
    def __init__(self, char):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(str(char))
        self.image = pygame.transform.scale(self.image, (12 * scale, 18 * scale))
        self.rect = self.image.get_rect()

class heart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("heart.png")
        self.image = pygame.transform.scale(self.image, (6 * scale, 6 * scale))
        self.rect = self.image.get_rect()

#----------Character Select--------------------------------

char_select = []
char_loc = []

arslan = pygame.image.load("arslan_trimmed.png")
arslan = pygame.transform.scale(arslan, (12 * scale, 18 * scale))
arslanrect = screen_width / 3, screen_height / 5
char_select.append(arslan)
char_loc.append(arslanrect)

jess = pygame.image.load("jess_trimmed.png")
jess = pygame.transform.scale(jess, (12 * scale, 18 * scale))
jessrect = 3 * screen_width / 5, screen_height / 5
char_select.append(jess)
char_loc.append(jessrect)

khai = pygame.image.load("khai_trimmed.png")
khai = pygame.transform.scale(khai, (12 * scale, 18 * scale))
khairect = screen_width / 3, 3 * screen_height / 5
char_select.append(khai)
char_loc.append(khairect)

jerome = pygame.image.load("jerome_trimmed.png")
jerome = pygame.transform.scale(jerome, (12 * scale, 18 * scale))
jeromerect = 3 * screen_width / 5, 3 * screen_height / 5
char_select.append(jerome)
char_loc.append(jeromerect)

#----------Score Stuff-------------------------------------
smallfont = pygame.font.SysFont("comicsansms", 5 * scale)

def score_function(score):
    text = smallfont.render("Score: "+str(score), True, white)
    screen.blit(text, [0 ,screen_height - (7 * scale)])

#-----------Sprite Initialization---------------------------
    
a_list = pygame.sprite.Group()
f_list = pygame.sprite.Group()
heart_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

giles1 = giles()
giles2 = giles()
all_sprites_list.add(giles1)
all_sprites_list.add(giles2)

heart1 = heart()
heart1.rect.x = (4 * screen_width / 10)
heart1.rect.y = 0
heart_list.add(heart1)
all_sprites_list.add(heart1)

heart2 = heart()
heart2.rect.x = (5 * screen_width / 10)
heart2.rect.y = 0
heart_list.add(heart2)
all_sprites_list.add(heart2)

heart3 = heart()
heart3.rect.x = (6 * screen_width / 10)
heart3.rect.y = 0
heart_list.add(heart3)
all_sprites_list.add(heart3)

#--------------Player Position----------------------------

pos = [x_coord, y_coord] = 0,0

speed = [x_speed, y_speed] = 0,0


#--------------Miscellaneous------------------------------
score = 1
time = 0
last_add_ticks = 0
ticks2 = 0
lives = 3
intro = True
done = False

#---------------Main Program Loop ----------------------#

    #-----------Main Menu--------------------------------

while intro == True:
    
        #-------Select Character on keypress-------------
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                char = "arslan_trimmed.png"
                player = player(char)
                all_sprites_list.add(player)
                intro = False
            if event.key == pygame.K_2:
                char = "jess_trimmed.png"
                player = player(char)
                all_sprites_list.add(player)
                intro = False
            if event.key == pygame.K_3:
                char = "khai_trimmed.png"
                player = player(char)
                all_sprites_list.add(player)
                intro = False
            if event.key == pygame.K_4:
                char = "jerome_trimmed.png"
                player = player(char)
                all_sprites_list.add(player)
                intro = False
            if event.key == pygame.K_5:
                char = "giles_trimmed.png"
                player = player(char)
                all_sprites_list.add(player)
                intro = False
        
            
    
        #-------Text on Screen---------------------------
                
    screen.fill(green)

    texts = []
    
    main_text = smallfont.render("Choose a Character (1,2,3,4 to start)", True, white)

    arslan_text = smallfont.render("1" , True, white)
    texts.append(arslan_text)
    
    jess_text = smallfont.render("2", True, white)
    texts.append(jess_text)
    
    khai_text = smallfont.render("3", True, white)
    texts.append(khai_text)
    
    jerome_text = smallfont.render("4", True, white)
    texts.append(jerome_text)
    


        #-------Menu - Draw Stuff Here-------------------
    screen.blit(background, [0,0])
    screen.blit(main_text, [ 42 * scale , screen_height / 2 - 5 * scale])
    screen.blit(arslan_text, [(screen_width / 3) + 5 * scale, (screen_height / 5) + 18 * scale])
    screen.blit(jess_text, [(3 * screen_width / 5) + 5 * scale, (screen_height / 5) + 18 * scale])
    screen.blit(khai_text, [(screen_width / 3) + 5 * scale, (3 * screen_height / 5) + 18 * scale])
    screen.blit(jerome_text, [(3 * screen_width / 5) + 5 * scale, (3 * screen_height / 5) + 18 * scale])
    
    for i in range(4):
        screen.blit(char_select[i], char_loc[i])

    
    pygame.display.flip()

    #-----------Game Start-------------------------------

clock = pygame.time.Clock()

if intro == False:
    while done == False:


        #-----------Event Management---------------------
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -10
                if event.key == pygame.K_RIGHT:
                    x_speed = 10
                if event.key == pygame.K_UP:
                    y_speed = -10
                if event.key == pygame.K_DOWN:
                    y_speed = 10
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = 0
                if event.key == pygame.K_UP:
                    y_speed = 0
                if event.key == pygame.K_DOWN:
                    y_speed = 0

        #----------Game Logic-----------------------------
        screen.fill(white)
            #------Lives----------------------------------

        if lives == 2:
            heart3.kill()

        if lives == 1:
            heart2.kill()

        if lives == 0:
            heart1.kill()
            done = True
            
            #----------Time Stuff-------------------------
        clock.tick(60)

        ticks = pygame.time.get_ticks()
        if ticks < 60000:
            if ticks - last_add_ticks > 1500:
            
                last_add_ticks = ticks
            
                a = A()
                a.rect.x = (screen_width - 5)
                a.rect.y = random.randrange(screen_height - 5)
                a_list.add(a)                    
                f = F()
                f.rect.x = (screen_width - 5)
                f.rect.y = random.randrange(screen_height - 5)
                f_list.add(f)
                
                all_sprites_list.add(a)
                all_sprites_list.add(f)

                giles1.rect.x = a.rect.x - (15 * scale)
                giles1.rect.y = a.rect.y - (5 * scale)

                giles2.rect.x = f.rect.x - (15 * scale)
                giles2.rect.y = f.rect.y - (5 * scale)
                
                
        if ticks >= 65000:
            if ticks - last_add_ticks > 100:
            
                last_add_ticks = ticks
            
                a = A()
                a.rect.x = (screen_width - (7 * scale))
                a.rect.y = random.randrange(screen_height - (7 * scale))
                a_list.add(a)
                    
                f = F()
                f.rect.x = (screen_width - (7 * scale))
                f.rect.y = random.randrange(screen_height - (7 * scale))
                f_list.add(f)

                all_sprites_list.add(a)
                all_sprites_list.add(f)

        if ticks - ticks2 > 200:
           ticks2 = ticks
           a_list.update()
           f_list.update()

           
            #---------Moving Stuff------------------------

        x_coord += x_speed
        y_coord += y_speed
        
        player.rect.x = (x_coord)
        player.rect.y = (y_coord)

        if x_coord < 0:
            x_coord = 0
        if x_coord > screen_width - (12 * scale):
            x_coord = screen_width - (12 * scale)
        if y_coord < 0:
            y_coord = 0
        if y_coord > screen_height - (18 * scale):
            y_coord = screen_height - (18 * scale)

            #---------Collision Management-----------------
        
        a_hit_list = pygame.sprite.spritecollide(player, a_list, True)
        f_hit_list = pygame.sprite.spritecollide(player, f_list, True)

        for a in a_hit_list:
            score += 1
            print( score - 1 )

        for f in f_hit_list:
            lives -= 1
            print("You have ", lives, " lives remaining", "\n", end="")

        #-----------Draw Stuff Here----------------------

        screen.blit(background, [0,0])
        
        all_sprites_list.draw(screen)

        score_function(score-1)
        
        pygame.display.flip()

    pygame.quit()
       
