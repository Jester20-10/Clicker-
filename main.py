from pygame import *
import pygame
import sys
import time
import json
import os
import random

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

reward_feathered_friend = False
reward_bird_level = False
reward_king_of_birds = False
reward_first_coins = False
reward_rich = False
reward_hot_springs_tycoon = False
reward_warm_water = False
reward_perfect_onsen = False
reward_automation = False
reward_relax_master = False
reward_improver = False
reward_perfectionist = False
reward_patient = False
reward_store_visitor = False
reward_capybara_tycoon = False

notification_texts = []
notification_times = []

cur_time = time.time()
session_start_time = time.time()
saved_playtime = 0

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

ach_feathered = transform.scale(image.load('Пернатый друг.png'), (45, 45))
ach_bird = transform.scale(image.load('Птичий уровень.png'), (45, 45))
ach_king = transform.scale(image.load('Король птиц.png'), (45, 45))
ach_first = transform.scale(image.load('Первые монеты.png'), (45, 45))
ach_rich = transform.scale(image.load('Богач.png'), (45, 45))
ach_tycoon = transform.scale(image.load('Магнат горячих источников.png'), (45, 45))
ach_warm = transform.scale(image.load('Тёплая водичка.png'), (45, 45))
ach_onsen = transform.scale(image.load('Идеальный онсэн.png'), (45, 45))
ach_auto = transform.scale(image.load('Автоматизация.png'), (45, 45))
ach_relax = transform.scale(image.load('Релакс мастер.png'), (45, 45))
ach_improve = transform.scale(image.load('Улучшатор.png'), (45, 45))
ach_perfect = transform.scale(image.load('Перфекционист.png'), (45, 45))
ach_patient = transform.scale(image.load('Терпеливый.png'), (45, 45))
ach_store = transform.scale(image.load('Посетитель магазина.png'), (45, 45))
ach_cap = transform.scale(image.load('Капибара-магнат.png'), (45, 45))

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
quest_btn_rect = Rect(326, 410, 290, 60)
quest_continue_rect = Rect(326, 110, 290, 60)
quest_training_rect = Rect(326, 180, 290, 60)
quest_achievements_rect = Rect(326, 250, 290, 60)
achievements_back_rect = Rect(366, 500, 200, 50)
training_back_rect = Rect(366, 500, 200, 50)
state = "start"

def save_game():
    current_total = saved_playtime + (time.time() - session_start_time)
    data = {
        "count": count, "per_click": per_click, "multiplier": multiplier, 
        "player_lvl": player_lvl, "water_lvl": water_lvl, "termo_lvl": termo_lvl, 
        "reward_feathered_friend": reward_feathered_friend, "reward_bird_level": reward_bird_level, 
        "reward_king_of_birds": reward_king_of_birds, "reward_first_coins": reward_first_coins, 
        "reward_rich": reward_rich, "reward_hot_springs_tycoon": reward_hot_springs_tycoon, 
        "reward_warm_water": reward_warm_water, "reward_perfect_onsen": reward_perfect_onsen, 
        "reward_automation": reward_automation, "reward_relax_master": reward_relax_master, 
        "reward_improver": reward_improver, "reward_perfectionist": reward_perfectionist, 
        "reward_patient": reward_patient, "reward_store_visitor": reward_store_visitor, 
        "reward_capybara_tycoon": reward_capybara_tycoon, 
        "total_playtime": current_total
    }
    with open("save.json", "w") as f: 
        json.dump(data, f)

