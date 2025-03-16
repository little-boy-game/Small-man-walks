import pgzrun
import random
WIDTH = 600
HEIGHT = 760

#开始调试
dix =  {370:6,430:6,490:8}#,550:9,310:5,250:4}
cao = []
b = 15


'''
print('按回车开始游戏')
a = input()
if a == 'kfl':
    b = int(input('开发者模式已开启\n输入跳跃高度（默认15）：'))
'''



sx = -30
for j in range(10):
    sx += 60
    sy = random.choice(list(dix.keys()))
    for i in range(dix[sy]):
        sy += 60
        cao.append(Actor('cao',center = (sx,sy)))
#cao = Actor('cao',center = (400,430))
ren = Actor('ren',center = (400,250))
is_jumping = False
jump_speed = b
gravity = 1

def draw() :
    screen.blit('blue',(0,0))
    for i in cao:
        i.draw()
    ren.draw()

def update():
    global is_jumping, jump_speed
    if keyboard.A and not keyboard.LSHIFT:
        ren.x -= 5
    if keyboard.D and not keyboard.LSHIFT:
        ren.x += 5
    if keyboard.SPACE and not is_jumping:
        is_jumping = True
        jump_speed = b

    if is_jumping:
        ren.image = 'ren_dun'
        ren.y -= jump_speed
        jump_speed -= gravity
        if ren.y >= 250:
            ren.y = 250
            is_jumping = False
            ren.image = 'ren'

def on_key_down(key):
    if key == keys.LSHIFT:
        ren.image = 'ren_dun'
    elif key == keys.ESCAPE:
        exit()

def on_key_up(key):
    if key == keys.LSHIFT:
        ren.image = 'ren'

pgzrun.go()