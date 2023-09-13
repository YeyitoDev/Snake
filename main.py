import pygame
import time
import random


pygame.init()

dis_width = 800
dis_height  = 600

dis=pygame.display.set_mode((dis_width,dis_height))

pygame.display.set_caption('Snake game by Yeyo')
pygame.display.update()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

game_over=False

x1 = dis_width/2
y1 = dis_height/2
 
x1_change = 0       
y1_change = 0

snakeMove = 10
snake_speed=10

snake_width = 10
snake_height = 10

snake_block = 1

snakeBody = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# snakeLen = len(snakeBody)


#la actualizacion de coordenadas no esta funcionando, 
#los bloques obtienen todos las mismas coordendas

def snakeBodyMovement(snakeBody, xchange, ychange, food):

    #La serpiente se mueve, el bloque n+1 obtiene las coordenadas de n

    print(snakeBody)
    snakeList = []
    
    if food:
        snakeList.append([snakeBody[0][0]+xchange, snakeBody[0][1]+ychange])   
    
    for block in range(len(snakeBody)):
        if block == 0:
            snakeList.append([snakeBody[block][0] + xchange,snakeBody[block][1] + ychange])
        else:
            snakeList.append([snakeBody[block-1][0],snakeBody[block-1][1] ])
         

    for block in range(len(snakeList)):
        pygame.draw.rect(dis, white, [snakeList[block][0], snakeList[block][1], snake_width, snake_height]) 

    return snakeList


food_x = random.randint(0, dis_width-20) 
food_y = random.randint(0, dis_height-20) 

food_width = 10
food_height = 10



clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])


food = False

 

while not game_over:
    for event in pygame.event.get():

        print(event)

        if event.type==pygame.QUIT:
            game_over=True
        
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'a':
                x1_change = -snakeMove
                y1_change = 0
            elif pygame.key.name(event.key) == 'd':
                x1_change = snakeMove
                y1_change = 0
            elif pygame.key.name(event.key) == 'w':
                y1_change = -snakeMove
                x1_change = 0
            elif pygame.key.name(event.key) == 's':
                y1_change = snakeMove
                x1_change = 0

        x1 += x1_change
        y1 += y1_change

    if snakeBody[0][1] > dis_height or snakeBody[0][0] > dis_width or snakeBody[0][1] < 0 or snakeBody[0][0] <  0:
        game_over = True
    
    if food_x-food_width <= snakeBody[0][0] <= food_x+food_width and food_y-food_height <= snakeBody[0][1] <= food_y+food_height:
        # snake_height += 10 
        food = True
        food_x = random.randint(0, dis_width-20) 
        food_y = random.randint(0, dis_height-20) 
        
    
    dis.fill(black)

    # print(x1_change, y1_change)

    snakeBody = snakeBodyMovement(snakeBody, x1_change, y1_change, food)
   
    food = False

    pygame.draw.rect(dis, red, [food_x, food_y, food_width, food_height])


    pygame.display.update()

    clock.tick(snake_speed)
           #prints out all the actions that take place on the screen
message("You lost",red)
pygame.display.update()
time.sleep(0)
pygame.quit()
quit()