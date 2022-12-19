#imports
import pygame
from pygame.locals import*
import sys
import random
from os import path



pygame.init()

#dir
dir_ = path.dirname(__file__)
#non changeable vars
M_S = [pygame.display.Info().current_w-20,pygame.display.Info().current_h-50]
HEIGHT = M_S[1]  
WIDTH = M_S[0] 
FPS = 60

#colours
RED = (255,0,0)
ORANGE = (255,165,0)
GOLD = (255,215,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SILVER = (192,192,192)
DARKIVORY = (150,150,140)
IVORY = (255,255,240)
GHOSTWHITE = (248,248,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
MINTCREAM = (245,255,250)
GREY = (169,169,169)
DARKGREY = (128,128,128)
LIGHTGREY = (211,211,211)
BOX_S = 7 #box size

#using vars
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('PixiKD')
clock = pygame.time.Clock()
palettes = [BLACK,WHITE,RED,GREEN,BLUE,SILVER]
palette_col = 1
grid_coord = (WIDTH//4,30)
current_tool = 'pen'
base_img = pygame.image.load(f'{dir_}\\images\\base_img.png')
#functions
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def clip(surf,x,y,size_x,size_y):
    surf_handled = surf.copy()
    clipRect = pygame.Rect(x,y,size_x,size_y)
    surf_handled.set_clip(clipRect)
    image = surf.subsurface(surf_handled.get_clip())
    return image.copy()

#classes

class canvas(object):
    '''Each frame has layers and each layer is basically a canvas object'''
    def __init__(self,xsize,ysize,colors):
        self.xsize = xsize
        self.ysize = ysize
        self.colors = colors
        self.colorkey = WHITE
        self.image = pygame.Surface((self.xsize,self.ysize))
        self.image.fill(self.colorkey)
        self.opacity = 255
        self.base = clip(base_img,0,0,self.xsize,self.ysize)
    
    def render(self,surf,pos,coeff_opacity,zoom=2):
        self.image.set_colorkey(self.colorkey)
        img_copy = self.image.copy()
        img_copy.set_alpha(int(self.opacity*coeff_opacity))
        surf.blit(pygame.transform.scale(self.base,(self.base.get_width()*zoom,self.base.get_height()*zoom)),pos)
        surf.blit(pygame.transform.scale(img_copy,(self.image.get_width()*zoom,self.image.get_height()*zoom)),pos)
    
    def resize(self,x,y):
        self.xsize,self.ysize = x,y
        new_surf = pygame.Surface((x,y))
        new_surf.fill(self.colorkey)
        new_surf.blit(self.image,(0,0))
        self.image = new_surf

class Frame(object):
    def __init__(self):
        pass
    
class Mouse_data(object):
    def __init__(self):
        self.pos = [0,0]
        self.last_pos = [0,0]
        self.left_click = False
        self.right_click = False
        self.middle_click = False
        self.middle_clicking = False
        self.left_clicking = False
        self.right_clicking = False
    def update_pos(self):
        mx,my = pygame.mouse.get_pos()
        self.last_pos = self.pos.copy()
        self.pos = [mx,my]

        

class Button: 
    
    def __init__(self,font,text,width,height,x,y,cc,color = DARKGREY):
        self.surf = pygame.Surface((int(width),int(height)))
        self.rect = self.surf.get_rect()
        self.color = color
        self.surf.fill(self.color)
        self.pos = (x,y)
        self.font = font
        self.text = text
        self.colour = LIGHTGREY
        self.cc = cc
        self.cc1 = False
        self.rect.topleft = self.pos
        
    def draw(self):
        if self.cc:
            if not self.cc1:
                self.surf.fill(self.color)
            else:
                self.surf.fill(self.colour)
        screen.blit(self.surf,self.pos)
        draw_text(self.text, self.font, BLACK, self.pos[0] + 5, self.pos[1] + 5)
        
    def click(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.cc1 = not self.cc1
                    action = True


        return action
        


#the working:
if __name__=='__main__':
    m_date = Mouse_data()
    canva = canvas(100,100,palettes)
    while True:

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                

        #buttons

        '''workstuff'''

        
        #blitting
        screen.fill(BLACK)
        canva.render(screen,grid_coord,1,2)

        #update screen and FPS rate
        pygame.display.update() 
        clock.tick(FPS)
