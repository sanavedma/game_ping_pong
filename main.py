import arcade
from arcade.examples.dual_stick_shooter import SCREEN_TITLE, SCREEN_HEIGHT, SCREEN_WIDTH
from pyglet import window
background_image = arcade.load_texture("background.gif")

SCREEN_WIDTH = 736
SCREEN_HEIGHT = 437
SCREEN_TITLE = 'Pong Game'

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 1.0)
        self.change_x = 2
        self.change_y = 3

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 1.0)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0 :
            self.left = 0

class Game(arcade.Window):
    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()
        #self.background = arcade.load_texture("background.jpg")

    def setup(self):

        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((142, 169, 151))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta_time: float):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers: int):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
