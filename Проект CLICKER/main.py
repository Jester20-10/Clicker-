from pygame import *
import pygame
import sys
import time
import json
import os

init()
window = display.set_mode((932, 564))
display.set_caption("Капибар кликер")

my_font = font.Font(None, 36)
title_font = font.Font(None, 72)
tr_font = font.Font(None, 23)
clock = pygame.time.Clock()
FPS = 60
count = 0
per_click = 1
multiplier = 1
player_lvl = 1
water_lvl = 1
termo_lvl = 0
auto = False
feathered_friend = False
bird_level = False
king_of_birds = False
first_coins = False
rich = False
hot_springs_tycoon = False
warm_water = False
perfect_onsen = False
automation = False
relax_master = False
improver = False
perfectionist = False
store_visitor = False
patient = False
capybara_tycoon = False
cur_time = time.time()

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


training_lines = [
    'Кликай по капибаре, чтобы зарабатывать очки.       Монета  -> усиливает один клик (+1 к силе).',
    'Базовая награда: 1 очко за клик.                                 AUTO->включает автокликер если на счету 10000 очков',
    'Вверху улучшения (каждое стоит 500):                       Термометр слева -> нажми ОДИН раз для +500 очков!',
    'Птица->меняет облик капибары.                                    Нажми ESC для меню паузы.',
    'Вода->увеличивает множитель кликов (x2, x3...).     Собирай очки, открывай уровни и удачи!',
]

rect_i = img.get_rect(center=(730, 425))
rect_b = bird.get_rect(center=(290, 25))
rect_w = water.get_rect(center=(458, 23))
rect_m = money.get_rect(center=(630, 23))
rect_a = autoclick.get_rect(center=(785, 23))
rect_t = termo.get_rect(center=(40, 100))

start_btn_rect = Rect(326, 252, 290, 60)
quest_btn_rect = Rect(326, 332, 290, 60)
training_btn_rect = Rect(326, 172, 290, 60)
quest_continue_rect = Rect(326, 172, 290, 60)
quest_training_rect = Rect(326, 252, 290, 60)
state = "start"

def save_game():
    data = {"count": count, "per_click": per_click, "multiplier": multiplier, "player_lvl": player_lvl, "water_lvl": water_lvl, "termo_lvl": termo_lvl, "auto": auto}
    with open("save.json", "w") as f: json.dump(data, f)

def load_game():
    global count, per_click, multiplier, player_lvl, water_lvl, termo_lvl, auto, cur_time, img, bird, water, termo, autoclick
    if os.path.exists("save.json"):
        with open("save.json", "r") as f: s = json.load(f)
        count = s.get("count", 0)
        per_click = s.get("per_click", 1)
        multiplier = s.get("multiplier", 1)
        player_lvl = s.get("player_lvl", 1)
        water_lvl = s.get("water_lvl", 1)
        termo_lvl = s.get("termo_lvl", 0)
        auto = s.get("auto", False)
        cur_time = time.time()
        if player_lvl == 2: img = transform.scale(image.load('player 2.png'), (165, 210)); bird = transform.scale(image.load('bird 2.png'), (155, 50))
        elif player_lvl == 3: img = transform.scale(image.load('player 3.png'), (165, 210)); bird = transform.scale(image.load('bird 3.png'), (155, 50))
        elif player_lvl == 4: img = transform.scale(image.load('player 4.png'), (165, 210)); bird = transform.scale(image.load('bird 4.png'), (155, 50))
        elif player_lvl == 5: img = transform.scale(image.load('player 5.png'), (165, 210)); bird = transform.scale(image.load('bird 5.png'), (155, 50))
        if water_lvl == 2: water = transform.scale(image.load('water 2.png'), (155, 50)); termo = transform.scale(image.load('termo 2.png'), (40, 100))
        elif water_lvl == 3: water = transform.scale(image.load('water 3.png'), (155, 50)); termo = transform.scale(image.load('termo 3.png'), (40, 100))
        elif water_lvl == 4: water = transform.scale(image.load('water 4.png'), (155, 50)); termo = transform.scale(image.load('termo 4.png'), (40, 100))
        elif water_lvl == 5: water = transform.scale(image.load('water 5.png'), (155, 50)); termo = transform.scale(image.load('termo 5.png'), (40, 100))
        if auto: autoclick = transform.scale(image.load('auto_click_on.png'), (180, 80))
        else: autoclick = transform.scale(image.load('auto_click_off.png'), (180, 80))

