from settings import Settings


class Cursor:
    RIGHT = 1
    LEFT = 2
    DOWN = 3
    UP = 4

    def __init__(self):
        self.x = 1
        self.y = 0

    def move(self, direction):
        if direction == Cursor.RIGHT:
            if self.x < Settings.getWidth() - 2:
                self.x += 2

        if direction == Cursor.LEFT:
            if self.x > 1:
                self.x -= 2

        if direction == Cursor.DOWN:
            if self.y < Settings.getHeight() - 1:
                self.y += 1

        if direction == Cursor.UP:
            if self.y > 0:
                self.y -= 1
