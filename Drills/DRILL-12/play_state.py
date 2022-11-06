from pico2d import *
import game_framework
import game_world

from grass import Grass
from grass import Grass
from boy import Boy


boy = None
grass = None
grass2 = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass, grass2
    grass = Grass()
    boy = Boy()
    grass2 = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)

# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def pause():
    pass

def resume():
    pass


