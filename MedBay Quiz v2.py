# .\env\Scripts\activate
# python3 -m pip install lib_name
# D:\Stuff\melon_honey


import pygame as pg
import os

pg.init()

WIDTH, HEIGHT = 800, 600

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Staff Training Quiz")

FPS = 60

fontObj = pg.font.Font('D:/Stuff/melon_honey/Melon Honey.ttf', 30) # ADD THIS FONT TO ALL TEXT

def display_score():
    curr_time = int(pg.time.get_ticks() / 1000) - start_time
    score_surf = title_text.render(f'Time: {curr_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (720, 580))
    WIN.blit(score_surf, score_rect)
    #print(curr_time, start_time) <--- For testing time


def display_q_num(q_num):
    q_surf = title_text.render(f'Q: {q_num}', False, (64,64,64))
    q_rect = q_surf.get_rect(center = (40, 580))
    WIN.blit(q_surf, q_rect)


def display_user_score(user_score):
    us_surf = fontObj.render(f'Your Score: {user_score}', False, (64,64,64))
    us_rect = us_surf.get_rect(center = (380, 580))
    WIN.blit(us_surf, us_rect)


def display_user_score_2(user_score): # <----------- Add some stuff like accuracy (score / total * 100) or add a quote like 'very good' if good score
    fontObj2 = pg.font.Font('D:/Stuff/melon_honey/Melon Honey.ttf', 55)

    end_surf = fontObj2.render('Game Over', False, (64, 64, 64))
    end_rect = end_surf.get_rect(center = (380, 100))



    us_surf = fontObj2.render(f'Final Score: {user_score} / 4', False, (64,64,64))
    us_rect = us_surf.get_rect(center = (380, 270))
    WIN.blit(us_surf, us_rect)
    WIN.blit(end_surf, end_rect)

    

start_time = 0

brain_img = pg.image.load('Assets/brain_vector.png') # left brain img
brain_img = pg.transform.scale(brain_img, (80, 90))

brain_img2 = pg.image.load('Assets/brain_vector.png') # right brain img
brain_img2 = pg.transform.scale(brain_img, (80, 90))
brain_img2 = pg.transform.flip(brain_img2, True, False)

title_text = pg.font.Font(None, 45)
title_text_2 = pg.font.Font(None, 30)
text_surf = title_text.render('Troublesome', False, 'Red') # Troublesome

title_text2 = pg.font.Font(None, 45)
text_surf2 = title_text.render('Tumours', False, 'Red') # Tumours

brain_scan =pg.image.load('Assets/brain_t_scan_pg.jpeg') # Brain Scan img
brain_scan = pg.transform.scale(brain_scan, (200, 220))


intro_surf = title_text.render('Welcome To Troublesome Tumours!', False, 'Red')
intro_rect = intro_surf.get_rect(center = (400, 300))

intro_surf_2 = fontObj.render('-Press Space To Start-', False, 'Yellow')
intro_rect_2 = intro_surf.get_rect(center = (495, 350))



def draw_intro(intro_surf, intro_rect): # intro screen
    WIN.fill((0, 0, 0))
    WIN.blit(intro_surf, intro_rect)
    WIN.blit(intro_surf_2, intro_rect_2)
    pg.display.update()
    

def draw_window(Q, user_score): # Q1
    WIN.fill((255, 255, 255)) # white bg
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_scan, (290, 180))
    display_score()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()

def draw_window_2(Q, user_score): # Q2
    WIN.fill((0, 0, 255)) # blue bg <--------------- bg changes to blue so I know it went to next question
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_scan, (290, 180))
    display_score()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()

def draw_window_3(Q, user_score): # Q3
    WIN.fill((51, 255, 153)) # green bg
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_scan, (290, 180))
    display_score()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()

def draw_window_4(Q, user_score):
    WIN.fill((255, 204, 255)) # green bg
    WIN.blit(brain_img, (200,35))
    WIN.blit(brain_img2, (500, 35))
    WIN.blit(text_surf, (300, 45))
    WIN.blit(text_surf2, (330, 80))
    WIN.blit(brain_scan, (290, 180))
    display_score()
    display_q_num(Q)
    display_user_score(user_score)
    
    pg.display.update()


def draw_end_game(user_score): # end game screen
    WIN.fill((255, 255, 255))
    display_user_score_2(user_score)
    pg.display.update()

#if not game_active:
                #if event.type == pg.KEYDOWN and event.type == pg.K_SPACE:
                    #game_active = True

            #if game_active:
                #draw_window()
            #else:
                #WIN.fill(0, 0, 0)


def main():  # CLICK SPACE AFTER EVERY Y OR N TO REGISTER IT <----------------------------------------------------- IMPORTANT!!

    game_active = False
    clock = pg.time.Clock()
    run = True
    Q = 0 # q number
    user_ans = []
    ans = ['Y', 'Y', 'N', 'Y']
    user_score = 0

    while run:

        keys=pg.key.get_pressed()

        for event in pg.event.get():
            clock.tick(FPS)
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN and game_active == False:
                #print('KD')
                game_active = True
                start_time = pg.time.get_ticks()  # <------- THIS DOES NOT WORK. I DONT KNOW WHY?. I WANT TIME TO RESET TO 0 AFTER GAME BEGINS.
                Q += 1

            if game_active and Q == 1: # Have to press Y or N twice for it to reg on q 1 dont know why
                draw_window(Q, user_score)
                if keys[pg.K_y]:
                    user_ans.append('Y')
                    if user_ans[0] == ans[0]:
                        user_score += 1
                    Q += 1
                    break  # <-------------------- DEADLY (remove if issue arises)
                elif keys[pg.K_n]:
                    user_ans.append('N')
                    if user_ans[0] == ans[0]:
                        user_score += 1
                    Q += 1
                    break # <--------------------- DEADLY (remove if issue arises)
            
            elif game_active and Q == 2:
                draw_window_2(Q, user_score)
                if keys[pg.K_y]:
                    user_ans.append('Y')
                    if user_ans[1] == ans[1]:
                        user_score += 1
                    Q += 1
                elif keys[pg.K_n]:
                    user_ans.append('N')
                    if user_ans[1] == ans[1]:
                        user_score += 1
                    Q += 1
            
            elif game_active and Q == 3:
                draw_window_3(Q, user_score)
                if keys[pg.K_y]:
                    user_ans.append('Y')
                    if user_ans[2] == ans[2]:
                        user_score += 1
                    Q += 1
                elif keys[pg.K_n]:
                    user_ans.append('N')
                    if user_ans[2] == ans[2]:
                        user_score += 1
                    Q += 1
            
            elif game_active and Q == 4:
                draw_window_4(Q, user_score)
                if keys[pg.K_y]:
                    user_ans.append('Y')
                    if user_ans[3] == ans[3]:
                        user_score += 1
                    Q += 1
                elif keys[pg.K_n]:
                    user_ans.append('N')
                    if user_ans[3] == ans[3]:
                        user_score += 1
                    Q += 1

            

            if len(user_ans) == len(ans):
                draw_end_game(user_score)

                
            if not game_active:
                draw_intro(intro_surf, intro_rect) # <---- INTRO SCREEN GUI
            
            
    
    
    
    pg.quit()


if __name__ == "__main__":
    main()