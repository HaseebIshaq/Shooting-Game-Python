# # pygame is library to build games in python
# import pygame
# import random
# import math
# import time
# from pygame import mixer #module to play sounds/music/audio in python

# #initializing the pygame
# # safely initalizes all imported pygame modules regardless eventhough module is not in Use
# # it saves the trouble of manually initialising each module
# pygame.init()

# #create screen
# # width x height 
# screen=pygame.display.set_mode((800,600))

# #background
# background=pygame.image.load('background.jpg')

# #backgroud music
# # pygame.mixer.music.load()
# mixer.music.load('background song.mp3')
# mixer.music.play(-1) #music plays infinitely

# #player (shooter)
# playerImg=pygame.image.load('space-invaders.png')
# # initialising position of shooter by setting coordinates
# playerX=370
# playerY=480
# #vel is width of moving the shooter (by 2 in this case)
# vel=2

# #placing the shooter (image) on the screen
# def player(x,y):
#     # first parameter source and coordinates as second
#     screen.blit(playerImg,(x,y))

# #enemy
# # 7 enemies at a time
# enemyImg=[]
# enemyX=[]
# enemyY=[]
# enemy_vel=[]
# num_enemy=7
# for i in range(num_enemy):
#     enemyImg.append(pygame.image.load('enemy.png'))
#     enemyX.append(random.randint(0,736))
#     enemyY.append(random.randint(50,100))
#     # movement distance in vel
#     enemy_vel.append(0.25)

# def enemy(x,y,i):
#     screen.blit(enemyImg[i],(x,y))

# #bullet
# bulletImg=pygame.image.load('bullet.png')
# bulletX=370
# bulletY=480
# # movement frequency
# bullet_vel=8

# def fire_bullet(x,y):
#     # bullets allignment with the shooter
#     screen.blit(bulletImg,(x+16,y+10))

# #writing score
# score=0
# #first argument is font style and second is size
# font=pygame.font.SysFont(None,32)
# def show_score():
#     #true indicates bold and after that color code
#     text=font.render('SCORE: '+ str(score),True,(0,255,0))
#     screen.blit(text,(0,0))
    
# #game over text
# over_font=pygame.font.SysFont(None,68)
# def game_over():
#     game_over_text=over_font.render('GAME OVER YOUR SCORE IS: '+ str(score) ,True,(0,0,0))
#     screen.blit(game_over_text,(20,300))
    

# def collision(enemyX,enemyY,bulletX,bulletY):
#     # distance formula between bullet and enemy
#     dis=math.sqrt((math.pow(enemyX+5-bulletX,2))+(math.pow(enemyY+5-bulletY,2)))
#     if dis<27:
#         return True
#     else:
#         return False
    
# #caption and icon
# pygame.display.set_caption('SPACE INVADERS')
# icon=pygame.image.load('ufo.png')
# pygame.display.set_icon(icon)

# # game loop
# running=True
# time.sleep(2)
# while running:
#     # drawing    
#     # color code in fill  
#     screen.fill((0,0,0))
#     # blit is pasting image
#     screen.blit(background,(0,0))
#     show_score()
#     for event in pygame.event.get():
#         # cross pressed on top right corner to quit
#         if event.type==pygame.QUIT:
#             running=False      

#     #enemy movement
#     for i in range(num_enemy):
#         # Reached to screen bottom
#         if enemyY[i]>560:
#             game_over()
#             running=False
#         enemyY[i]+=enemy_vel[i]

#         # if enemyY[i]>600:
#         #     enemyX[i]=random.randint(0,736)
#         #     enemyY[i]=random.randint(50,100)
#         is_collision=collision(enemyX[i],enemyY[i],bulletX,bulletY)
#         if is_collision:
#             bulletY=480
#             enemyX[i]=random.randint(0,736)
#             enemyY[i]=random.randint(50,100)
#             score+=1
            
#         enemy(enemyX[i],enemyY[i],i)
#     #bullet movement
#     bulletY-=bullet_vel
#     # path crossed so bullet re generated
#     if bulletY<100:
#         bulletY=480

    
#     keys=pygame.key.get_pressed()  # pressed
#     if keys[pygame.K_LEFT] and playerX>0: # left movement
#         playerX-=vel
#         bulletX-=vel
#     if keys[pygame.K_RIGHT] and playerX<736: # right movement
#         playerX+=vel
#         bulletX+=vel
    


    

#     player(playerX,playerY)
#     fire_bullet(bulletX,bulletY)
#     pygame.display.update() # changes being updated

# time.sleep(4)
# pygame.quit()

color_list = ["white","red","black"]
print(color_list[0] , "and" , color_list[-1])

word = 'flabbergasted'
for i in word:
    print (i)