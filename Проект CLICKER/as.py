from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load('bg.png'), (700, 500)) 

sprite1 = transform.scale(image.load('player 1.png'), (100, 100))
x1 = 100
y1 = 100

x2 = 300
y2 = 300

# sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))

clock = time.Clock()
FPS = 60

game = True
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    # window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()
    speed = 5

    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed

    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed

    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed

    if keys_pressed[K_d] and x2 < 595:
        x2 += speed

    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed

    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed

    if keys_pressed[K_s] and y2 < 395:
        y2 += speed

    display.update()
    clock.tick(FPS)
#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»