def load_game():
    global count, per_click, multiplier, player_lvl, water_lvl, termo_lvl, auto, cur_time, img, bird, water, termo, autoclick
    global reward_feathered_friend, reward_bird_level, reward_king_of_birds, reward_first_coins, reward_rich
    global reward_hot_springs_tycoon, reward_warm_water, reward_perfect_onsen, reward_automation, reward_relax_master
    global reward_improver, reward_perfectionist, reward_patient, reward_store_visitor, reward_capybara_tycoon, saved_playtime, session_start_time
    if os.path.exists("save.json"):
        with open("save.json", "r") as f: 
            s = json.load(f)
        count = s.get("count", 0)
        per_click = s.get("per_click", 1)
        multiplier = s.get("multiplier", 1)
        player_lvl = s.get("player_lvl", 1)
        water_lvl = s.get("water_lvl", 1)
        termo_lvl = s.get("termo_lvl", 0)
        reward_feathered_friend = s.get("reward_feathered_friend", False)
        reward_bird_level = s.get("reward_bird_level", False)
        reward_king_of_birds = s.get("reward_king_of_birds", False)
        reward_first_coins = s.get("reward_first_coins", False)
        reward_rich = s.get("reward_rich", False)
        reward_hot_springs_tycoon = s.get("reward_hot_springs_tycoon", False)
        reward_warm_water = s.get("reward_warm_water", False)
        reward_perfect_onsen = s.get("reward_perfect_onsen", False)
        reward_automation = s.get("reward_automation", False)
        reward_relax_master = s.get("reward_relax_master", False)
        reward_improver = s.get("reward_improver", False)
        reward_perfectionist = s.get("reward_perfectionist", False)
        reward_patient = s.get("reward_patient", False)
        reward_store_visitor = s.get("reward_store_visitor", False)
        reward_capybara_tycoon = s.get("reward_capybara_tycoon", False)
        saved_playtime = s.get("total_playtime", 0)
        session_start_time = time.time()
        cur_time = time.time()
        if player_lvl == 2: 
            img = transform.scale(image.load('player 2.png'), (165, 210))
            bird = transform.scale(image.load('bird 2.png'), (155, 50))
        elif player_lvl == 3: 
            img = transform.scale(image.load('player 3.png'), (165, 210))
            bird = transform.scale(image.load('bird 3.png'), (155, 50))
        elif player_lvl == 4: 
            img = transform.scale(image.load('player 4.png'), (165, 210))
            bird = transform.scale(image.load('bird 4.png'), (155, 50))
        elif player_lvl == 5: 
            img = transform.scale(image.load('player 5.png'), (165, 210))
            bird = transform.scale(image.load('bird 5.png'), (155, 50))
        if water_lvl == 2: 
            water = transform.scale(image.load('water 2.png'), (155, 50))
            termo = transform.scale(image.load('termo 2.png'), (40, 100))
        elif water_lvl == 3: 
            water = transform.scale(image.load('water 3.png'), (155, 50))
            termo = transform.scale(image.load('termo 3.png'), (40, 100))
        elif water_lvl == 4: 
            water = transform.scale(image.load('water 4.png'), (155, 50))
            termo = transform.scale(image.load('termo 4.png'), (40, 100))
        elif water_lvl == 5: 
            water = transform.scale(image.load('water 5.png'), (155, 50))
            termo = transform.scale(image.load('termo 5.png'), (40, 100))
        if auto: 
            autoclick = transform.scale(image.load('auto_click_on.png'), (180, 80))
        else: 
            autoclick = transform.scale(image.load('auto_click_off.png'), (180, 80))

load_game()

def format_number(count):
    suffixes = ["", 'k', 'm', 'b', 't', 'q']
    index = 0
    while count >= 1000 and index < len(suffixes) - 1:
        count /= 1000
        index += 1
    formatted = f'{count:.2f}'.rstrip('0').rstrip('.')
    return f'{formatted}{suffixes[index]}'
