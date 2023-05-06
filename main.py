import sys
from random import *
import pygame
from img_dote import *
import time
from collections import deque
from math import *
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,Rect,MOUSEBUTTONDOWN,K_SPACE,K_a 
pygame.init()
FPSCLOCK = pygame.time.Clock()
size=(985,1000)
SURFACE = pygame.display.set_mode(size)


color={
    "black":[0,0,0],
    "white":[255,255,255],
    "red":[255,0,0],
    "blue":[0,0,255],
    "yellow":[255,255,0],
    "green":[0,255,0],
    "gray":[192,192,192],
    "cyan":[0,183,235],
    "purple":[106,13,173],
    "orange":[249,146,69],
    }

QE=["white","red","blue","yellow","green","gray"]
colorn=[QE[i%len(QE)]for i in range(100)]

block_categories=["","background","I","J","L","O","S","T","Z"]
block_color=["","gray","cyan","blue","orange","yellow","green","purple","red"]

class tile(pygame.sprite.Sprite):
    def __init__(self,tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size=tile_size
        self.style=-1
        self.block="I"
        self.block_number=0
        self.Tile=[]
        self.X=-1 # 타일의 왼쪽 상단 위치
        self.Y=-1 # 타일의 왼쪽 상단 위치
        self.dy=[-1,0,1,0] # 위,오른쪽,아래,왼쪽
        self.dx=[0,1,0,-1] # 위,오른쪽,아래,왼쪽
        #(8, 4)
        self.wall_left_x=8
        #(19, 4)
        self.wall_right_x=19
        #(14, 24)
        self.wall_under_y=24

        #hold
        self.hold=0
        self.hold_tile=""
        self.hold_number=0
        self.hold_x=3
        self.hold_y=7


    def drop_new(self,hold=0,gravity=0):

        if gravity==1 and self.Y<=2:
            print("GAMEOVER")
            sys.exit()

        self.hold=hold
        self.block_number=randint(2,len(block_categories)-1)
        self.block=block_categories[self.block_number]
        self.style=0
        #(12, 2)
        self.X=12
        self.Y=2
        self.Tile=dote(self.block)
        self.draw(self.X,self.Y)

    def return_tile(self):
        
        self.del_tile(self.Tile[self.style])

        if self.hold_tile!="":

            last_tile=dote(TILE.hold_tile)[0]
            #print(last_tile)
            for i in range(len(last_tile)):
                for g in range(len(last_tile[i])):
                    #print(i,g)
                    if last_tile[i][g]!=0:
                        #print("#",i,g,TILE.hold_y+i,TILE.hold_x+g)
                        map_Tile[TILE.hold_y+i][TILE.hold_x+g]=0


            self.hold_tile,self.block = self.block,self.hold_tile
            self.block_number,self.hold_number = self.hold_number,self.block_number
            self.style=0

             #(12, 2)
            self.X=12
            self.Y=2
            self.Tile=dote(self.block)
            self.draw(self.X,self.Y)
            self.hold=1

        
        else:

            self.hold_tile = self.block
            self.hold_number = self.block_number

            self.drop_new(hold=1)

        Tile=dote(self.hold_tile)[0]
        #print(Tile)
        for i in range(len(Tile)):
            for g in range(len(Tile[i])):
                if Tile[i][g]!=0:
                    map_Tile[self.hold_y+i][self.hold_x+g]=self.hold_number


    def draw(self,X,Y):
        Tile=self.Tile[self.style]
        #print(Tile)
        for i in range(len(Tile)):
            for g in range(len(Tile[i])):
                if Tile[i][g]!=0:
                    map_Tile[Y+i][X+g]=self.block_number


    def check(self,Tile,dx,dy):
        #map_Tile[self.Y+i][self.X+g]
        for i in range(len(Tile)):
            for g in range(len(Tile[i])):
                #print("#",self.Y+i+1,self.X+g)
                if Tile[i][g]!=0 and map_Tile[self.Y+i+dy][self.X+g+dx]!=0:
                    return 0
        return 1
    
    def gravity_check(self,Tile,dx,dy):
        self.del_tile(Tile)
        #map_Tile[self.Y+i][self.X+g]
        for i in range(len(Tile)):
            for g in range(len(Tile[i])):
                #print("#",self.Y+i+1,self.X+g)
                if Tile[i][g]!=0 and map_Tile[self.Y+i+dy][self.X+g+dx]!=0:
                    self.draw(self.X,self.Y)
                    return 0
                
        self.draw(self.X,self.Y)
        return 1
    
    def del_tile(self,Tile):
        for i in range(len(Tile)):
            for g in range(len(Tile[i])):
                if Tile[i][g]!=0:
                    map_Tile[self.Y+i][self.X+g]=0
    

    def move_tile(self,direction):

        #print(self.style)

        Tile=self.Tile[self.style]
        self.del_tile(Tile)

        if direction=="down":
            idx=2
        elif direction=="left":
            idx=3
        elif direction=="right":
            idx=1

        ANS=self.check(Tile,self.dx[idx],self.dy[idx])

        if ANS==0:
            self.draw(self.X,self.Y)
        else:
            self.draw(self.X+self.dx[idx],self.Y+self.dy[idx])
            self.Y+=self.dy[idx]
            self.X+=self.dx[idx]

        return ANS
    
    def move_all_tile(self):
        while 1:
            if self.move_tile("down")==0:return 0
    
    def change_tile(self):
        Tile=self.Tile[self.style]
        self.del_tile(Tile)

        next_style=(self.style+1)%len(self.Tile)

        ANS=self.check(self.Tile[next_style],0,0)
        
        if ANS==1:
            self.style=next_style

        self.draw(self.X,self.Y)

        return ANS

                
class map(pygame.sprite.Sprite):
    def __init__(self,tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size=tile_size
        self.block_size=self.draw(init=1)
        
        #"""

    def draw(self,init=0):

        if init!=1:
            for i in range(self.block_size[1]+2):
                for g in range(self.block_size[0]+2):
                    if map_Tile[i][g]!=0 and map_Tile[i][g]!=-1:
                        pygame.draw.rect(SURFACE, color[block_color[map_Tile[i][g]]], [g*self.tile_size,i*self.tile_size,self.tile_size,self.tile_size])

        X=0
        x_cnt=0
        while X<size[0]:
            pygame.draw.line(SURFACE,color["white"],[X,0],[X,size[1]], 1)
            x_cnt+=1
            X+=self.tile_size

        Y=0
        y_cnt=0
        while Y<size[1]:
            pygame.draw.line(SURFACE,color["white"],[0,Y],[size[0],Y], 1)
            y_cnt+=1
            Y+=self.tile_size
        
        return [x_cnt,y_cnt]

    def mouse(self):
        POS=(pygame.mouse.get_pos()[0]//self.tile_size,pygame.mouse.get_pos()[1]//self.tile_size)
        map_Tile[POS[1]][POS[0]]=1

    def mouse_del(self):
        POS=(pygame.mouse.get_pos()[0]//self.tile_size,pygame.mouse.get_pos()[1]//self.tile_size)
        map_Tile[POS[1]][POS[0]]=0


###############
develop=0
###############

MAP=map(35)
TILE=tile(35)

map_Tile=dote("background")
last_time=time.time()
delay={
    "down":[last_time,1.1],
    "k_down":[last_time,0.1],
    "k_left":[last_time,0.1],
    "k_right":[last_time,0.1],
}
contact_floor=[0,1.5,last_time]
hold=0

for i in range(MAP.block_size[1]+2):
    if i>=len(map_Tile):
        map_Tile.append([0]*(MAP.block_size[0]+2))
    else:
        for g in range(MAP.block_size[0]+2):
            if g>=len(map_Tile[i]):
                map_Tile[i].append(0)

TILE.drop_new()

while 1:
    SURFACE.fill(color["black"])


    #event = pygame.event.poll()
    #if event.type == pygame.QUIT:pygame.quit();sys.exit()

    keys = pygame.key.get_pressed()


    #if drop==1:
    #    drop=0
    #    TILE.drop_new()
    if contact_floor[0]==1 and time.time()-contact_floor[2]>=contact_floor[1]:
        contact_floor[0]=0
        
        TILE.drop_new(gravity=1)

    if keys[pygame.K_DOWN]:
        if time.time()-delay["k_down"][0]>=delay["k_down"][1]:
            ANS=TILE.move_tile("down")
            delay["k_down"][0]=time.time()
            if ANS==0:
                if contact_floor[0]==0:
                    contact_floor[0]=1
                    contact_floor[2]=time.time()

            else:
                contact_floor[0]=0
            

    if keys[pygame.K_LEFT]:
        if time.time()-delay["k_left"][0]>=delay["k_left"][1]:
            ANS=TILE.move_tile("left")
            delay["k_left"][0]=time.time()

    if keys[pygame.K_RIGHT]:
        if time.time()-delay["k_right"][0]>=delay["k_right"][1]:
            ASN=TILE.move_tile("right")
            delay["k_right"][0]=time.time()

    if keys[pygame.K_c] and TILE.hold==0:

        TILE.return_tile()

        
        #print("##")
        #(2,6)->(3,7)##
        #(7,9)->(6,8)
        #print()

    for EVENT in pygame.event.get():
        if EVENT.type==QUIT:pygame.quit();sys.exit()

        if EVENT.type == KEYDOWN:
            if EVENT.key == K_UP:
                #print("ASD")
                TILE.change_tile()
            if EVENT.key == K_a:
                TILE.change_tile()
                TILE.change_tile()
            if EVENT.key == K_SPACE:
                TILE.move_all_tile()
                TILE.drop_new()



    if TILE.gravity_check(TILE.Tile[TILE.style],TILE.dx[2],TILE.dy[2])==1:

        contact_floor[0]=0
        contact_floor[2]=time.time()
        #print("XCCCV")
        if time.time()-delay["down"][0]>=delay["down"][1]:#1.1:
            TILE.move_tile("down")
            delay["down"][0]=time.time()

    else:
         if contact_floor[0]==0:
            contact_floor[0]=1



    if develop==1:
        if keys[pygame.K_0]:
            print("################")
            print(*MAP.map_Tile, sep=', \n')
        if keys[pygame.K_1]:
            POS=(pygame.mouse.get_pos()[0]//MAP.tile_size,pygame.mouse.get_pos()[1]//MAP.tile_size)
            print(POS)

        
        if pygame.mouse.get_pressed()[0]==1:
            MAP.mouse()
        if pygame.mouse.get_pressed()[2]==1:
            MAP.mouse_del()

    #print("#")

    MAP.draw()

    """
    key=0
    for event  in pygame.event.get():
        if event.type==QUIT:pygame.quit();sys.exit()
        elif event.type==KEYDOWN:key=event.key

    event = pygame.event.poll()
        if event.type == pygame.QUIT:break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:

    """

    #FPSCLOCK.tick(100)

    pygame.display.update()