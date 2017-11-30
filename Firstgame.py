import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255) #difing colours
ugly_colour = (67, 137, 219)

pete_width = 70

gameDisplay = pygame.display.set_mode((display_width, display_height)) #make a window
pygame.display.set_caption("A bit Pete-y") #give window name
clock = pygame.time.Clock() #give game ingame clock

peteImg = pygame.image.load("Pixel_Pete.png") #load character into background
boydImg = pygame.image.load("boyd_orr.png") #load backdrop into background
APImg = pygame.image.load("AP.png") #load dealine sprite into back ground
DFImg = pygame.image.load("DF.png")
PSDImg = pygame.image.load("PSD.png")
AlgsImg = pygame.image.load("Algs.png")
ISImg = pygame.image.load("IS.png")


def boydorr(boydx, boydy):
    gameDisplay.blit(boydImg,(boydx, boydy))

#def deadlines(deadx, deady, deadw, deadh, colour): #obsticle functiuon
    #pygame.draw.rect(gameDisplay, colour, [deadx, deady, deadw, deadh])

def deadlines(sprite, position):
    gameDisplay.blit(sprite, position)

def pete(x,y):
    gameDisplay.blit(peteImg,(x,y)) #show it on the window, peteImg is parameter, x,y is a toople

def message_display(text):
    font = pygame.font.SysFont('comicsansms', 36) #it was font = pygame.font.Font('freesansbold.ttf', 90)
    gameDisplay.blit(font.render(text, True, white, black), (150,200)) #blit(font.render(text, antialias, colour),(x,y))
    pygame.display.update()

def fail():
    message_display("  Peter missed a deadline!!  ")

def message_display1(text):
    font = pygame.font.SysFont('comicsansms', 20) #it was font = pygame.font.Font('freesansbold.ttf', 90)
    gameDisplay.blit(font.render(text, True, white, black), (250, 240)) #blit(font.render(text, antialias, colour),(x,y))
    pygame.display.update()
    time.sleep(2) #let it display for 2 seconds

    game_loop()

def hit(number_of_hit): #pass though the number of hits
    message_display1("  Peter hit: " + str(number_of_hit) + " deadlines.  ")

def game_loop():
    CS_sprites = random.choice([APImg, DFImg, PSDImg, AlgsImg, ISImg])
    num_hit = 0
    x = (display_width * 0.45)
    y = (display_height * 0.83) #plop him around middle of screen

    x_change = 0 #define change for counting

    deadlines_width = 100
    deadlines_height = 100
    deadlines_startx = random.randrange(0, (display_width - deadlines_width))
    deadlines_starty = -600
    deadlines_speed = 6

    gameExit = False

    while not gameExit: #event quitting loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Did somebody click the X button?
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN: #Was there a keypress?
               if event.key == pygame.K_LEFT:
                   x_change = -6
               elif event.key == pygame.K_RIGHT:
                   x_change = 6
            if event.type == pygame.KEYUP: #Don't need to continuously press. Can hold it.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change #change position of peter

        boydorr(0,0) #make background the boyd orr
        #deadlines(deadlines_startx, deadlines_starty, deadlines_width, deadlines_height, ugly_colour) #deadlines(deadx, deady, deadw, deadh, color)
        deadlines(CS_sprites, (deadlines_startx, deadlines_starty))
        deadlines_starty += deadlines_speed #add 7 to y position every loop
        pete(x,y)

        if x > display_width - pete_width or x < 0:
            x_change = 0 #do the crash funct which shows message

        if y < deadlines_starty + deadlines_height: #is bottom corner lower than pete
            if x > deadlines_startx and x < deadlines_startx + deadlines_width or x + pete_width > deadlines_startx and x + pete_width < deadlines_startx + deadlines_width:
                deadlines_starty = 0 - deadlines_height
                deadlines_startx = random.randrange(0, display_width - deadlines_width)
                num_hit += 1
                CS_sprites = random.choice([APImg, DFImg, PSDImg, AlgsImg, ISImg])
                print(num_hit)
                if num_hit%5 == 0:
                    deadlines_speed += 1


            if deadlines_starty > display_height - deadlines_height/3:
                fail()
                hit(num_hit)

        pygame.display.update()
        clock.tick(60) #frames per second

game_loop()
pygame.quit()
quit()
