

from pygame import *
from random import randint
from time import time as timer 

win_width = 600
win_height = 500
SCORE = 0 
FPS = 60
BGColor = (200,255,255)
clock = time.Clock()

playerSprite = "racket.png"
ball = "tenis_ball.png"


window = display.set_mode((win_width, win_height))
display.set_caption("ping pong")
window.fill(BGColor)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_w, player_h , player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_w,player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if (keys[K_w]) and (self.rect.y > 5):
            self.rect.y -= self.speed
        if (keys[K_l]) and (self.rect.y < 495):
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if (keys[K_UP]) and (self.rect.y > 5):
            self.rect.y -= self.speed
        if (keys[K_DOWN]) and (self.rect.y < 495):
            self.rect.y += self.speed


window = display.set_mode((win_width, win_height))
display.set_caption("ping pong")
window.fill(BGColor)

player1 = Player(playerSprite, 25, 300, 10, 100, 10)
player2 = Player(playerSprite, 575, 300, 10, 100, 10)





game = True
Finish = False

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False


    if Finish != True:
        window.fill(BGColor)
        player1.update_l()
        player2.update_r()

        player1.reset()
        player2.reset()

display.update()
clock.tick(FPS)