load_game()

def format_number(count):
    suffixes = ["", 'k', 'm', 'b', 't', 'q']
    index = 0
    while count >= 1000 and index < len(suffixes) - 1:
        count /= 1000
        index += 1
    formatted = f'{count:.2f}'.rstrip('0').rstrip('.')
    return f'{formatted}{suffixes[index]}'

while True:
    keys_pressed = key.get_pressed()
    new_time = time.time()
    for e in event.get():
        if e.type == QUIT:
            save_game()
            quit()
            sys.exit()
        if e.type == KEYDOWN and e.key == K_ESCAPE:
            if state == "game":
                state = "quest"
            elif state == "quest":
                state = "game"
            elif state == "training":
                state = "quest"
                
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            if state == "start":
                if start_btn_rect.collidepoint(e.pos):
                    state = "game"
                if quest_btn_rect.collidepoint(e.pos):
                    save_game()
                    quit()
                    sys.exit()
            elif state == "game":
                if rect_b.collidepoint(e.pos):
                    if count >= 500:
                        if player_lvl == 1:
                            player_lvl += 1
                            img = transform.scale(image.load('player 2.png'), (165, 210))
                            bird = transform.scale(image.load('bird 2.png'), (155, 50))
                            count -= 500
                            save_game()
                        elif player_lvl == 2:
                            player_lvl += 1
                            img = transform.scale(image.load('player 3.png'), (165, 210))
                            bird = transform.scale(image.load('bird 3.png'), (155, 50))
                            count -= 500
                            save_game()
                        elif player_lvl == 3:
                            player_lvl += 1
                            img = transform.scale(image.load('player 4.png'), (165, 210))
                            bird = transform.scale(image.load('bird 4 .png'), (155, 50))
                            count -= 500
                            save_game()
                        elif player_lvl == 4:
                            player_lvl += 1
                            img = transform.scale(image.load('player 5.png'), (165, 210))
                            bird = transform.scale(image.load('bird 5.png'), (155, 50))
                            count -= 500
                            save_game()
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
                            save_game()
                        elif water_lvl == 2:
                            water_lvl += 1
                            termo = transform.scale(image.load('termo 3.png'), (40, 100))
                            water = transform.scale(image.load('water 3.png'), (155, 50))
                            count -= 500
                            multiplier += 1
                            save_game()
                        elif water_lvl == 3:
                            water_lvl += 1
                            termo = transform.scale(image.load('termo 4.png'), (40, 100))
                            water = transform.scale(image.load('water 4.png'), (155, 50))
                            count -= 500
                            multiplier += 1
                            save_game()
                        elif water_lvl == 4:
                            water_lvl += 1
                            termo = transform.scale(image.load('termo 5.png'), (40, 100))
                            water = transform.scale(image.load('water 5.png'), (155, 50))
                            count -= 500
                            multiplier += 1
                            save_game()
                        else:
                            count += 0
                if rect_a.collidepoint(e.pos) and count >= 5000:
                    if auto == False:
                        auto = True 
                        autoclick = transform.scale(image.load('auto_click_on.png'), (180, 80))
                        rect_a = autoclick.get_rect(center=(785, 23))
                        save_game()
                    elif auto == True:
                        autoclick = transform.scale(image.load('auto_click_off.png'), (180, 80))
                        rect_a = autoclick.get_rect(center=(785, 23))
                        auto = False
                        save_game()
                
                if rect_m.collidepoint(e.pos):
                    if count >= 500:
                        per_click += 1
                        count -= 500
                        save_game()

                if rect_t.collidepoint(e.pos):
                    if termo_lvl == 0:
                        count += 500
                        termo_lvl += 1
                        save_game()

                if rect_i.collidepoint(e.pos):
                    count += per_click * multiplier
                    save_game()

                if player_lvl == 2:
                    feathered_friend = True
                    if feathered_friend == True:
                        achievements = transform.scale(image.load('Пернатый друг.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if player_lvl == 3:
                    bird_level = True
                    if bird_level == True:
                        achievements = transform.scale(image.load('Птичий уровень.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if player_lvl == 5:
                    king_of_birds = True
                    if king_of_birds == True:
                        achievements = transform.scale(image.load('Король птиц.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if count == 100:
                    first_coins = True
                    if first_coins == True:
                        achievements = transform.scale(image.load('Первые монеты.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if count == 1000:
                    rich = True
                    if rich == True:
                        achievements = transform.scale(image.load('Богач.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if count == 10000:
                    hot_springs_tycoon = True
                    if hot_springs_tycoon == True:
                        achievements = transform.scale(image.load('Магнат горячих источников.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if water_lvl == 3:
                    warm_water = True
                    if warm_water == True:
                        achievements = transform.scale(image.load('Тёплая водичка.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if water_lvl == 5:
                    perfect_onsen = True
                    if perfect_onsen == True:
                        achievements = transform.scale(image.load('Идеальный онсэн.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if auto == True:
                    automation = True
                    if automation == True:
                        achievements = transform.scale(image.load('Автоматизация.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if new_time - cur_time == 600:
                    relax_master = True
                    if relax_master == True:
                        achievements = transform.scale(image.load('Релакс мастер.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if water_lvl == 2 or player_lvl == 2 or per_click == 2:
                    improver = True
                    if improver == True:
                        achievements = transform.scale(image.load('Улучшатор.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if water_lvl == 5 or player_lvl == 5 or per_click == 10:
                    perfectionist = True
                    if perfectionist == True:
                        achievements = transform.scale(image.load('Перфекционист.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                if new_time - cur_time == 3600:
                    patient = True
                    if relax_master == True:
                        achievements = transform.scale(image.load('Релакс мастер.png'), (165, 210))
                        window.blit(achievements, (50, 0))
                        count += 500

                    
            elif state == "quest":
                if quest_continue_rect.collidepoint(e.pos):
                    state = "game"
                if quest_training_rect.collidepoint(e.pos):
                    # background = transform.scale(image.load('bc_tr.png'), (932, 564))
                    state = "training"
                if quest_btn_rect.collidepoint(e.pos):
                    save_game()
                    quit()
                    sys.exit()



    window.blit(background, (0, 0))
    if state == "training":
        y = 180
        for line in training_lines:
            txt = tr_font.render(line, True, (255, 255, 255))
            window.blit(txt, (75, y))
            y += 40
    if new_time - cur_time >= 0.25 and auto == True:
        count += per_click * multiplier
        cur_time = new_time
    if state == "start":
        draw.rect(window, (70, 130, 180), start_btn_rect)
        btn_text = my_font.render("Начать", True, (255, 255, 255))
        btn_text_rect = btn_text.get_rect(center=start_btn_rect.center)
        window.blit(btn_text, btn_text_rect)
        draw.rect(window, (70, 130, 180), quest_btn_rect)
        btn_text_2 = my_font.render("Выйти на робочий стол", True, (255, 255, 255))
        btn_text_rect_2 = btn_text_2.get_rect(center=quest_btn_rect.center)
        window.blit(btn_text_2, btn_text_rect_2)

    elif state == "game":
        background = transform.scale(image.load('bg.png'), (932, 564))
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
    
    elif state == 'quest':
        background = transform.scale(image.load('bg.png'), (932, 564))
        draw.rect(window, (70, 130, 180), quest_continue_rect)
        btn_text = my_font.render("Продолжить", True, (255, 255, 255))
        btn_text_rect = btn_text.get_rect(center=quest_continue_rect.center)
        window.blit(btn_text, btn_text_rect)
        
        draw.rect(window, (70, 130, 180), quest_training_rect)
        btn_text_3 = my_font.render("Обучение", True, (255, 255, 255))
        btn_text_rect_3 = btn_text_3.get_rect(center=quest_training_rect.center)
        window.blit(btn_text_3, btn_text_rect_3)
        
        draw.rect(window, (70, 130, 180), quest_btn_rect)
        btn_text_4 = my_font.render("Выйти на робочий стол", True, (255, 255, 255))
        btn_text_rect_4 = btn_text_4.get_rect(center=quest_btn_rect.center)
        window.blit(btn_text_4, btn_text_rect_4)

    display.update()
    clock.tick(FPS)