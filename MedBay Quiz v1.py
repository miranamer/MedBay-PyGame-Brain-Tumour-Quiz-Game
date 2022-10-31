# .\env\Scripts\activate
# python3 -m pip install lib_name

from copyreg import dispatch_table
from tkinter.tix import Tree
from matplotlib.pyplot import draw
import pygame as pg
import os

pg.init()

WIDTH, HEIGHT = 800, 600

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("New_Game - V1")

FPS = 60



def display_score():
    curr_time = int(pg.time.get_ticks() / 1000) - start_time
    score_surf = title_text.render(f'Time: {curr_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (720, 580))
    WIN.blit(score_surf, score_rect)
    #print(curr_time, start_time) <--- For testing time

start_time = 0

brain_img = pg.image.load('Assets/brain_vector.png') # left brain img
brain_img = pg.transform.scale(brain_img, (80, 90))

brain_img2 = pg.image.load('Assets/brain_vector.png') # right brain img
brain_img2 = pg.transform.scale(brain_img, (80, 90))
brain_img2 = pg.transform.flip(brain_img2, True, False)

title_text = pg.font.Font(None, 45)
text_surf = title_text.render('Troublesome', False, 'Red') # Troublesome

title_text2 = pg.font.Font(None, 45)
text_surf2 = title_text.render('Tumours', False, 'Red') # Tumours

brain_scan =pg.image.load('Assets/brain_t_scan_pg.jpeg') # Brain Scan img
brain_scan = pg.transform.scale(brain_scan, (200, 220))

def draw_intro(): # intro screen
    WIN.fill((0, 0, 0))
    display_score()

def draw_window(): # Q1
    WIN.fill((255, 255, 255)) # white bg
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_scan, (290, 180))
    display_score()
    
    pg.display.update()

def draw_window_2(): # Q2
    pass

def draw_window_3(): # Q3
    pass

def draw_end_game(): # end game screen
    pass

#if not game_active:
                #if event.type == pg.KEYDOWN and event.type == pg.K_SPACE:
                    #game_active = True

            #if game_active:
                #draw_window()
            #else:
                #WIN.fill(0, 0, 0)


def main():

    game_active = False
    clock = pg.time.Clock()
    run = True

    while run:

        for event in pg.event.get():
            clock.tick(FPS)
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN and game_active == False:
                #print('KD')
                game_active = True
                start_time = pg.time.get_ticks()  # <------- THIS DOES NOT WORK. I DONT KNOW WHY?. I WANT TIME TO RESET TO 0 AFTER GAME BEGINS.

            if game_active:
                draw_window()
            else:
                WIN.fill((0, 0, 0)) # <---- INTRO SCREEN GUI
    
    
    
    pg.quit()



# create intro screen
# ans = ['Y', 'Y', 'N'] => q ans'
# user_ans = [] => ans that user inputs
# Q = 0
# User_Score = 0 => users score

# if user_input == pg.K_Y:
    # user_ans.append('Y')
# elif user_input == pg.K_N:
    # user_ans.append('N')

# draw_window() => for q 1
# def draw_window_2() => for q 2
# def draw_window_3() => for q 3
# if Q == 4:
    # for i, v in enumerate(user_ans):
        # if v == ans[i]:
            # User_Score += 1
    # def end_screen() # => end of game screen showing score


if __name__ == "__main__":
    main()