flag = False
ship_rd = 0

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
                background = transform.scale(image.load('bg.png'), (932, 564))
            elif state == "quest":
                state = "game"
                background = transform.scale(image.load('bg.png'), (932, 564))
            elif state == "training":
                state = "quest"
                background = transform.scale(image.load('bg.png'), (932, 564))
            elif state == "achievements":
                state = "quest"
                background = transform.scale(image.load('bg.png'), (932, 564))
                
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            if state == "start":
                if start_btn_rect.collidepoint(e.pos):
                    state = "game"
                    background = transform.scale(image.load('bg.png'), (932, 564))
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
                            bird = transform.scale(image.load('bird 4.png'), (155, 50))
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
                if flag == True:
                    if rect_s.collidepoint(e.pos):
                        if ship_rd != 0:
                            ship_rd = 0
                            count += 500
                            flag = False
                    
            elif state == "quest":
                if quest_continue_rect.collidepoint(e.pos):
                    state = "game"
                    background = transform.scale(image.load('bg.png'), (932, 564))
                if quest_training_rect.collidepoint(e.pos):
                    background = transform.scale(image.load('bc_tr.png'), (932, 564))
                    state = "training"
                if quest_achievements_rect.collidepoint(e.pos):
                    background = transform.scale(image.load('bc_tr.png'), (932, 564))
                    state = "achievements"
                if quest_btn_rect.collidepoint(e.pos):
                    save_game()
                    quit()
                    sys.exit()
            elif state == "training":
                if training_back_rect.collidepoint(e.pos):
                    state = "quest"
                    background = transform.scale(image.load('bg.png'), (932, 564))
            elif state == "achievements":
                if achievements_back_rect.collidepoint(e.pos):
                    state = "quest"
                    background = transform.scale(image.load('bg.png'), (932, 564))

    if new_time - cur_time >= 0.25 and auto == True:
        count += per_click * multiplier
        cur_time = new_time

    if new_time - cur_time >= 60:
        ship_pr  = random.randint(1, 10)
        if ship_pr == 8:
            if ship_rd == 0:
                ship_rd = random.randint(1, 3)  
            flag = True 
            
        cur_time = new_time

    playtime = saved_playtime + (new_time - session_start_time)
    
    if playtime >= 600 and not reward_relax_master:
        relax_master = True
        reward_relax_master = True
        count += 500
        notification_texts.append("Релакс мастер")
        notification_times.append(new_time)

    if playtime >= 3600 and not reward_patient:
        patient = True
        reward_patient = True
        count += 500
        notification_texts.append("Терпеливый")
        notification_times.append(new_time)

    if player_lvl == 2 and not reward_feathered_friend:
        feathered_friend = True
        reward_feathered_friend = True
        count += 500
        notification_texts.append("Пернатый друг")
        notification_times.append(new_time)

    if player_lvl == 3 and not reward_bird_level:
        bird_level = True
        reward_bird_level = True
        count += 500
        notification_texts.append("Птичий уровень")
        notification_times.append(new_time)

    if player_lvl == 5 and not reward_king_of_birds:
        king_of_birds = True
        reward_king_of_birds = True
        count += 500
        notification_texts.append("Король птиц")
        notification_times.append(new_time)

    if count >= 100 and not reward_first_coins:
        first_coins = True
        reward_first_coins = True
        count += 500
        notification_texts.append("Первые монеты")
        notification_times.append(new_time)

    if count >= 1000 and not reward_rich:
        rich = True
        reward_rich = True
        count += 500
        notification_texts.append("Богач")
        notification_times.append(new_time)

    if count >= 10000 and not reward_hot_springs_tycoon:
        hot_springs_tycoon = True
        reward_hot_springs_tycoon = True
        count += 500
        notification_texts.append("Магнат горячих источников")
        notification_times.append(new_time)

    if count >= 100000 and not reward_capybara_tycoon:
        capybara_tycoon = True
        reward_capybara_tycoon = True
        count += 500
        notification_texts.append("Капибара-магнат")
        notification_times.append(new_time)

    if water_lvl == 3 and not reward_warm_water:
        warm_water = True
        reward_warm_water = True
        count += 500
        notification_texts.append("Тёплая водичка")
        notification_times.append(new_time)

    if water_lvl == 5 and not reward_perfect_onsen:
        perfect_onsen = True
        reward_perfect_onsen = True
        count += 500
        notification_texts.append("Идеальный онсэн")
        notification_times.append(new_time)

    if auto == True and not reward_automation:
        automation = True
        reward_automation = True
        count += 500
        notification_texts.append("Автоматизация")
        notification_times.append(new_time)

    if (water_lvl == 2 or player_lvl == 2 or per_click == 2) and not reward_improver:
        improver = True
        reward_improver = True
        count += 500
        notification_texts.append("Улучшатор")
        notification_times.append(new_time)

    if (water_lvl == 5 or player_lvl == 5 or per_click == 10) and not reward_perfectionist:
        perfectionist = True
        reward_perfectionist = True
        count += 500
        notification_texts.append("Перфекционист")
        notification_times.append(new_time)

    if (player_lvl > 1 or water_lvl > 1 or per_click > 1) and not reward_store_visitor:
        store_visitor = True
        reward_store_visitor = True
        count += 500
        notification_texts.append("Посетитель магазина")
        notification_times.append(new_time)

    window.blit(background, (0, 0))
    
    if state == "training":
        y = 180
        for line in training_lines:
            txt = tr_font.render(line, True, (255, 255, 255))
            window.blit(txt, (75, y))
            y += 40
        draw.rect(window, (70, 130, 180), training_back_rect)
        window.blit(my_font.render("Назад", True, (255, 255, 255)), my_font.render("Назад", True, (255, 255, 255)).get_rect(center=training_back_rect.center))

    elif state == "achievements":
        unlocked = 0
        if reward_feathered_friend: unlocked += 1
        if reward_bird_level: unlocked += 1
        if reward_king_of_birds: unlocked += 1
        if reward_first_coins: unlocked += 1
        if reward_rich: unlocked += 1
        if reward_hot_springs_tycoon: unlocked += 1
        if reward_capybara_tycoon: unlocked += 1
        if reward_warm_water: unlocked += 1
        if reward_perfect_onsen: unlocked += 1
        if reward_automation: unlocked += 1
        if reward_relax_master: unlocked += 1
        if reward_improver: unlocked += 1
        if reward_perfectionist: unlocked += 1
        if reward_patient: unlocked += 1
        if reward_store_visitor: unlocked += 1

        window.blit(title_font.render(f"Достижения: {unlocked}/15", True, (255, 215, 0)), (250, 20))

        y = 80
        if reward_feathered_friend:
            window.blit(ach_feathered, (50, y))
            window.blit(tr_font.render("Пернатый друг", True, (0, 255, 0)), (105, y + 5))
            window.blit(tr_font.render("Получите 2 уровень капибары", True, (0, 255, 0)), (105, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (50, y, 45, 45))
            window.blit(tr_font.render("Пернатый друг", True, (100, 100, 100)), (105, y + 5))
            window.blit(tr_font.render("Получите 2 уровень капибары", True, (100, 100, 100)), (105, y + 25))
        y += 45

        if reward_bird_level:
            window.blit(ach_bird, (50, y))
            window.blit(tr_font.render("Птичий уровень", True, (0, 255, 0)), (105, y + 5))
            window.blit(tr_font.render("Получите 3 уровень капибары", True, (0, 255, 0)), (105, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (50, y, 45, 45))
            window.blit(tr_font.render("Птичий уровень", True, (100, 100, 100)), (105, y + 5))
            window.blit(tr_font.render("Получите 3 уровень капибары", True, (100, 100, 100)), (105, y + 25))
        y += 45

        if reward_king_of_birds:
            window.blit(ach_king, (50, y))
            window.blit(tr_font.render("Король птиц", True, (0, 255, 0)), (105, y + 5))
            window.blit(tr_font.render("Получите 5 уровень капибары", True, (0, 255, 0)), (105, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (50, y, 45, 45))
            window.blit(tr_font.render("Король птиц", True, (100, 100, 100)), (105, y + 5))
            window.blit(tr_font.render("Получите 5 уровень капибары", True, (100, 100, 100)), (105, y + 25))
        y += 45

        if reward_first_coins:
            window.blit(ach_first, (50, y))
            window.blit(tr_font.render("Первые монеты", True, (0, 255, 0)), (105, y + 5))
            window.blit(tr_font.render("Накопите 100 очков", True, (0, 255, 0)), (105, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (50, y, 45, 45))
            window.blit(tr_font.render("Первые монеты", True, (100, 100, 100)), (105, y + 5))
            window.blit(tr_font.render("Накопите 100 очков", True, (100, 100, 100)), (105, y + 25))
        y += 45

        if reward_rich:
            window.blit(ach_rich, (50, y))
            window.blit(tr_font.render("Богач", True, (0, 255, 0)), (105, y + 5))
            window.blit(tr_font.render("Накопите 1000 очков", True, (0, 255, 0)), (105, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (50, y, 45, 45))
            window.blit(tr_font.render("Богач", True, (100, 100, 100)), (105, y + 5))
            window.blit(tr_font.render("Накопите 1000 очков", True, (100, 100, 100)), (105, y + 25))
        y += 45

        if reward_hot_springs_tycoon:
            window.blit(ach_tycoon, (50, y))
            window.blit(tr_font.render("Магнат горячих источников", True, (0, 255, 0)), (105, y + 5))
            window.blit(tr_font.render("Накопите 10000 очков", True, (0, 255, 0)), (105, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (50, y, 45, 45))
            window.blit(tr_font.render("Магнат горячих источников", True, (100, 100, 100)), (105, y + 5))
            window.blit(tr_font.render("Накопите 10000 очков", True, (100, 100, 100)), (105, y + 25))
        y += 45

        if reward_capybara_tycoon:
            window.blit(ach_cap, (50, y))
            window.blit(tr_font.render("Капибара-магнат", True, (0, 255, 0)), (105, y + 5))
            window.blit(tr_font.render("Накопите 100000 очков", True, (0, 255, 0)), (105, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (50, y, 45, 45))
            window.blit(tr_font.render("Капибара-магнат", True, (100, 100, 100)), (105, y + 5))
            window.blit(tr_font.render("Накопите 100000 очков", True, (100, 100, 100)), (105, y + 25))
        y += 45

        y = 80
        if reward_warm_water:
            window.blit(ach_warm, (480, y))
            window.blit(tr_font.render("Тёплая водичка", True, (0, 255, 0)), (535, y + 5))
            window.blit(tr_font.render("Получите 3 уровень воды", True, (0, 255, 0)), (535, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (480, y, 45, 45))
            window.blit(tr_font.render("Тёплая водичка", True, (100, 100, 100)), (535, y + 5))
            window.blit(tr_font.render("Получите 3 уровень воды", True, (100, 100, 100)), (535, y + 25))
        y += 45

        if reward_perfect_onsen:
            window.blit(ach_onsen, (480, y))
            window.blit(tr_font.render("Идеальный онсэн", True, (0, 255, 0)), (535, y + 5))
            window.blit(tr_font.render("Получите 5 уровень воды", True, (0, 255, 0)), (535, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (480, y, 45, 45))
            window.blit(tr_font.render("Идеальный онсэн", True, (100, 100, 100)), (535, y + 5))
            window.blit(tr_font.render("Получите 5 уровень воды", True, (100, 100, 100)), (535, y + 25))
        y += 45

        if reward_automation:
            window.blit(ach_auto, (480, y))
            window.blit(tr_font.render("Автоматизация", True, (0, 255, 0)), (535, y + 5))
            window.blit(tr_font.render("Включите автокликер", True, (0, 255, 0)), (535, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (480, y, 45, 45))
            window.blit(tr_font.render("Автоматизация", True, (100, 100, 100)), (535, y + 5))
            window.blit(tr_font.render("Включите автокликер", True, (100, 100, 100)), (535, y + 25))
        y += 45

        if reward_relax_master:
            window.blit(ach_relax, (480, y))
            window.blit(tr_font.render("Релакс мастер", True, (0, 255, 0)), (535, y + 5))
            window.blit(tr_font.render("Играйте 10 минут", True, (0, 255, 0)), (535, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (480, y, 45, 45))
            window.blit(tr_font.render("Релакс мастер", True, (100, 100, 100)), (535, y + 5))
            window.blit(tr_font.render("Играйте 10 минут", True, (100, 100, 100)), (535, y + 25))
        y += 45

        if reward_improver:
            window.blit(ach_improve, (480, y))
            window.blit(tr_font.render("Улучшатор", True, (0, 255, 0)), (535, y + 5))
            window.blit(tr_font.render("Улучшите любую характеристику до 2 уровня", True, (0, 255, 0)), (535, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (480, y, 45, 45))
            window.blit(tr_font.render("Улучшатор", True, (100, 100, 100)), (535, y + 5))
            window.blit(tr_font.render("Улучшите любую характеристику до 2 уровня", True, (100, 100, 100)), (535, y + 25))
        y += 45

        if reward_perfectionist:
            window.blit(ach_perfect, (480, y))
            window.blit(tr_font.render("Перфекционист", True, (0, 255, 0)), (535, y + 5))
            window.blit(tr_font.render("Максимально улучшите любую характеристику", True, (0, 255, 0)), (535, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (480, y, 45, 45))
            window.blit(tr_font.render("Перфекционист", True, (100, 100, 100)), (535, y + 5))
            window.blit(tr_font.render("Максимально улучшите любую характеристику", True, (100, 100, 100)), (535, y + 25))
        y += 45

        if reward_patient:
            window.blit(ach_patient, (480, y))
            window.blit(tr_font.render("Терпеливый", True, (0, 255, 0)), (535, y + 5))
            window.blit(tr_font.render("Играйте 1 час", True, (0, 255, 0)), (535, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (480, y, 45, 45))
            window.blit(tr_font.render("Терпеливый", True, (100, 100, 100)), (535, y + 5))
            window.blit(tr_font.render("Играйте 1 час", True, (100, 100, 100)), (535, y + 25))
        y += 45

        if reward_store_visitor:
            window.blit(ach_store, (480, y))
            window.blit(tr_font.render("Посетитель магазина", True, (0, 255, 0)), (535, y + 5))
            window.blit(tr_font.render("Совершите первую покупку", True, (0, 255, 0)), (535, y + 25))
        else:
            draw.rect(window, (100, 100, 100), (480, y, 45, 45))
            window.blit(tr_font.render("Посетитель магазина", True, (100, 100, 100)), (535, y + 5))
            window.blit(tr_font.render("Совершите первую покупку", True, (100, 100, 100)), (535, y + 25))

        draw.rect(window, (70, 130, 180), achievements_back_rect)
        window.blit(my_font.render("Назад", True, (255, 255, 255)), my_font.render("Назад", True, (255, 255, 255)).get_rect(center=achievements_back_rect.center))
        
    elif state == "start":
        draw.rect(window, (70, 130, 180), start_btn_rect)
        btn_text = my_font.render("Начать", True, (255, 255, 255))
        btn_text_rect = btn_text.get_rect(center=start_btn_rect.center)
        window.blit(btn_text, btn_text_rect)
        draw.rect(window, (70, 130, 180), quest_btn_rect)
        btn_text_2 = my_font.render("Выйти на рабочий стол", True, (255, 255, 255))
        btn_text_rect_2 = btn_text_2.get_rect(center=quest_btn_rect.center)
        window.blit(btn_text_2, btn_text_rect_2)

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
        if flag == True:
            if ship_rd == 1:
                ship = transform.scale(image.load('корабль.png'), (189, 159))
                rect_s =  ship.get_rect(center=(200, 200))
                window.blit(ship, (200, 200))

            elif ship_rd == 2:
                ship = transform.scale(image.load('корабль с золотом.png'), (189, 159))
                rect_s =  ship.get_rect(center=(200, 200))
                window.blit(ship, (200, 200))

            elif ship_rd == 3:
                ship = transform.scale(image.load('богатый корабль.png'), (189, 159))
                rect_s =  ship.get_rect(center=(200, 200))
                window.blit(ship, (200, 200))
                            
        window.blit(my_font.render(f"{format_number(count)}", True, (255, 255, 255)), (90, 15))
    
    elif state == 'quest':
        draw.rect(window, (70, 130, 180), quest_continue_rect)
        btn_text = my_font.render("Продолжить", True, (255, 255, 255))
        btn_text_rect = btn_text.get_rect(center=quest_continue_rect.center)
        window.blit(btn_text, btn_text_rect)
        
        draw.rect(window, (70, 130, 180), quest_training_rect)
        btn_text_3 = my_font.render("Обучение", True, (255, 255, 255))
        btn_text_rect_3 = btn_text_3.get_rect(center=quest_training_rect.center)
        window.blit(btn_text_3, btn_text_rect_3)
        
        draw.rect(window, (70, 130, 180), quest_achievements_rect)
        btn_text_5 = my_font.render("Достижения", True, (255, 255, 255))
        btn_text_rect_5 = btn_text_5.get_rect(center=quest_achievements_rect.center)
        window.blit(btn_text_5, btn_text_rect_5)
        
        draw.rect(window, (70, 130, 180), quest_btn_rect)
        btn_text_4 = my_font.render("Выйти на рабочий стол", True, (255, 255, 255))
        btn_text_rect_4 = btn_text_4.get_rect(center=quest_btn_rect.center)
        window.blit(btn_text_4, btn_text_rect_4)

    i = 0
    while i < len(notification_texts):
        if new_time - notification_times[i] >= 5:
            notification_texts.pop(i)
            notification_times.pop(i)
        else:
            i += 1

    for i in range(len(notification_texts)):
        y_pos = 60 + i * 55
        draw.rect(window, (40, 80, 40), (316, y_pos, 300, 45))
        draw.rect(window, (255, 215, 0), (316, y_pos, 300, 45), 2)
        window.blit(tr_font.render("Получено: " + notification_texts[i], True, (255, 255, 255)), (325, y_pos + 12))

    display.update()
    clock.tick(FPS)