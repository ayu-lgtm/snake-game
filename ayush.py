import pygame
import random
import os

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Snake.mp3')
pygame.mixer.music.play()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

clock=pygame.time.Clock()
screen = pygame.display.set_mode((1000,500))

bgimg=pygame.image.load("hp.jpg")
bgimg=pygame.transform.scale(bgimg,(1000,500)).convert_alpha()


pygame.display.set_caption('ANCONDA')
pygame.display.update()

font=pygame.font.SysFont(None,55)

def scree_score(text,color,x,y):
    scree_text = font.render(text,True,color)
    screen.blit(scree_text,(x,y))

def plot_snake(screen,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(screen,black,[x,y,snake_size,snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        screen.fill((0,0,0))
        scree_score("Welcome To SnakeGame!", white, 250, 200)
        scree_score("Press Space Bar To Play", white, 252, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('ppp.mp3')
                    pygame.mixer.music.play()       
                    gameloop()

        pygame.display.update()
        clock.tick(60)
#creating a game loop
def gameloop():
    exit_game=False
    game_over=False
    
    snk_list=[]
    snk_leng=1
    #check a highscore file
    if(not os.path.exists("Hiscore.txt")):
        with open("Hiscore.txt","w") as f:
            f.write("0")
    with open("Hiscore.txt","r")as f:
        Hiscore=f.read()

    food_x=random.randint(10,990)
    food_y=random.randint(63,419)
    snake_x=50
    snake_y=419
    snake_size=20

    velocity_x=0
    velocity_y=0
    init=3

    fps=60
    score=0
    while not exit_game:
        if game_over:
            with open("Hiscore.txt", "w") as f:
                f.write(str(Hiscore))
            screen.fill(white)
            scree_score("Game_Over ! PRess Enter To Continue",red,150,150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game =True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('Bomb.mp3')
                        pygame.mixer.music.play()
                        welcome()
                

        else:   
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=init
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-init
                        velocity_y=0 
                    if event.key == pygame.K_UP:
                        velocity_y=-init
                        velocity_x=0
                    if event.key == pygame.K_DOWN:
                        velocity_y=init
                        velocity_x=0
                    if event.key == pygame.K_q:
                        score +=10

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=1
                food_x=random.randint(10,990)
                food_y=random.randint(63,419)
                snk_leng +=5 
                if score>int(Hiscore):
                    Hiscore = score

            screen.fill(white)
            screen.blit(bgimg,(0,0))
            scree_score("SCORE:" +str(score)+"      HISCORE:"+str(Hiscore),white,4,4)

            pygame.draw.rect(screen,red,[food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)


            if len(snk_list)>snk_leng:
                del snk_list[0]
            
            if snake_x>1000:
                snake_x = 0
            if snake_x<0:
                snake_x = 1000
                
            if snake_y<63 or snake_y>437:
                game_over=True
                pygame.mixer.music.load('Bomb.mp3')
                pygame.mixer.music.play()


            if head in snk_list[:-1]:
                game_over = True 
                pygame.mixer.music.load('Bomb.mp3')
                pygame.mixer.music.play()
                
            plot_snake(screen,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()