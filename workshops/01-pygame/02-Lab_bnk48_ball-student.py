# pylint: disable=E,W

# Lab_BNK48
import math
from random import randint
import pygame as pg

# TODO 1 : กำหนด width : 1000 , height : 600 และ FPS : 60
width = 1000
height = 600
FPS = 60

# TODO 2 : กำหนดค่าสีดังนี้ pink : (197,142,195) , white : (255,255,255)
pink = (197, 142, 195)
white = (255, 255, 255)

# TODO 3 : กำหนดความเร็วให้กับ member แต่ละคน [ 3 member ]
ball1_speed = [2.0, 2.0]
ball2_speed = [-3.0, 4.0]
ball3_speed = [3.0, -2.0]

# TODO 4 : initialize pygame variable and create clock
pg.init()
clock = pg.time.Clock()
running = True

# TODO 5 : create screen [pygame.display.set_mode]
# and set caption [pygame.display.set_caption] => "BNK_BALL (Heavy Collision)"
screen = pg.display.set_mode((width, height))
pg.display.set_caption("BNK48 ボール ヘビーコリジョン")

# TODO 6
# Load sound [change your sound filepath according to your computer]
pg.mixer.init()
pg.mixer.music.load("workshops/01-pygame/assets/sound.mp3")
pg.mixer.music.play(-1, 0)

# ใช้คำสั่ง soundeffect.play() เพื่อเล่นเสียง effect ตอนลูกบอลชนกัน
soundeffect = pg.mixer.Sound("workshops/01-pygame/assets/effect.wav")
ඞ = pg.mixer.Sound("workshops/01-pygame/assets/AMOGUS.mp3")
pg.mixer.Sound.play(ඞ)


def play_sound():
    pg.mixer.Sound.play(ඞ if randint(0, 1000) < 25 else soundeffect)

# Choose 3 members from BNK48 and create pygame object from  get_rect
# [ load , resize , get_rect ]


class Member:
    def __init__(self, name: str, speed: list[float], size=(100, 100)):
        img = pg.image.load(f"workshops/01-pygame/assets/BNK48/{name}_cc.png")
        self.size = size[0]
        self.surface = pg.transform.scale(img, size)
        self.rect = self.surface.get_rect()
        self.rect.center = (randint(75, width - 75), randint(75, height - 75))
        self.speed = speed
        self.max_speed = [6.9, 6.9]
        self.increase_speed_counter = 0
        self.collision_cooldown = 0

    def rectify_speed(self, x: float) -> float:
        if x > 0:
            return min(x, self.max_speed[0])
        else:
            return max(x, -self.max_speed[0])

    def move(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])
        # self.increase_speed_counter += 1
        self.collision_cooldown -= 1

        # if self.increase_speed_counter % 180 == 0:
        #     self.increase_speed()

        x, y = self.rect.center

        lt = self.size // 2 - 5

        if x < lt:
            x = 95
        if x > width - lt:
            x = width - 95

        if y < lt:
            y = 95
        if y > height - lt:
            y = height - 95

        self.rect.center = (x, y)

        self.speed = [
            self.rectify_speed(self.speed[0]),
            self.rectify_speed(self.speed[1])]

    def increase_speed(self):
        self.speed[0] *= 1.2
        self.speed[1] *= 1.2

    def check_frame_collision(self):
        collided = False

        if self.rect.left < 0 or self.rect.right > width:
            collided = True
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            collided = True
            self.speed[1] = -self.speed[1]

        if collided:
            play_sound()

    def draw_self(self):
        screen.blit(self.surface, self.rect)


def is_collide(x1, y1, x2, y2, threshold=100):
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist if dist <= threshold else False


def safe_atan(y, x):
    if x == 0:
        return math.pi / 2 if y > 0 else -math.pi / 2

    return math.atan(y / x)


