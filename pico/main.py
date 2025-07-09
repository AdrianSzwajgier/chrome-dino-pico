from machine import Pin
from time import sleep_ms

import config


class Game:
    def mainloop(self):
        pass


def main():
    cooldown = 1 / config.TPS

    while True:
        game = Game()
        game.mainloop()
        while not game.jmp_pin.value():
            sleep_ms(cooldown)


if __name__ == '__main__':
    main()
