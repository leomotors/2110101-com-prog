# pylint: disable=no-member,import-error

import pygame as pg
import random
from os import path
import webbrowser
from PIL import Image
import math

img_dir = path.join('source/img')

# define screen resolution [width 480 , height 600 , FPS 60 ]
width = 480
height = 600
FPS = 60
# define colors
white = (255, 255, 255)
black = (0, 0, 0)

# initialize pg and create window
pg.init()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("シップスペース - ShipSpace")
clock = pg.time.Clock()


# load game graphics
bg = pg.image.load(path.join(img_dir, "space.png")).convert()
bg_rect = bg.get_rect()
ship_img = pg.image.load(path.join(img_dir, "Ship.png")).convert()
meteor_img = pg.image.load(path.join(img_dir, "meteor_med.png")).convert()
bullet_img = pg.image.load(path.join(img_dir, "red_bullet.png")).convert()

thicc_font = pg.font.Font(pg.font.match_font("Comic Sans MS"), 48)
font = pg.font.Font(pg.font.match_font("Comic Sans MS"), 24)

game_over_text = thicc_font.render("Game Over", True, white)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (width // 2, 75)

mutsuki_gif = Image.open("mutsuki_dance.gif")
mutsuki = []
for i in range(mutsuki_gif.n_frames):
    mutsuki_gif.seek(i)
    frame = pg.image.fromstring(
        mutsuki_gif.tobytes(),
        mutsuki_gif.size, mutsuki_gif.mode)
    frame = pg.transform.scale(frame, (300, 300))
    frame_rect = frame.get_rect()
    frame_rect.center = (240, 340)
    mutsuki.append((frame, frame_rect))

mutsuki_frame = 0


def render_game_over():
    global mutsuki_frame

    f = int(mutsuki_frame)

    score_text = font.render(f"Score: {score:.3f}", True, white)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (width // 2, 120)

    screen.blit(score_text, score_text_rect)
    screen.blit(game_over_text, game_over_rect)
    screen.blit(mutsuki[f][0], mutsuki[f][1])

    mutsuki_frame += 0.4
    if mutsuki_frame >= len(mutsuki):
        mutsuki_frame = 0

#################################################################################################
# Class ที่เพิ่มเข้ามาใหม่ -> Ship , Meteor , Bullet ; Function ที่เพิ่มเข้ามาใหม่ -> newmeteor()

# Class ของผู้เล่นภายในมี method __init__ , update , shoot


class Ship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(ship_img, (50, 38))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx -= 8
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx += 8
        if keystate[pg.K_UP] or keystate[pg.K_w]:
            self.speedy -= 8
        if keystate[pg.K_DOWN] or keystate[pg.K_s]:
            self.speedy += 8

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Class ของของหินภายในมี method __init__ , update


meteor_thres = 1.0


class Meteor(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, round(8 * meteor_thres))
        self.speedx = random.randrange(-3, round(3 * meteor_thres))

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Class ของลูกกระสุนภายในมี method __init__ , update


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # ทำลายลูกกระสุนทิ้งถ้าลูกกระสุนออกจากหน้าจอ
        if self.rect.bottom < 0:
            self.kill()

# function ที่สร้างหินขึ้นมา 1 ก้อน


def newmeteor():
    m = Meteor()
    all_sprites.add(m)
    meteors.add(m)
#################################################################################################


new_game = True
game_over = False
score = 0
FULL_AMMO = 8
ammo = 0
ammo_reload = 0
shoot_debounce = False
elapsed = 0

while True:

    # set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม
    clock.tick(FPS)

    if new_game:
        new_game = False
        score = 0
        meteor_thres = 1
        ammo = FULL_AMMO
        elapsed = 0

        #################################################################################################
        # TO DO 1-1 : สรา้ง sprite Group ให้กับ all_sprites, meteors, bullets, ship

        all_sprites = pg.sprite.Group()
        meteors = pg.sprite.Group()
        bullets = pg.sprite.Group()
        ship = pg.sprite.Group()

        # TO DO 1-2 : สร้าง Object ให้กับ ship
        myShip = Ship()

        # TO DO 1-3 : เพิ่ม ship ลงใน all_sprites
        all_sprites.add(myShip)

        #################################################################################################
        # TO DO 2 : สร้าง Object Meteor ขึ้นมา 8 ก้อนโดยผ่านการเรียกใช้ฟังก์ชัน newmeteor()
        for i in range(8):
            newmeteor()

        #################################################################################################

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    #################################################################################################
    # TO DO 3 : ตรวจสอบว่าถ้ามีการกดปุ่ม spacebar (K_SPACE) ให้ ship เรียกฟังก์ชั่นสำหรับการยิงกระสุน
    keystate = pg.key.get_pressed()
    if keystate[pg.K_SPACE]:
        if not shoot_debounce and ammo > 0:
            myShip.shoot()
            ammo -= 1
            shoot_debounce = True
    else:
        shoot_debounce = False

        #################################################################################################

    if game_over:
        render_game_over()

        keystate = pg.key.get_pressed()
        if keystate[pg.K_r]:
            game_over = False
            new_game = True

    else:
        # Update
        all_sprites.update()
        meteor_thres += 0.001
        elapsed += 1
        time_factor = max(1, math.log(elapsed))
        score += 0.001 * time_factor

        #################################################################################################
        # TO DO 5 : ตรวจสอบว่าลูกกระสุนชนหินหรือไม่
        # ถ้าชนให้สร้างหินขึ้นมาใหม่เท่ากับจำนวนที่ถูกชนไป
        hits = pg.sprite.groupcollide(bullets, meteors, True, True)
        for k, vl in hits.items():
            newmeteor()

            for v in vl:
                dist = (myShip.rect.center[0] - v.rect.center[0]) ** 2 + \
                    (myShip.rect.center[1] - v.rect.center[1]) ** 2

                MAX_DIST = 400 * 400 * 1.69

                dist = max(0, (MAX_DIST - min(dist, MAX_DIST)) / MAX_DIST)

                score += (dist + 1) * time_factor

        #################################################################################################
        # TO DO 6 : ตรวจสอบว่าหินชนยานผู้เล่นหรือไม่
        # ถ้าชนให้เริ่มเกมใหม่
        hits = pg.sprite.spritecollide(myShip, meteors, False)
        if hits:
            game_over = True
            webbrowser.open("https://www.brikl.com/jobs")

        #################################################################################################
        # TO DO 4 : clear screen ด้วยสีดำ จากนั้น เอา bg ใส่ใน bg_rect
        screen.fill(black)
        screen.blit(bg, bg_rect)

        #################################################################################################
        # TO DO 7 : วาด element ใน all_sprites ลงใน screen
        for x in all_sprites:
            screen.blit(x.image, x.rect)

        if ammo == 0:
            ammo_reload += 1
            if ammo_reload >= 180:
                ammo_reload = 0
                ammo = FULL_AMMO

        ammo_text = font.render(
            f"Ammo: {ammo}"
            if ammo > 0 else f"Reloading {(3 - ammo_reload / 60):.2f}s",
            True, white)
        ammo_text_rect = ammo_text.get_rect()
        ammo_text_rect.top = 10
        ammo_text_rect.left = 6
        screen.blit(ammo_text, ammo_text_rect)

        mini_score_text = font.render(f"Score: {score:.2f}", True, white)
        mini_score_text_rect = mini_score_text.get_rect()
        mini_score_text_rect.top = 10
        mini_score_text_rect.right = width - 6
        screen.blit(mini_score_text, mini_score_text_rect)

        elapsed_text = font.render(f"Time: {(elapsed / 60):.2f}s", True, white)
        elapsed_text_rect = elapsed_text.get_rect()
        elapsed_text_rect.top = 35
        elapsed_text_rect.right = width - 6
        screen.blit(elapsed_text, elapsed_text_rect)

    #################################################################################################
    # after drawing everything, flip the display

    pg.display.flip()
