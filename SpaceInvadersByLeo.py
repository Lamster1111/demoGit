import pygame
import Dude
from time import sleep
pygame.init()
#Set up for screen
x_size = 500
y_size = 600
win = pygame.display.set_mode((x_size,y_size))
pygame.display.set_caption("Space Invaders By Leo")


#Some Colour For Uses
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
White = (255,255,255)


win.fill(Black)
pygame.display.update()

#The Making Of A Hero
class player(object):
    def __init__(self, x, y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 7
        self.hitbox = (self.x,self.x+self.w,self.y,self.y+self.h)

    def draw(self,win):
        pygame.draw.rect(win,Green,(self.x,self.y,self.w,self.h))
        
    def hit(self):
        font = pygame.font.Font(None,46)
        win.blit(font.render("You Died",1,Red),(50,50))
        print(score)
            
    
        
#Bulllllllllllllllllllllllllllllllllllllllllllllllllllllllets        
class shoot(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 5
        self.h = 20
        self.speed = 10
        self.hp = 3
        self.hitbox = (self.x,self.x+self.w,self.y,self.y+self.h)
    def draw(self,win):
        pygame.draw.rect(win,White,(self.x,self.y,self.w,self.h))


class alien(object):
    def __init__(self,x,y,w,h,colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = colour
        self.speed = 5
        self.drop = 43
        self.hitbox = (self.x-(2*self.w),self.x+(9*self.w),self.y,self.y+(9*self.h))

    def draw(self,win):
        Dude.m(self.x,self.y,self.w,self.h,self.colour)


    def move(self):
        if self.x < (x_size - 50) and self.y % 2 == 0:
            self.x += self.speed

        elif 10 < self.x  and self.y % 2 != 0:
            self.x -= self.speed
         
        elif self.x >= (x_size - 50):
            self.y += self.drop
            
        elif 10 >= self.x:
            self.y += self.drop
            
    def hit(self):
        print("Hit")
        

score = 0

def ScoreBoard():
    pygame.draw.line(win,Red,(0,50),(x_size,50),2)
    font = pygame.font.Font(None,32)
    k = font.render("Score: "+ str(score), 1, Blue)
    win.blit(k,(15,15))

def rdw():
    win.fill(Black)
    ship.draw(win)
    ScoreBoard()
    '''
    for test in badguy:
        test.draw(win)
    '''
    test.draw(win)
    for pew in gun:
        pew.draw(win)
   
                   
    pygame.display.update()
    


score = 0

ship = player(250,500,50,25)
ship.draw(win)
test = alien(100,100,5,5,Blue)
test.draw(win)
gun = []
badguy = []
t = 0
a = 0
bgn = 10

#MainLoop P.S note for later rember title page
run = True
while run:
    pygame.time.delay(100)
    """
    a += 1
    if len(badguy) < bgn and a % 15 == 0:
        badguy.append(alien(100,100,5,5,Blue))
        pass
    
    """
    if test.hitbox[0] < pew.hitbox[0] < test.hitbox[1] and test.hitbox[2] < pew.hitbox[2] < test.hitbox[3]:
        test.hit()
        
    test.move()
    t -= 1   
    pew = shoot((ship.x + (ship.w/2)),ship.y)
    score = len(gun) 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False

    for pew in gun:
        if test.hitbox[0] < pew.hitbox[0] < test.hitbox[1] and test.hitbox[2] < pew.hitbox[2] < test.hitbox[3]:
            test.hit()
        if pew.y > 50:
            pew.y -= pew.speed
        else:
            gun.pop(gun.index(pew))

    for test in badguy:
        test.move()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and ship.x + ship.w < x_size:
        ship.x += ship.speed
        
    if keys[pygame.K_LEFT] and ship.x > 0:
        ship.x -= ship.speed

    if keys[pygame.K_UP] and t < 0:
        t = 10
        gun.append(shoot((ship.x + (ship.w/2)),ship.y))
    
        
    
    rdw()

pygame.quit()
        
print(pew.hitbox[0])
print("Score:",score)


    
    
