import pygame
import random
import time


pygame.mixer.init()
pygame.init()

# color
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
# Creating window display
Screen_Width=800
Screen_Height=500

# Background
bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg, (Screen_Width, Screen_Height))

go = pygame.image.load("gameover.jpg")
go = pygame.transform.scale(go, (Screen_Width, Screen_Height))


gameWindow = pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("The King Cobra")
pygame.display.update()


clock=pygame.time.Clock()

def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, red, [x,y, snake_size, snake_size])
def welcome():
    fps=60
    exit_game=False
    while not exit_game:
        gameWindow.fill((233,220,200))
        gameWindow.blit(bg,(0,0))
        text_screen("Welcome to 'The King Cobra' game",black,160,170)
        text_screen("Press Enter to Play", red, 260, 220)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(fps)
font=pygame.font.SysFont(None,40)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
# Game loop
def gameloop():
    # Games specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    scr = 0
    food_x = random.randint(20, Screen_Width - 20)
    food_y = random.randint(20, Screen_Height - 20)
    snake_size = 10
    init_velocity = 3
    fps = 60
    food_size=3
    snake_list = []
    snake_length = 1

    while not exit_game:
        if game_over==True:
            gameWindow.fill(black)
            gameWindow.blit(go,(0,0))
            text_screen("Press 'Enter' to continue...",red,230,300)
            text_screen("You Score: " + str(scr), red,320,170)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                         # snake_x=snake_x + 10
                    if event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                        # snake_x = snake_x - 10
                    if event.key == pygame.K_UP:
                        velocity_x=0
                        velocity_y=-init_velocity
                        # snake_y = snake_y - 10
                    if event.key == pygame.K_DOWN:
                        velocity_x=0
                        velocity_y=init_velocity
                        # snake_y = snake_y + 10
                    if event.key == pygame.K_q:
                        scr=scr+50
            snake_x = snake_x+velocity_x
            snake_y = snake_y+velocity_y
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                scr=scr+10
                print("Score: ",scr)
                init_velocity=init_velocity+0.3
                snake_length=snake_length+5
                pygame.mixer.music.load('snakehiss.mp3')
                pygame.mixer.music.play()
                food_x = random.randint(20, Screen_Width -20)
                food_y = random.randint(20, Screen_Height -20)
            if snake_x<0 or snake_x>Screen_Width or snake_y<0 or snake_y>Screen_Height:
                game_over=True
                time.sleep(0.5)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True
                time.sleep(0.5)

            gameWindow.fill(black)
            text_screen("Score: "+str(scr),red,5,5)
            pygame.draw.rect(gameWindow,red,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,red,snake_list,snake_size)
        pygame.draw.rect(gameWindow, white,[food_x,food_y,food_size,food_size])

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
