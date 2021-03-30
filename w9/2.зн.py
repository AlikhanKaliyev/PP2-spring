import pygame
import math

class Point:
    # constructed using a normal tupple
    def __init__(self, point_t = (0,0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)
def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=4):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement.__div__(length)
    for index in range(0, int(length/dash_length), 2):
        start = origin + (slope *    index    * dash_length)
        end   = origin + (slope * (index + 1) * dash_length)
        pygame.draw.line(surf, color, start.get(), end.get(), width)
pygame.init()
screen=pygame.display.set_mode((850,650))
White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)
Blue=(0,0,255)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    screen.fill(White)
    pygame.draw.line(screen,Black,(425,100),(425,550),2)
    pygame.draw.line(screen,Black,(100,325),(750,325),2)
    pygame.draw.rect(screen,Black,(100,100,650,450),2)
    x=125
    for i in range(0,7):
        pygame.draw.line(screen,Black,(x,100),(x,550))
        x+=100
    y=125
    for i in range(0,9):
        pygame.draw.line(screen,Black,(100,y),(750,y))
        y+=50
    x=137.5
    for i in range(0,24):
        pygame.draw.line(screen,Black,(x,100),(x,106.25))
        pygame.draw.line(screen,Black,(x,550-6.25),(x,550))
        x+=25
    x=150
    for i in range(0,12):
        pygame.draw.line(screen,Black,(x,100),(x,112.5))
        pygame.draw.line(screen,Black,(x,550-12.5),(x,550))
        x+=50
    x=175
    for i in range(0,6):
        pygame.draw.line(screen,Black,(x,100),(x,100+0.75*25))
        pygame.draw.line(screen,Black,(x,550-0.75*25),(x,550))
        x+=100
    y=137.5
    for i in range(0,16):
        pygame.draw.line(screen,Black,(100,y),(106.25,y))
        pygame.draw.line(screen,Black,(750-6.25,y),(750,y))
        y+=25
    y=150
    for i in range(0,8):
        pygame.draw.line(screen,Black,(100,y),(112.5,y))
        pygame.draw.line(screen,Black,(750-12.5,y),(750,y))
        y+=50
    pygame.draw.line(screen,White,(525,126),(525,174))
    myfont = pygame.font.SysFont('arial',16)
    screen.blit(myfont.render('1.00',False,(0,0,0)),(70,115))
    screen.blit(myfont.render('0.75',False,(0,0,0)),(70,165))
    screen.blit(myfont.render('0.50',False,(0,0,0)),(70,215))
    screen.blit(myfont.render('0.25',False,(0,0,0)),(70,265))
    screen.blit(myfont.render('0.00',False,(0,0,0)),(70,315))
    screen.blit(myfont.render('-0.25',False,(0,0,0)),(65.5,365))
    screen.blit(myfont.render('-0.50',False,(0,0,0)),(65.5,415))
    screen.blit(myfont.render('-0.75',False,(0,0,0)),(65.5,465))
    screen.blit(myfont.render('-1.00',False,(0,0,0)),(65.5,515))
    screen.blit(myfont.render('-3п',False,(0,0,0)),(115,560))
    screen.blit(myfont.render('-5п/2',False,(0,0,0)),(165,560))
    screen.blit(myfont.render('-2п',False,(0,0,0)),(215,560))
    screen.blit(myfont.render('-3п/2',False,(0,0,0)),(265,560))
    screen.blit(myfont.render('-п',False,(0,0,0)),(320,560))
    screen.blit(myfont.render('-п/2',False,(0,0,0)),(365,560))
    screen.blit(myfont.render('0',False,(0,0,0)),(423,560))
    screen.blit(myfont.render('п/2',False,(0,0,0)),(465,560))
    screen.blit(myfont.render('п',False,(0,0,0)),(525,560))
    screen.blit(myfont.render('3п/2',False,(0,0,0)),(565,560))
    screen.blit(myfont.render('2п',False,(0,0,0)),(615,560))
    screen.blit(myfont.render('5п/2',False,(0,0,0)),(665,560))
    screen.blit(myfont.render('3п',False,(0,0,0)),(715,560))
    u=[]
    pi=3.14
    k=-3*pi
    q=125
    for i in range(0,97):
        e=math.sin(k)*200
        u.append((q,325-e))
        k+=pi/16
        q+=6.25
    for i in range(0,len(u)-1):
        pygame.draw.aaline(screen,Red,u[i],u[i+1])
    t1=[]
    l=-3*pi
    q=125
    for i in range(0,97):
        e=math.cos(l)*200
        t1.append((q,325-e))
        l+=pi/16
        q+=6.25
    for i in range(0,len(t1)-1):
        draw_dashed_line(screen,Blue,t1[i],t1[i+1])
    screen.blit(myfont.render('sinx',False,(0,0,0)),(509,130))
    screen.blit(myfont.render('cosx',False,(0,0,0)),(509,150))
    pygame.draw.aaline(screen,Red,(550,137.5),(587.5,137.5))
    draw_dashed_line(screen,Blue,(550,162.5),(587.5,162.5))
    pygame.display.flip()
pygame.quit()