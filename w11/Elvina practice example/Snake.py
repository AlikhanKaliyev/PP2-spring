import pygame
import random 
import time
import json
from pygame import mixer
pygame.init()

WIDTH = 600
HEIGHT = 500

speed=2
speed1=2
score=0
score1=0
go = True
AR=0
BR=0
data={
    'score': 0,
    'score1': 0,
    'speed':0,
    'speed1':0,
    'dx':0,
    'dy':0,
    'dx1':0,
    'dy1':0,
    'snake.elements':[],
    'snake1.elements1':[],
    'lolikta':0,
    'size':0,
    'size1':0
    }
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Snake Game')
font = pygame.font.SysFont('Arial', 30)

pygame.display.set_caption("Game")
mixer.music.load('Music123.wav')
mixer.music.play(-1)

FPS = 30
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        global speed
        self.radius = 10
        self.dx = speed
        self.dy = 0
        self.elements = [[100, 100]]
        self.size = 1
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (50, 28, 217), element, self.radius)

    def add_snake(self):
        global score
        global AR
        if AR==0:
            score+=1
            self.elements.append([0, 0])
            self.is_add = False

    def move(self):
        if self.is_add:
            self.add_snake()
        for i in range(len(self.elements) -1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
            
class Snake1:
    def __init__(self):
        global speed1
        self.radius1 = 10
        self.dx1 = -speed1
        self.dy1 = 0
        self.elements1 = [[500, 100]]
        self.is_add1 = False

    def draw1(self):
        for element in self.elements1:
            pygame.draw.circle(screen, (50, 200, 217), element, self.radius1)

    def add_snake1(self):
        global score1
        global BR
        if BR==0:    
            score1 += 1
            self.elements1.append([0, 0])
            self.is_add1 = False

    def move1(self):
        if self.is_add1:
            self.add_snake1()
        for i in range(len(self.elements1) - 1, 0, -1):
            self.elements1[i][0] = self.elements1[i - 1][0]
            self.elements1[i][1] = self.elements1[i - 1][1]
        
        self.elements1[0][0] += self.dx1
        self.elements1[0][1] += self.dy1

class Food:

    def __init__(self):
        self.x = random.randint(100, WIDTH - 70)
        self.y = random.randint(100, HEIGHT - 70)
        self.image = pygame.image.load("apple.png")
        # self.position = [random.randint(0, WIDTH - 100), random.randint(0, HEIGHT - 100)]
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def show_score(x, y, score):
    show = font.render('1st:' + str(score), True, (50, 28, 217))
    screen.blit(show, (x, y))
def show_score1(x, y, score1):
    show = font.render('2nd:' + str(score1), True, (50, 28, 217))
    screen.blit(show, (x, y))

def collision():
    global AR
    if AR==0:
        if(food.x in range(snake.elements[0][0] - 20, snake.elements[0][0])) and (food.y in range(snake.elements[0][1] - 20, snake.elements[0][1])):
            snake.is_add = True
            global speed
            speed+=0
            food.x = random.randint(50, WIDTH - 70)
            food.y = random.randint(50, HEIGHT - 70)

def collision1():
    global BR
    if BR==0:
        if(food.x in range(snake1.elements1[0][0] - 20, snake1.elements1[0][0])) and (food.y in range(snake1.elements1[0][1] - 20, snake1.elements1[0][1])):
            snake1.is_add1 = True
            global speed1
            speed1+=0
            food.x = random.randint(50, WIDTH - 70)
            food.y = random.randint(50, HEIGHT - 70)

def is_in_walls():
    return snake.elements[0][0] > WIDTH - 45 or snake.elements[0][0] < 45 or snake.elements[0][1]>HEIGHT-45 or snake.elements[0][1]<45
def is_in_walls1():
    return snake1.elements1[0][0] > WIDTH - 45 or snake1.elements1[0][0] < 45 or snake1.elements1[0][1]>HEIGHT-45 or snake1.elements1[0][1]<45
def game_over():
    # pygame.display.flip()
    global score,score1
    screen.fill((255, 0, 0))
    txt = font.render('GAME OVER!', True, (255, 255, 255))
    if score==score1:
        my_score = font.render('DRAW', True, (255, 255, 255))
    elif score>score1:
        my_score = font.render('1st has won', True, (255, 255, 255))
    else:
        my_score = font.render('2nd has won', True, (255, 255, 255))
    lolka = font.render('1st score:'+str(score), True,(255,255,255))
    lolka1 = font.render('2nd score:'+str(score1), True,(255,255,255))
    screen.blit(txt, (200, 200))
    screen.blit(my_score, (200, 300))
    screen.blit(lolka, (200, 350))
    screen.blit(lolka1, (200, 400))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

def show_walls():
    for i in range(0, WIDTH, 15):
        screen.blit(wall_image, (i, 0))
        screen.blit(wall_image, (i, HEIGHT-30))
        screen.blit(wall_image, (0, i))
        screen.blit(wall_image, (WIDTH-30, i))
def walle():
    for i in range(0,225,15):
        screen.blit(wall_image,(150+i,250))
        screen.blit(wall_image,(250,150+i))
def wallik():
    for i in range(0,300,15):
        screen.blit(wall_image,(190,i))
        screen.blit(wall_image,(90,200+i))
        screen.blit(wall_image,(290,200+i))
        screen.blit(wall_image,(390,i))
        screen.blit(wall_image,(490,200+i))

def collo():
    return (snake.elements[0][0]>245 and snake.elements[0][0]<290 and snake.elements[0][1]>140 and snake.elements[0][1]<380) or (snake.elements[0][0]>140 and snake.elements[0][0]<380 and snake.elements[0][1]>245 and snake.elements[0][1]<290) 
def collo1():
    return (snake1.elements1[0][0]>245 and snake1.elements1[0][0]<290 and snake1.elements1[0][1]>145 and snake1.elements1[0][1]<380) or (snake1.elements1[0][0]>145 and snake1.elements1[0][0]<380 and snake1.elements1[0][1]>245 and snake1.elements1[0][1]<290)
def coalio():
    if(food.x in range(225,295) and food.y in range(125,395)) or (food.x in range(125,395) and food.y in range(225,295)):
            food.x = random.randint(50, WIDTH - 70)
            food.y = random.randint(50, HEIGHT - 70)
def coalio2():
    if(food.x in range(160,260) and food.y in range(0,340)):
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)
    if(food.x in range(60,160) and food.y in range(160,500)):
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)
    if(food.x in range(260,360) and food.y in range(160,500)):
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)
    if(food.x in range(360,460) and food.y in range(0,340)):
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)
    if(food.x in range(460,560) and food.y in range(160,500)):
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)


