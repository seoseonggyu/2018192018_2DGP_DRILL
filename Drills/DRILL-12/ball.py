from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x, y , face, velocity = 2):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.face = face

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.face == 1:
            self.x += self.velocity
        elif self.face == -1:
            self.x -= self.velocity

        # if self.x < 25 or self.x > 800 - 25:
        #         game_world.remove_object(self)
