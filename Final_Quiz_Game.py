# .\env\Scripts\activate
# python3 -m pip install lib_name
# D:\Stuff\melon_honey


import pygame as pg
import os
from pygame import mixer
import pandas as pd

pg.init()

WIDTH, HEIGHT = 800, 600 # Screen Widht, Height

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Staff Training Quiz")

FPS = 60 # capped at 60fps


class Button(): # button class
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pg.transform.scale(image, (int(width * scale), int(height * scale))) # correct image scale
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw_bttn(self, surface): # checks if button is clicked
		action = False
		#get mouse position
		pos = pg.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pg.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		WIN.blit(self.image, (self.rect.x, self.rect.y))

		return action

start_bttn_img = pg.image.load('Assets/bttn_1_new-removebg-preview.png').convert_alpha() # start button img
stop_bttn_img = pg.image.load('Assets/bttn_2-removebg-preview.png').convert_alpha() # stop button img
yes_bttn_img = pg.image.load('Assets/yes_bttn_img.PNG').convert_alpha() # yes button img
no_bttn_img = pg.image.load('Assets/no_bttn_img.PNG').convert_alpha() # no button img

start_bttn = Button(130, 420, start_bttn_img, 0.7) # start button instance
stop_bttn = Button(540, 420, stop_bttn_img, 0.7) # stop button instance


yes_bttn = Button(240, 440, yes_bttn_img, 0.2) # yes button instance
no_bttn = Button(440, 440, no_bttn_img, 0.2) # no button instance


fontObj = pg.font.Font("Assets/alagard.ttf", 30) # ADD THIS FONT TO ALL TEXT

def display_time(): # displays time
    curr_time = int(pg.time.get_ticks() / 1000) - start_time # to ensure correct time (accounts for time taken to load)
    score_surf = fontObj.render(f'Time: {curr_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (720, 580))
    WIN.blit(score_surf, score_rect)


def display_q_num(q_num): # displays question number
    q_surf = fontObj.render(f'Q: {q_num}', False, (64,64,64))
    q_rect = q_surf.get_rect(center = (40, 580))
    WIN.blit(q_surf, q_rect)


def display_user_score(user_score): # displays user score
    us_surf = fontObj.render(f'Your Score: {user_score}', False, (64,64,64))
    us_rect = us_surf.get_rect(center = (380, 580))
    WIN.blit(us_surf, us_rect)


fontObj3 = pg.font.Font("Assets/alagard.ttf", 60)
fontObj4 = pg.font.Font("Assets/alagard.ttf", 40)


def display_user_score_2(user_score): # displays final user score
    

    end_surf = fontObj.render('Game Over', False, 'Red')
    end_rect = end_surf.get_rect(center = (395, 100))



    us_surf = fontObj3.render(f'Final Score: {user_score} / 4', False, (64,64,64))
    us_rect = us_surf.get_rect(center = (405, 270))
    WIN.blit(us_surf, us_rect)
    WIN.blit(end_surf, end_rect)


    

start_time = 0 # start time intialized to 0

brain_scan =pg.image.load('Assets/mri.jpg') # Brain Scan img
brain_scan = pg.transform.scale(brain_scan, (200, 220))
#-------------------------------------------------------------
brain_img = pg.image.load('Assets/brain_img.png') # left brain img
brain_img = pg.transform.scale(brain_img, (80, 90))

brain_img2 = pg.image.load('Assets/brain_img.png') # Right brain img
brain_img2 = pg.transform.scale(brain_img, (80, 90))
brain_img2 = pg.transform.flip(brain_img2, True, False)
#-------------------------------------------------------------
brain_img_3 = pg.image.load('Assets/brs1.jpg') # Q1 -> N
brain_img_3 = pg.transform.scale(brain_img_3, (260, 210))

brain_img_4 = pg.image.load('Assets/brs2.jpg') # Q1 -> N
brain_img_4 = pg.transform.scale(brain_img_4, (200, 210))

brain_img_5 = pg.image.load('Assets/brs3.jpg') # Q3 -> Y
brain_img_5 = pg.transform.scale(brain_img_5, (200, 210))

brain_img_6 = pg.image.load('Assets/brs4.jpg') # Q4 -> N
brain_img_6 = pg.transform.scale(brain_img_6, (200, 210))
#--------------------------------------------------------------
medbay_logo = pg.image.load('Assets/image.png') # medbay logo
medbay_logo = pg.transform.scale(medbay_logo, (290, 200))
#--------------------------------------------------------------
pixel_brain = pg.image.load('Assets/pixel_brain.png') # pixel brain img
pixel_brain = pg.transform.scale(pixel_brain, (160, 150))




text_surf = fontObj.render('Troublesome', False, (255, 0, 0)) # Troublesome
text_surf2 = fontObj.render('Tumours', False, (0, 0, 245)) # Tumours

intro_surf = fontObj4.render('Welcome To Troublesome Tumours!', False, (255,0,0)) # welcome text
intro_rect = intro_surf.get_rect(center = (400, 200))

intro_surf_2 = fontObj4.render('Created By Miran Amer (2022)', False, (0, 0, 254)) # created by text
intro_rect_2 = intro_surf.get_rect(center = (455, 300))

game_logo = pg.image.load('Assets/game_logo.png') # game logo
game_logo = pg.transform.scale(game_logo, (WIDTH, HEIGHT))
game_logo_rect = game_logo.get_rect(topleft = (0, 0))

fontObj2 = pg.font.Font("Assets/alagard.ttf", 20)

game_q_title = fontObj2.render('Is There A Tumour?', False, (0,0,0))
game_q_rect = intro_surf.get_rect(center = (635, 155))

perf_score = fontObj4.render('Perfect :)', False, 'Green') # if score is 4/4
perf_score_rect = intro_surf.get_rect(center = (640, 380))

zero_score = fontObj4.render('Horrendous :(', False, 'Red') # if score is 0 / 4
zero_score_rect = intro_surf.get_rect(center = (585, 380))







def draw_intro(intro_surf, intro_rect, Q, game_active): # intro screen
    #WIN.blit(game_logo, game_logo_rect)
    WIN.fill((250, 248, 248))
    WIN.blit(medbay_logo, (250, 450))
    WIN.blit(pixel_brain, (310, 5))
    WIN.blit(intro_surf, intro_rect)
    WIN.blit(intro_surf_2, intro_rect_2)
    
    if start_bttn.draw_bttn(WIN) and game_active == False: # checks if start button is clicked
      button_sound_effect = mixer.Sound('Assets/laser.wav') # sound effect (currently not working and not needed)
      button_sound_effect.play()
      game_active = True
      Q += 1
    
    elif stop_bttn.draw_bttn(WIN) and game_active == False: # checks if stop button is clicked
      pg.quit()
    
    pg.display.update()
    

def draw_window(Q, user_score): # Q1
    WIN.fill((255, 255, 255)) # white bg
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(game_q_title, game_q_rect)
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_img_3, (265, 180))
    display_time()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()

