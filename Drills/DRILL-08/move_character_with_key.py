from pico2d import *



def handle_events():
    global running
    global dir
    global dir2
    global way
    global frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                way = 1
                dir += 1
            elif event.key == SDLK_LEFT:
                way = 0
                dir -= 1
            elif event.key == SDLK_UP:
                dir2 += 1
            elif event.key == SDLK_DOWN:
                dir2 -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir2 -= 1
            elif event.key == SDLK_DOWN:
                dir2 += 1


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
dir = 0
dir2 = 0
way = 1
running = True
x = 1280 // 2
y = 1024 // 2
frame = 0

open_canvas(TUK_WIDTH,TUK_HEIGHT)
map = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hide_cursor()

while running:
    clear_canvas()
    map.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * way, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    y += dir2 * 5
    if x >= TUK_WIDTH or x <= 0:
        running = False
    elif y >= TUK_HEIGHT-100 or y <= 150:
        running = False
    delay(0.01)

close_canvas()