def wallik1():
    return  (snake.elements[0][0]>185 and snake.elements[0][0]<230 and snake.elements[0][1]>0 and snake.elements[0][1]<310) or (snake.elements[0][0]>385 and snake.elements[0][0]<430 and snake.elements[0][1]>0 and snake.elements[0][1]<310)
def wallik2():
    return  (snake.elements[0][0]>85 and snake.elements[0][0]<130 and snake.elements[0][1]>190 and snake.elements[0][1]<500) or (snake.elements[0][0]>285 and snake.elements[0][0]<330 and snake.elements[0][1]>190 and snake.elements[0][1]<500) 
def wallik3():
    return  (snake.elements[0][0]>485 and snake.elements[0][0]<530 and snake.elements[0][1]>190 and snake.elements[0][1]<500)
def wallik11():
    return  (snake1.elements1[0][0]>185 and snake1.elements1[0][0]<230 and snake1.elements1[0][1]>0 and snake1.elements1[0][1]<310) or (snake1.elements1[0][0]>385 and snake1.elements1[0][0]<430 and snake1.elements1[0][1]>0 and snake1.elements1[0][1]<310)
def wallik12():
    return  (snake1.elements1[0][0]>85 and snake1.elements1[0][0]<130 and snake1.elements1[0][1]>190 and snake1.elements1[0][1]<500) or (snake1.elements1[0][0]>285 and snake1.elements1[0][0]<330 and snake1.elements1[0][1]>190 and snake1.elements1[0][1]<500) 
def wallik13():
    return  (snake1.elements1[0][0]>485 and snake1.elements1[0][0]<530 and snake1.elements1[0][1]>190 and snake1.elements1[0][1]<500)
snake = Snake()
snake1 = Snake1()

food = Food()