def elastic_collision(ux1, uy1, ux2, uy2, x1, y1, x2, y2):
    # give up mode T_T
    # return (-ux1, -uy1, -ux2, -uy2)

    u1 = math.sqrt(ux1 ** 2 + uy1 ** 2)
    u2 = math.sqrt(ux2 ** 2 + uy2 ** 2)
    theta1 = safe_atan(uy1, ux1)
    theta2 = safe_atan(uy2, ux2)

    dx = x2 - x1
    dy = y2 - y1

    phi = -safe_atan(dy, dx)

    v1x = u2 * math.cos(theta2 - phi) + u1 * math.sin(
        theta1 - phi) * math.cos(phi + math.pi / 2)
    v1y = u2 * math.sin(theta2 - phi) + u1 * math.sin(
        theta1 - phi) * math.sin(phi + math.pi / 2)
    v2x = u1 * math.cos(theta1 - phi) + u2 * math.sin(
        theta2 - phi) * math.cos(phi + math.pi / 2)
    v2y = u1 * math.sin(theta1 - phi) + u2 * math.sin(
        theta2 - phi) * math.sin(phi + math.pi / 2)
    return (v1x, v1y, v2x, v2y)


members = [
    Member("Cherprang", ball1_speed),
    Member("Music", ball2_speed, (150, 150)),
    Member("Mobile", ball3_speed)]


# TODO 7 : create object with attribute in each comment
# list of members more pog

while running:
    # TODO 8 : set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม [clock.tick(...)]
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

    if running:
        # TODO 9 :ใส่สี background สีชมพู (screen.fill(...))
        screen.fill(pink)

        # TODO 10 : ให้ member ทั้ง 3 คนเคลื่อนที่ตามทิศทางและความเร็วเป็นไปตาม speed ของแต่ละคน
        for member in members:
            member.move()

        # TODO 11 : วาด text คำว่า "Heavy Collision" [size : 150 , center :(width/2 , height/3), สีขาว]
        jp_font_name = pg.font.match_font('Yu Mincho')  # กำหนดชื่อ Font
        font = pg.font.Font(jp_font_name, 100)  # กำหนดขนาด font
        heavy_rotation_surface = font.render("ヘビーコリジョン", True, white)
        heavy_rotation_rect = heavy_rotation_surface.get_rect()
        heavy_rotation_rect.center = (width // 2, height // 3)

        # TODO 12 : วาด text รหัสนิสิต ลงไป ข้างใต้คำว่า "Heavy Collision" [size : 100 ,center :(width/2 , height/1.5), สีขาว]
        # [ขนาดและตำแหน่งสามารถปรับได้ตามความเหมาะสม]
        en_font_name = pg.font.match_font('Sarabun')
        font = pg.font.Font(en_font_name, 100)
        my_id_surface = font.render("6532068721", True, white)
        my_id_rect = my_id_surface.get_rect()
        my_id_rect.center = (width // 2, (height * 2) // 3)

        screen.blit(heavy_rotation_surface, heavy_rotation_rect)
        screen.blit(my_id_surface, my_id_rect)

        # TODO 13 : เขียนเงื่อนไขไม่ให้ตกกรอบทุกด้านให้กับ member ทั้ง 3 คน
        for member in members:
            member.check_frame_collision()

            # Special point ทำให้ลูกบอลชนกันแล้วเด้งในทิศตรงกันข้าม
            for i in range(len(members)):
                for j in range(i + 1, len(members)):
                    x1, y1 = members[i].rect.center
                    ux1, uy1 = members[i].speed
                    x2, y2 = members[j].rect.center
                    ux2, uy2 = members[j].speed
                    if (d := is_collide(x1, y1, x2, y2, round(members[i].size / 2 + members[j].size / 2))) and members[i].collision_cooldown < 0 and members[j].collision_cooldown < 0:
                        play_sound()
                        v1x, v1y, v2x, v2y = elastic_collision(
                            ux1, uy1, ux2, uy2, x1, y1, x2, y2)
                        members[i].speed = [v1x, v1y]
                        members[j].speed = [v2x, v2y]
                        members[i].collision_cooldown = (150 - round(d)) // 3
                        members[j].collision_cooldown = (150 - round(d)) // 3
            ################################################

            # TODO 14 : เอาภาพของ member แต่ละคนใส่ลงใน object ของตนเอง
            member.draw_self()

        pg.display.flip()
