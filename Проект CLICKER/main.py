from pygame import *
import pygame
import sys
import time

init()
window = display.set_mode((932, 564))
display.set_caption("Капибар кликер")

my_font = font.Font(None, 36)
title_font = font.Font(None, 72)
clock = pygame.time.Clock()
FPS = 60
count = 0
per_click = 1
multiplier = 1
player_lvl = 1
water_lvl = 1
termo_lvl = 0
auto = False

background = transform.scale(image.load('bg.png'), (932, 564))
img = transform.scale(image.load('player 1.png'), (165, 210))
m_background = transform.scale(image.load('main backround.png'), (932, 50))
score = transform.scale(image.load('score.png'), (200, 50))
bird = transform.scale(image.load('bird 1.png'), (155, 50))
water = transform.scale(image.load('water 1.png'), (155, 50))
money = transform.scale(image.load('money .png'), (155, 50))
shop = transform.scale(image.load('shop.png'), (63, 48))
termo = transform.scale(image.load('termo 1.png'), (40, 100))
autoclick = transform.scale(image.load('auto_click_off.png'), (180, 80))

rect_i = img.get_rect(center=(730, 425))
rect_b = bird.get_rect(center=(290, 25))
rect_w = water.get_rect(center=(458, 23))
rect_m = money.get_rect(center=(630, 23))
rect_a = autoclick.get_rect(center=(785, 23))
rect_t = termo.get_rect(center=(40, 100))

start_btn_rect = Rect(386, 282, 160, 60)
state = "start"

def  format_number(count):
    suffixes = ["", 'k', 'm', 'b', 't', 'q']
    index = 0
    while count >= 1000 and index < len(suffixes) - 1:
        count /= 1000
        index += 1
    formatted = f'{count:.2f}'.rstrip('0').rstrip('.')
    return f'{formatted}{suffixes[index]}'

start_time = time.time()
cur_time = start_time

while True:
    new_time = time.time()
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
        if e.type == MOUSEBUTTONDOWN:
            if state == "start":
                if start_btn_rect.collidepoint(e.pos):
                    state = "game"
            elif state == "game":
                if rect_b.collidepoint(e.pos):
                    if count >= 500:
                        if player_lvl == 1:
                            player_lvl += 1
                            img = transform.scale(image.load('player 2.png'), (165, 210))
                            bird = transform.scale(image.load('bird 2.png'), (155, 50))
                            count -= 500
                        elif player_lvl == 2:
                            player_lvl += 1
                            img = transform.scale(image.load('player 3.png'), (165, 210))
                            bird = transform.scale(image.load('bird 3.png'), (155, 50))
                            count -= 500
                        elif player_lvl == 3:
                            player_lvl += 1
                            img = transform.scale(image.load('player 4.png'), (165, 210))
                            bird = transform.scale(image.load('bird 4 .png'), (155, 50))
                            count -= 500
                        elif player_lvl == 4:
                            player_lvl += 1
                            img = transform.scale(image.load('player 5.png'), (165, 210))
                            bird = transform.scale(image.load('bird 5.png'), (155, 50))
                            count -= 500
                        else:
                            count += 0

                if rect_w.collidepoint(e.pos):
                    if count >= 500:
                        if water_lvl == 1:
                            water_lvl += 1
                            termo = transform.scale(image.load('termo 2.png'), (40, 100))
                            water = transform.scale(image.load('water 2.png'), (155, 50))
                            count -= 500
                            multiplier += 1
                        elif water_lvl == 2:
                            water_lvl += 1
                            termo = transform.scale(image.load('termo 3.png'), (40, 100))
                            water = transform.scale(image.load('water 3.png'), (155, 50))
                            count -= 500
                            multiplier += 1
                        elif water_lvl == 3:
                            water_lvl += 1
                            termo = transform.scale(image.load('termo 4.png'), (40, 100))
                            water = transform.scale(image.load('water 4.png'), (155, 50))
                            count -= 500
                            multiplier += 1
                        elif water_lvl == 4:
                            water_lvl += 1
                            termo = transform.scale(image.load('termo 5.png'), (40, 100))
                            water = transform.scale(image.load('water 5.png'), (155, 50))
                            count -= 500
                            multiplier += 1
                        else:
                            count += 0
                if rect_a.collidepoint(e.pos):
                    if auto == False:
                        auto = True 
                        autoclick = transform.scale(image.load('auto_click_on.png'), (180, 80))
                        
                    elif auto == True:
                        autoclick = transform.scale(image.load('auto_click_off.png'), (180, 80))
                        auto = False
                
                if rect_m.collidepoint(e.pos):
                    if count >= 500:
                        per_click += 1
                        count -= 500

                if rect_t.collidepoint(e.pos):
                    if termo_lvl == 0:
                        count += 500
                        termo_lvl += 1

                if rect_i.collidepoint(e.pos):
                    count += per_click * multiplier

    window.blit(background, (0, 0))
    if new_time - cur_time >= 0.25 and auto == True:
        count += per_click * multiplier
        cur_time = new_time
    if state == "start":
        draw.rect(window, (70, 130, 180), start_btn_rect)
        btn_text = my_font.render("Начать", True, (255, 255, 255))
        btn_text_rect = btn_text.get_rect(center=start_btn_rect.center)
        window.blit(btn_text, btn_text_rect)
    elif state == "game":
        window.blit(m_background, (0, 0))
        window.blit(score, (0, 0))
        window.blit(bird, rect_b)
        window.blit(water, rect_w)
        window.blit(money, rect_m)
        window.blit(autoclick, rect_a)
        window.blit(shop, (855, 0))
        window.blit(termo, (0, 50))
        window.blit(img, rect_i)
        window.blit(my_font.render(f"{format_number(count)}", True, (255, 255, 255)), (90, 15))

    display.update()
    clock.tick(FPS)