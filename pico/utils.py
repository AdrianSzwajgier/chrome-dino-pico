from display_driver import TFT


def draw(x, y, sprite, display):
    for start_x, column in enumerate(sprite):
        for start_y, length in column:
            display.hline((start_x + x, start_y + y), length, TFT.BLACK)