wall_image = pygame.image.load('wall.png')
plus=True
screen.fill((165, 206, 216))
font = pygame.font.SysFont('Arial', 40)
show = font.render('Press 1 to pick the first level', True, (0, 0, 0))
screen.blit(show, (20, 50))
show = font.render('Press 2 to pick the second level', True, (0, 0, 0))
screen.blit(show, (20, 150))
show = font.render('Press 3 to pick the third level', True, (0, 0, 0))
screen.blit(show, (20, 250))
show = font.render('Press 4 to load the last played level', True, (0, 0, 0))
screen.blit(show, (20, 350))
k=0
k=0
lolikta=0
while plus:
    mil= clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            plus = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                lolikta=1
                while go:
                    mil = clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            with open('lolik.txt','w') as scorefile:
                                json.dump(data,scorefile)
                            go = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT:
                                snake.dx = speed
                                snake.dy = 0
                            if event.key == pygame.K_LEFT:
                                snake.dx = -speed
                                snake.dy = 0
                            if event.key == pygame.K_UP:
                                snake.dx = 0
                                snake.dy = -speed
                            if event.key == pygame.K_DOWN:
                                snake.dx = 0
                                snake.dy = speed
                            if event.key == pygame.K_d:
                                snake1.dx1 = speed1
                                snake1.dy1 = 0
                            if event.key == pygame.K_a:
                                snake1.dx1 = -speed1
                                snake1.dy1 = 0
                            if event.key == pygame.K_w:
                                snake1.dx1 = 0
                                snake1.dy1 = -speed1
                            if event.key == pygame.K_s:
                                snake1.dx1 = 0
                                snake1.dy1 = speed1
                    if is_in_walls():
                        score=0
                        score-=9999
                        game_over()
                    if is_in_walls1():
                        score1=0
                        score1-=9999
                        game_over()
                    for block in snake.elements[1:]:

                            if (block[0] == snake.elements[0][0] and
                                    block[1] == snake.elements[0][1]):
                                    score=0
                                    score=-9999
                                    game_over()
                    for block in snake1.elements1[1:]:

                            if (block[0] == snake1.elements1[0][0] and
                                    block[1] == snake1.elements1[0][1]):
                                    score1=0
                                    score1-=9999
                                    game_over()
                    for i in snake1.elements1:
                        if i[0]==snake.elements[0][0] and i[1]==snake.elements[0][1]:
                            game_over()
                    for i in snake.elements:
                        if i[0]==snake1.elements1[0][0] and i[1]==snake1.elements1[0][1]:
                            game_over()
                    data['score']=score
                    data['score1']=score1
                    data['speed']=speed
                    data['speed1']=speed1
                    data['dx']=snake.dx
                    data['dy']=snake.dy
                    data['dx1']=snake1.dx1
                    data['dy1']=snake1.dy1
                    data['snake.elements']=snake.elements
                    data['snake1.elements1']=snake1.elements1
                    data['lolikta']=lolikta
                    collision()
                    collision1()
                    screen.fill((165, 206, 216))
                    snake.move()
                    snake.draw()
                    snake1.move1()
                    snake1.draw1()
                    food.draw()
                    show_score(35, 45, score)
                    show_score1(35,85,score1)
                    show_walls()
                    pygame.display.flip()
            if event.key == pygame.K_2:
                lolikta=2
                while go:
                    mil = clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            with open('lolik.txt','w') as scorefile:
                                json.dump(data,scorefile)
                            go = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT:
                                snake.dx = speed
                                snake.dy = 0
                            if event.key == pygame.K_LEFT:
                                snake.dx = -speed
                                snake.dy = 0
                            if event.key == pygame.K_UP:
                                snake.dx = 0
                                snake.dy = -speed
                            if event.key == pygame.K_DOWN:
                                snake.dx = 0
                                snake.dy = speed
                            if event.key == pygame.K_d:
                                snake1.dx1 = speed1
                                snake1.dy1 = 0
                            if event.key == pygame.K_a:
                                snake1.dx1 = -speed1
                                snake1.dy1 = 0
                            if event.key == pygame.K_w:
                                snake1.dx1 = 0
                                snake1.dy1 = -speed1
                            if event.key == pygame.K_s:
                                snake1.dx1 = 0
                                snake1.dy1 = speed1
                    if is_in_walls():
                        score=0
                        score=-9999
                        game_over()
                    if is_in_walls1():
                        score1=0
                        score1-=9999
                        game_over()
                    if collo():
                        score=0
                        score-=9999
                        game_over()
                    if collo1():
                        score1=0
                        score1-=9999
                        game_over()
                    for block in snake.elements[1:]:

                            if (block[0] == snake.elements[0][0] and
                                    block[1] == snake.elements[0][1]):
                                    score=0
                                    score-=9999
                                    game_over()
                    for block in snake1.elements1[1:]:

                            if (block[0] == snake1.elements1[0][0] and
                                    block[1] == snake1.elements1[0][1]):
                                    score1=0
                                    score-=9999
                                    game_over()
                    for i in snake1.elements1:
                        if i[0]==snake.elements[0][0] and i[1]==snake.elements[0][1]:
                            game_over()
                    for i in snake.elements:
                        if i[0]==snake1.elements1[0][0] and i[1]==snake1.elements1[0][1]:
                            game_over()
                    data['score']=score
                    data['score1']=score1
                    data['speed']=speed
                    data['speed1']=speed1
                    data['dx']=snake.dx
                    data['dy']=snake.dy
                    data['dx1']=snake1.dx1
                    data['dy1']=snake1.dy1
                    data['snake.elements']=snake.elements
                    data['snake1.elements1']=snake1.elements1
                    data['lolikta']=lolikta
                    collision()
                    collision1()
                    screen.fill((165, 206, 216))
                    snake.move()
                    snake.draw()
                    snake1.move1()
                    snake1.draw1()
                    food.draw()
                    show_score(35, 45, score)
                    show_score1(35,85,score1)
                    show_walls()
                    walle()
                    collo()
                    collo1()
                    coalio()
                    pygame.display.flip()
            if event.key == pygame.K_3:
                lolikta=3
                while go:
                    mil = clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            with open('lolik.txt','w') as scorefile:
                                json.dump(data,scorefile)
                            go = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT:
                                snake.dx = speed
                                snake.dy = 0
                            if event.key == pygame.K_LEFT:
                                snake.dx = -speed
                                snake.dy = 0
                            if event.key == pygame.K_UP:
                                snake.dx = 0
                                snake.dy = -speed
                            if event.key == pygame.K_DOWN:
                                snake.dx = 0
                                snake.dy = speed
                            if event.key == pygame.K_d:
                                snake1.dx1 = speed1
                                snake1.dy1 = 0
                            if event.key == pygame.K_a:
                                snake1.dx1 = -speed1
                                snake1.dy1 = 0
                            if event.key == pygame.K_w:
                                snake1.dx1 = 0
                                snake1.dy1 = -speed1
                            if event.key == pygame.K_s:
                                snake1.dx1 = 0
                                snake1.dy1 = speed1
                    if is_in_walls():
                        score=0
                        score=-9999
                        game_over()
                    if is_in_walls1():
                        score1=0
                        score1-=9999
                        game_over()
                    if wallik1():
                        score=0
                        score=-9999
                        game_over()
                    if wallik2():
                        score=0
                        score=-9999
                        game_over()
                    if wallik3():
                        score=0
                        score=-9999
                        game_over()
                    if wallik11():
                        score1=0
                        score1=-9999
                        game_over()
                    if wallik12():
                        score1=0
                        score1=-9999
                        game_over()
                    if wallik13():
                        score1=0
                        score1=-9999
                        game_over()

                    for block in snake.elements[1:]:

                            if (block[0] == snake.elements[0][0] and
                                    block[1] == snake.elements[0][1]):
                                    score=0
                                    score-=9999
                                    game_over()
                    for block in snake1.elements1[1:]:

                            if (block[0] == snake1.elements1[0][0] and
                                    block[1] == snake1.elements1[0][1]):
                                    score1=0
                                    score-=9999
                                    game_over()
                    for i in snake1.elements1:
                        if i[0]==snake.elements[0][0] and i[1]==snake.elements[0][1]:
                            game_over()
                    for i in snake.elements:
                        if i[0]==snake1.elements1[0][0] and i[1]==snake1.elements1[0][1]:
                            game_over()
                    data['score']=score
                    data['score1']=score1
                    data['speed']=speed
                    data['speed1']=speed1
                    data['dx']=snake.dx
                    data['dy']=snake.dy
                    data['dx1']=snake1.dx1
                    data['dy1']=snake1.dy1
                    data['snake.elements']=snake.elements
                    data['snake1.elements1']=snake1.elements1
                    data['lolikta']=lolikta
                    collision()
                    collision1()
                    screen.fill((165, 206, 216))
                    snake.move()
                    snake.draw()
                    snake1.move1()
                    snake1.draw1()
                    food.draw()
                    show_score(35, 45, score)
                    show_score1(35,85,score1)
                    show_walls()
                    wallik()
                    wallik1()
                    wallik2()
                    wallik3()
                    wallik11()
                    wallik12()
                    wallik13()
                    coalio2()
                    pygame.display.flip()
            if event.key==pygame.K_4:
                with open('lolik.txt',) as scorefile:
                        data=json.load(scorefile)
                score=data['score']
                score1=data['score1']
                speed=data['speed']
                speed1=data['speed1']
                snake.dx=data['dx']
                snake.dy=data['dy']
                snake1.dx1=data['dx1']
                snake1.dy1=data['dy1']
                snake.elements=data['snake.elements']
                snake1.elements1=data['snake1.elements1']
                
                if data['lolikta']==1:
                    while go:
                        mil = clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                with open('lolik.txt','w') as scorefile:
                                    json.dump(data,scorefile)
                                go = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                    snake.dx = speed
                                    snake.dy = 0
                                if event.key == pygame.K_LEFT:
                                    snake.dx = -speed
                                    snake.dy = 0
                                if event.key == pygame.K_UP:
                                    snake.dx = 0
                                    snake.dy = -speed
                                if event.key == pygame.K_DOWN:
                                    snake.dx = 0
                                    snake.dy = speed
                                if event.key == pygame.K_d:
                                    snake1.dx1 = speed1
                                    snake1.dy1 = 0
                                if event.key == pygame.K_a:
                                    snake1.dx1 = -speed1
                                    snake1.dy1 = 0
                                if event.key == pygame.K_w:
                                    snake1.dx1 = 0
                                    snake1.dy1 = -speed1
                                if event.key == pygame.K_s:
                                    snake1.dx1 = 0
                                    snake1.dy1 = speed1
                        if is_in_walls():
                            score=0
                            score-=9999
                            game_over()
                        if is_in_walls1():
                            score1=0
                            score1-=9999
                            game_over()
                        for block in snake.elements[1:]:

                                if (block[0] == snake.elements[0][0] and
                                        block[1] == snake.elements[0][1]):
                                        score=0
                                        score=-9999
                                        game_over()
                        for block in snake1.elements1[1:]:

                                if (block[0] == snake1.elements1[0][0] and
                                        block[1] == snake1.elements1[0][1]):
                                        score1=0
                                        score1-=9999
                                        game_over()
                        for i in snake1.elements1:
                            if i[0]==snake.elements[0][0] and i[1]==snake.elements[0][1]:
                                game_over()
                        for i in snake.elements:
                            if i[0]==snake1.elements1[0][0] and i[1]==snake1.elements1[0][1]:
                                game_over()
                        data['score']=score
                        data['score1']=score1
                        data['speed']=speed
                        data['speed1']=speed1
                        data['dx']=snake.dx
                        data['dy']=snake.dy
                        data['dx1']=snake1.dx1
                        data['dy1']=snake1.dy1
                        data['snake.elements']=snake.elements
                        data['snake1.elements1']=snake1.elements1

                        
                        collision()
                        collision1()
                        screen.fill((165, 206, 216))
                        snake.move()
                        snake.draw()
                        snake1.move1()
                        snake1.draw1()
                        food.draw()
                        show_score(35, 45, score)
                        show_score1(35,85,score1)
                        show_walls()
                        pygame.display.flip()
                if data['lolikta']==2:
                    while go:
                        mil = clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                with open('lolik.txt','w') as scorefile:
                                    json.dump(data,scorefile)
                                go = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                    snake.dx = speed
                                    snake.dy = 0
                                if event.key == pygame.K_LEFT:
                                    snake.dx = -speed
                                    snake.dy = 0
                                if event.key == pygame.K_UP:
                                    snake.dx = 0
                                    snake.dy = -speed
                                if event.key == pygame.K_DOWN:
                                    snake.dx = 0
                                    snake.dy = speed
                                if event.key == pygame.K_d:
                                    snake1.dx1 = speed1
                                    snake1.dy1 = 0
                                if event.key == pygame.K_a:
                                    snake1.dx1 = -speed1
                                    snake1.dy1 = 0
                                if event.key == pygame.K_w:
                                    snake1.dx1 = 0
                                    snake1.dy1 = -speed1
                                if event.key == pygame.K_s:
                                    snake1.dx1 = 0
                                    snake1.dy1 = speed1
                        if is_in_walls():
                            score=0
                            score=-9999
                            game_over()
                        if is_in_walls1():
                            score1=0
                            score1-=9999
                            game_over()
                        if collo():
                            score=0
                            score-=9999
                            game_over()
                        if collo1():
                            score1=0
                            score1-=9999
                            game_over()
                        for block in snake.elements[1:]:

                                if (block[0] == snake.elements[0][0] and
                                        block[1] == snake.elements[0][1]):
                                        score=0
                                        score-=9999
                                        game_over()
                        for block in snake1.elements1[1:]:

                                if (block[0] == snake1.elements1[0][0] and
                                        block[1] == snake1.elements1[0][1]):
                                        score1=0
                                        score-=9999
                                        game_over()
                        for i in snake1.elements1:
                            if i[0]==snake.elements[0][0] and i[1]==snake.elements[0][1]:
                                game_over()
                        for i in snake.elements:
                            if i[0]==snake1.elements1[0][0] and i[1]==snake1.elements1[0][1]:
                                game_over()
                        data['score']=score
                        data['score1']=score1
                        data['speed']=speed
                        data['speed1']=speed1
                        data['dx']=snake.dx
                        data['dy']=snake.dy
                        data['dx1']=snake1.dx1
                        data['dy1']=snake1.dy1
                        data['snake.elements']=snake.elements
                        data['snake1.elements1']=snake1.elements1
                        collision()
                        collision1()
                        screen.fill((165, 206, 216))
                        snake.move()
                        snake.draw()
                        snake1.move1()
                        snake1.draw1()
                        food.draw()
                        show_score(35, 45, score)
                        show_score1(35,85,score1)
                        show_walls()
                        walle()
                        collo()
                        collo1()
                        coalio()
                        pygame.display.flip()
                if data['lolikta']==3:
                    while go:
                        mil = clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                with open('lolik.txt','w') as scorefile:
                                    json.dump(data,scorefile)
                                go = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                    snake.dx = speed
                                    snake.dy = 0
                                if event.key == pygame.K_LEFT:
                                    snake.dx = -speed
                                    snake.dy = 0
                                if event.key == pygame.K_UP:
                                    snake.dx = 0
                                    snake.dy = -speed
                                if event.key == pygame.K_DOWN:
                                    snake.dx = 0
                                    snake.dy = speed
                                if event.key == pygame.K_d:
                                    snake1.dx1 = speed1
                                    snake1.dy1 = 0
                                if event.key == pygame.K_a:
                                    snake1.dx1 = -speed1
                                    snake1.dy1 = 0
                                if event.key == pygame.K_w:
                                    snake1.dx1 = 0
                                    snake1.dy1 = -speed1
                                if event.key == pygame.K_s:
                                    snake1.dx1 = 0
                                    snake1.dy1 = speed1
                        if is_in_walls():
                            score=0
                            score=-9999
                            game_over()
                        if is_in_walls1():
                            score1=0
                            score1-=9999
                            game_over()
                        if wallik1():
                            score=0
                            score=-9999
                            game_over()
                        if wallik2():
                            score=0
                            score=-9999
                            game_over()
                        if wallik3():
                            score=0
                            score=-9999
                            game_over()
                        if wallik11():
                            score1=0
                            score1=-9999
                            game_over()
                        if wallik12():
                            score1=0
                            score1=-9999
                            game_over()
                        if wallik13():
                            score1=0
                            score1=-9999
                            game_over()

                        for block in snake.elements[1:]:

                                if (block[0] == snake.elements[0][0] and
                                        block[1] == snake.elements[0][1]):
                                        score=0
                                        score-=9999
                                        game_over()
                        for block in snake1.elements1[1:]:

                                if (block[0] == snake1.elements1[0][0] and
                                        block[1] == snake1.elements1[0][1]):
                                        score1=0
                                        score-=9999
                                        game_over()
                        for i in snake1.elements1:
                            if i[0]==snake.elements[0][0] and i[1]==snake.elements[0][1]:
                                game_over()
                        for i in snake.elements:
                            if i[0]==snake1.elements1[0][0] and i[1]==snake1.elements1[0][1]:
                                game_over()
                        data['score']=score
                        data['score1']=score1
                        data['speed']=speed
                        data['speed1']=speed1
                        data['dx']=snake.dx
                        data['dy']=snake.dy
                        data['dx1']=snake1.dx1
                        data['dy1']=snake1.dy1
                        data['snake.elements']=snake.elements
                        data['snake1.elements1']=snake1.elements1
                        collision()
                        collision1()
                        screen.fill((165, 206, 216))
                        snake.move()
                        snake.draw()
                        snake1.move1()
                        snake1.draw1()
                        food.draw()
                        show_score(35, 45, score)
                        show_score1(35,85,score1)
                        show_walls()
                        wallik()
                        wallik1()
                        wallik2()
                        wallik3()
                        wallik11()
                        wallik12()
                        wallik13()
                        coalio2()
                        pygame.display.flip()


    pygame.display.flip()