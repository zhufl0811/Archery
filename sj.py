import pygame,time
from pygame.locals import *

class ba():
    def __init__(self,screen):
        self.x = 260
        self.y = 10
        self.img=pygame.image.load('./ba.png').convert()
        self.screen=screen
        self.flag = 0
    def draw(self):
        if self.flag == 0:
            if self.x>12:
                self.x -=1
            else:
                self.flag = 1
        else:
            if self.x<826:
                self.x+=1
            else:
                self.flag = 0
        self.screen.blit(self.img, (self.x, self.y))

class kuajiang():
    def __init__(self,screen):
        self.img=pygame.image.load('./text.png').convert()
        self.x=30
        self.y=30
        self.screen=screen
        self.createdtime=time.time()
        
    def draw(self):
            self.screen.blit(self.img,(self.x,self.y))
                    
class jian():
    def __init__(self,x,y,screen,ba):
        self.x=x
        self.y=y
        self.screen=screen
        self.img=pygame.image.load('./jian.ico').convert()
        self.ba=ba
        self.kj=''
        self.createdtime=time.time()
                 

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))
        if self.y>0:
            self.y -=4
        else:
            if self.ba.x<self.x<self.ba.x+110 or self.ba.x+130<self.x<self.ba.x+237:
                if self.ba.flag == 0:
                    self.x-=1
                else:
                    self.x+=1
            elif self.ba.x+100<self.x<self.ba.x+137:
                if self.ba.flag == 0:
                    self.x-=1
                else:
                    self.x+=1
                self.kj=kuajiang(screen)
                print('表扬创建')
            else:
                self.y -=4
        
class gong():
    def __init__(self,screen,ba):
        self.x=290
        self.y=390
        self.img=pygame.image.load('./pao.ico').convert()
        self.screen=screen
        self.jian=[]
        self.ba = ba
        self.screen.blit(self.img, (self.x, self.y))

    def move(self,keytype):
        if keytype == 'left' and self.x>20:
            print('left')
            self.x -=15
        elif keytype == 'right' and self.x<720:
            print('right')
            self.x+=15
        elif keytype == 'space':
            print('space')
            self.jian.append(jian(self.x+136,self.y,self.screen,self.ba))

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))

screen=pygame.display.set_mode([1076,604])
background_img = pygame.image.load('./bg.png').convert()
bazhi = ba(screen)
bow = gong(screen,bazhi)

while True:
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            print('exit')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                bow.move('left')
            elif event.key == K_RIGHT:
                bow.move('right')
            elif event.key == K_SPACE:
                bow.move('space')
    bazhi.draw()
    bow.draw()
    if bow.jian != []:
        print(len(bow.jian))
        for ji in bow.jian:
            if ji.createdtime<time.time()-5:
                bow.jian.remove(ji)
                print('An Arrow was destoried!')
            else:
                ji.draw()
                if ji.kj !='':
                    if ji.kj.createdtime<time.time()-5:
                        del ji.kj
                    else:
                        ji.kj.draw()
    pygame.display.update()
    time.sleep(0.01)