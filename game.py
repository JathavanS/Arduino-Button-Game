# Simple pygame program

# Import and initialize the pygame library
import time
import serial
import pygame
import random
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1400, 800])
font = pygame.font.Font('freesansbold.ttf', 32)

DEFAULT_GHOST_SIZE = (300, 300)
AMMA_SIZE = (250,400)
STONE_SIZE = (230,400)
WATER_SIZE = (100,100)
GRASS_SIZE = (200,300)
HERO_SIZE = (300,250)
GUN_SIZE = (100,100)
HEART_SIZE = (50,50)

# Run until the user asks to quit
running = True

arduinoData = serial.Serial("COM3",9600)
time.sleep(1)

bluePng = pygame.image.load("blueGhost.png")
bluePng = pygame.transform.scale(bluePng, DEFAULT_GHOST_SIZE)

redPng = pygame.image.load("redGhost.png")
redPng = pygame.transform.scale(redPng, DEFAULT_GHOST_SIZE)

greenPng = pygame.image.load("greenGhostDark.png")
greenPng = pygame.transform.scale(greenPng, DEFAULT_GHOST_SIZE)

whitePng = pygame.image.load("whiteGhost.png")
whitePng = pygame.transform.scale(whitePng, DEFAULT_GHOST_SIZE)

yellowPng = pygame.image.load("yellowGhostDark.png")
yellowPng = pygame.transform.scale(yellowPng, DEFAULT_GHOST_SIZE)

ghostX = 100
ghostY = 450
ghostSpeed = 1


ammaJgp = pygame.image.load("image1.jpg")
ammaJgp =  pygame.transform.scale(ammaJgp, AMMA_SIZE)
ammaX = 1150
ammaY = 400

stoneJpg = pygame.image.load("stone.jpg")
stoneJpg = pygame.transform.scale(stoneJpg, STONE_SIZE)
stoneX = 0
stoneY = 400

waterJpg = pygame.image.load("water.jpg")
waterJpg = pygame.transform.scale(waterJpg, WATER_SIZE)
waterX = 0
waterY = 300

grassJpg = pygame.image.load("grass.jpg")
grassJpg = pygame.transform.scale(grassJpg, GRASS_SIZE)
grassX = 0
grassY = 0

heroPng = pygame.image.load("hero.png")
heroPng = pygame.transform.scale(heroPng, HERO_SIZE)
heroX = 550
heroY = 0

gunPng = pygame.image.load("gun.png")
gunPng = pygame.transform.scale(gunPng, GUN_SIZE)
gunPng = pygame.transform.flip(gunPng,True,False)
gunPng = pygame.transform.rotate(gunPng,75)

gunX = 470
gunY = 160

heartPng = pygame.image.load("heart.png")
heartPng = pygame.transform.scale(heartPng, HEART_SIZE)

heartX = 1330
heartY = 400

ghostLst = [[yellowPng,"Y"], [bluePng,"B"], [redPng,"R"],[greenPng,"G"], [whitePng,"W"] ]
ghostAlive = False
ghostPng = None
ghostAns = None
ghostDeathTime = None

startTime = time.time()

life = 3
score = 0

def spawnGhost():
    global ghostAlive
    global ghostAns
    global ghostPng
    global ghostX
    global ghostDeathTime

    ghostAlive= True
    ghost = random.choice(ghostLst)
    print(ghost)
    ghostPng = ghost[0]
    ghostAns = ghost[1]
    ghostX = 100
    ghostDeathTime = None




while running:

    while(arduinoData.inWaiting()==0):
        pass
    dataPacket=arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = dataPacket.strip("\r\n")
    #if(dataPacket != "E\n" and len(dataPacket) > 1):
        #running = False
    #print(dataPacket, len(dataPacket))
    if ghostAlive and  len(dataPacket) >= 1 and dataPacket[0] == ghostAns:
        print("KILL!!!!")
        score += 1
        ghostAlive = False
        ghostDeathTime = time.time()


    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
   # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    screen.blit(ammaJgp,(ammaX,ammaY))
    for i in range(life):
        screen.blit(heartPng,(heartX - 80*i,heartY))
    
    for i in range(5):
        screen.blit(stoneJpg,(stoneX + 230*i,stoneY))
    
    for i in range(14):
        screen.blit(waterJpg,(waterX + 100*i,waterY))
    for i in range(7):
        screen.blit(grassJpg,(grassX + 200*i,grassY))

    screen.blit(heroPng,(heroX,heroY))
    screen.blit(gunPng,(gunX,gunY))

    if ghostAlive:
        screen.blit(ghostPng,(ghostX,ghostY))
        print(ghostX)
    ghostX += ghostSpeed
    if ghostX > 850:
        life -= 1
        ghostAlive = False


     


    # Flip the display
    #pygame.display.flip()
    pygame.display.update()
    current_time = time.time()
    if not ghostAlive and current_time - startTime > 5:
        spawnGhost()



# Done! Time to quit.
pygame.quit()