from pico2d import *

open_canvas()

grass = load_image('grass.png')

character_run = load_image('character_run.png')
character_jump = load_image('character_jump.png')
character_attack = load_image('character_attack.png')
character_walking = load_image('character_walking.png')

def render_all():
        clear_canvas()
        grass.draw(400, 30)


def render_last():
    delay(0.05)
    get_events()

def Run(frame):
    for x in range(0, 800 + 1, 10):
        render_all()
        character_run.clip_draw(frame * 47, 0, 47, 70, x, 80)
        update_canvas()
        frame = (frame + 1) % 8
        render_last()

def jump(frame):
    for x in range(0, 800 + 1, 10):
        render_all()
        character_jump.clip_draw(frame * 39, 0, 36, 90, x, 90)
        update_canvas()
        frame = (frame + 1) % 7
        render_last()

def Weapon_change(frame,jump):
    for x in range(0, 800 + 1, 5):
        clear_canvas()
        grass.draw(400, 30)
        character_attack.clip_draw(frame * 48 + jump, 0, 48 + jump, 65, x, 80)
        update_canvas()
        frame = (frame + 1) % 12

        if jump >= 48:
            jump = 0

        if frame == 11:
            jump = 48

        delay(0.07)
        get_events()


def Waking(frame):
    for x in range(0, 800 + 1, 5):
        render_all()
        character_walking.clip_draw(frame * 43, 0, 43, 75, x, 70)
        update_canvas()
        frame = (frame + 1) % 12
        delay(0.09)
        get_events()




while True:
    Run(0)
    jump(0)
    Weapon_change(0,0)
    Waking(0)
    break

close_canvas()