def draw_window_2(Q, user_score): # Q2
    WIN.fill((255, 255, 255)) 
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(game_q_title, game_q_rect)
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_img_4, (300, 180))
    display_time()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()

def draw_window_3(Q, user_score): # Q3
    WIN.fill((255, 255, 255)) 
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(game_q_title, game_q_rect)
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_img_5, (290, 180))
    display_time()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()

def draw_window_4(Q, user_score): # Q4
    WIN.fill((255, 255, 255)) 
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(game_q_title, game_q_rect)
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_img_6, (290, 180))
    display_time()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()


def draw_end_game(user_score, written): # end game screen
    WIN.fill((255, 255, 255))
    display_user_score_2(user_score)
    if user_score == 4:
        WIN.blit(perf_score, perf_score_rect)
    elif user_score == 0:
        WIN.blit(zero_score, zero_score_rect)

    
    pg.display.update()


def main(): # main game loop

    game_active = False # game active bool to check if game is running or not
    clock = pg.time.Clock() # timer
    run = True # to run game loop
    Q = 0 # q number
    user_ans = [] # user inputs
    ans = ['N', 'N', 'Y', 'N'] # actual answers
    user_score = 0 # user score
    written = False # to add score to a file

    while run:

        keys=pg.key.get_pressed()

        for event in pg.event.get():
            clock.tick(FPS)
            if event.type == pg.QUIT:
                run = False

            
            if start_bttn.draw_bttn(WIN) and game_active == False: # start button checker
              game_active = True
              Q += 1
              

            if game_active and Q == 1: # Q1
                draw_window(Q, user_score)
                if yes_bttn.draw_bttn(WIN):  
                    user_ans.append('Y') # add 'Y' to user_ans list
                    if user_ans[0] == ans[0]: # if ans is correct
                        user_score += 1 # increment user score
                    Q += 1 # Question increment
                elif no_bttn.draw_bttn(WIN):
                    user_ans.append('N') # add 'N' to user_ans list
                    if user_ans[0] == ans[0]: # if ans is correct
                        user_score += 1 # increment user score
                    Q += 1 # Question increment
                
                pg.display.update()
               
            
            elif game_active and Q == 2:
                draw_window_2(Q, user_score)
                if yes_bttn.draw_bttn(WIN):  
                    user_ans.append('Y')
                    if user_ans[1] == ans[1]:
                        user_score += 1
                    Q += 1
                elif no_bttn.draw_bttn(WIN):
                    user_ans.append('N')
                    if user_ans[1] == ans[1]:
                        user_score += 1
                    Q += 1

                pg.display.update()
            
            elif game_active and Q == 3:
                draw_window_3(Q, user_score)
                if yes_bttn.draw_bttn(WIN):  
                    user_ans.append('Y')
                    if user_ans[2] == ans[2]:
                        user_score += 1
                    Q += 1
                elif no_bttn.draw_bttn(WIN):
                    user_ans.append('N')
                    if user_ans[2] == ans[2]:
                        user_score += 1
                    Q += 1

                pg.display.update()
            
            elif game_active and Q == 4:
                draw_window_4(Q, user_score)
                if yes_bttn.draw_bttn(WIN):  
                    user_ans.append('Y')
                    if user_ans[3] == ans[3]:
                        user_score += 1
                    Q += 1
                elif no_bttn.draw_bttn(WIN):
                    user_ans.append('N')
                    if user_ans[3] == ans[3]:
                        user_score += 1
                    Q += 1

                pg.display.update()

            #for index, value in enumerate(user_ans):
                #if value == ans[index]:
                    #user_score += 1
                #else:
                    #continue

            if len(user_ans) == len(ans):
                draw_end_game(user_score, written)
                if written == False:
                    f = open("Assets/scores.txt", "a")
                    f.write(str(user_score) + '\n')
                    f.close()
                    written = True

                    #with open('Assets/scores.txt') as q:
                        #lines = q.readlines()
                        #end_scores.append(lines)
                        #print(lines)
                

                
            if not game_active:
                draw_intro(intro_surf, intro_rect, Q, game_active) # <---- INTRO SCREEN GUI
            
    
    
    
    pg.quit()   
    


if __name__ == "__main__":
    main()