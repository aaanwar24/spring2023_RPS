# FIle created by Abdullah Anwar 
# import libraries
# the objective of this code is to create an interactive game of rock, paper, scissors, with images as well as rules. 
# time give us access to the sleep function, which allows us to slow the code down 
from time import sleep
# random allows the computer to make a decision on whether it wants to choose and play rock, paper, or scissors. 
from random import randint 
# pygame is where we get graphics 
import pygame as pg
# the operating system allows the program to find files in the computer. 
import os
# game_folder tells the program where in the computer to find a certain file. 
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 800
HEIGHT = 800
FPS = 30
GAMEOVER = False 

# define colors
# tuples are immutable - you cannot change the value once created 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# this line initializes pygame, and basucally turns it on. It gets pygame ready to use the pixels on the screen.Kinf of like a light switch 
pg.init()
pg.mixer.init()
# opens pygame in a window that is defined by set_mode under the paramters for WIDTH and HEIGHT that have been defined previously 
screen = pg.display.set_mode((WIDTH, HEIGHT))
# when you open up the window, it has a caption on the top, and this gives the string values for the caption. 
pg.display.set_caption("rock, paper, scissors...")
# Clock is a class that does a few things, and it ticks at frames per second. 
clock = pg.time.Clock()
# rock_image creates the variable that stores the pixels and keeps them as ready to be used. 
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
# rock_image_rect isn't storing the pixels themselves, but the dimensions of the pixels, and allows us to access and change those things. 
# if you add to the rock_image_rect variable, it will move. Adding or subtratcing to x and y in certain quantities will lead
# the image to move in a variety of directions
# you need rect because it allows you to change the location of a function 
rock_image_rect = rock_image.get_rect()
rock_image_rect.x = 10

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = 300
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = rock_image.get_rect()
scissors_image_rect.x = 300
scissors_image_rect.y = 190


# running is a variable and it hold the value of True. It remains true until labelled as false like. 
running = True

while running:
    clock.tick(FPS)
    # an event is any time that something happens to the computer that causes them  to ru a loop 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # flow control, it drop us out of the loop and brings us all the way to the pg.quit and ends the loop. 
            running = False
            # 
        if event.type == pg.MOUSEBUTTONUP:
            # this displays the coordinates of the click
            # the 0 is the first value in the tuple and represents the x-value
            print(pg.mouse.get_pos()[0])
            # the 1 is the second value in the tuple and represents the y-value
            print(pg.mouse.get_pos()[1])
            mouse_coords = pg.mouse.get_pos()
            # if pg.mouse.get_pos()[0] <= my_image_rect.width and pg.mouse.get_pos()[1] < my_image_rect.height:
            #     print("i clicked the rock")
            # else:
            #     print("no rock....")
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords): 
                print ("you clicked on rock !")
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False
            elif paper_image_rect.collidepoint(mouse_coords):
                print ("you clicked on paper !")
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors !")
                if GAMEOVER == False:
                    GAMEOVER = True
                else:
                    GAMEOVER = False
            else: 
                print ("you didn't click on anything")
        
    ########### get user input ##########
    ########### update ############
    if rock_image_rect.y < 300 and not GAMEOVER:
            rock_image_rect.y += 1
    if paper_image_rect.y < 300 and not GAMEOVER: 
        paper_image_rect.x += 1 
    if scissors_image_rect.y < 300 and not GAMEOVER:
        scissors_image_rect.x += 1 
        scissors_image_rect.y += 1 
   
    # draw
    screen.fill(BLACK)
    if not GAMEOVER:
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
    
    # this is where the rock is drawn on the screen
    screen.blit(rock_image, rock_image_rect)
    pg.display.flip()
    screen.blit(paper_image, paper_image_rect)
    pg.display.flip()
    screen.blit(scissors_image, scissors_image_rect)
    pg.display.flip()