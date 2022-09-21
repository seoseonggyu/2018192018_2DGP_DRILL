from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')



r = 0
u = 0
l = 0
d = 0
r2 = 0
while(True):

    
    if r < 390:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+r,90)
        r = r + 2
        delay(0.01)

    
    elif u < 490:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(790,90+u)
        u= u + 2
        delay(0.01)

    elif l < 790:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(790-l,580)
        l = l + 2
        delay(0.01)


    elif d < 490:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,580-d)
        d= d + 2
        delay(0.01)


    
    elif r2 < 400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0+r2,90)
        r2 = r2 + 2
        delay(0.01)
        
    else:
        r = 0
        u = 0
        l = 0
        d = 0
        r2 = 0
        
    
close_canvas()
