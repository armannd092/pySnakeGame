import pygame
import time
import random

pygame.init()

# set the display
dis_width = 720
dis_height = 480
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('snake game')

#Color
white = (255, 255, 255)
black = (0,0,0)
gray = (180,180,180)
blue = (0,0,255)
red = (255,0,0)
#Font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
#time defined
clock = pygame.time.Clock()
#Snake variable
snake_block = 10
snake_speed=10

def our_snake(snake_block, snake_list):
    '''
        this function growing the snake when it eats 
    '''
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])


def message(msg,color,pos = [dis_width/5, dis_height/2]):
    '''
        this function render the texts on the scren 
    '''
    mesg = font_style.render(msg,True, color)
    dis.blit(mesg,pos)

def gameloop():
    '''
        this the main game funtion
    '''
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0 
    y1_change = 0
    game_over = False
    game_close = False
    snake_list = []
    length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block)/ 10.0)*10
    foody = round(random.randrange(0, dis_height - snake_block)/ 10.0)*10

    while not game_over:
        
        while  game_close == True:
            dis.fill(white)
            message('You lost! press Q-Quit or C-Play again', red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            # game controler
            if event.type == pygame.QUIT:
                game_over =True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0 
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0 
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0 :
            #rule1: do not pass the play ground
            game_close = True

        #moving the snake
        x1 += x1_change
        y1 += y1_change

        #draw the playground 
        dis.fill(white)
        #draw food
        pygame.draw.rect(dis,blue,[foodx,foody,snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        
        snake_list.append(snake_Head)
        if len(snake_list)> length_of_snake:
            del snake_list[0]
            pass
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_list)
        message(str(length_of_snake-1),gray,pos = [dis_width/15,dis_height/10])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameloop()