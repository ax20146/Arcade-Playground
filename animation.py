# /animation.py

from typing import Literal

import arcade as ac

State = Literal["Idle", "Walk"]
Direction = Literal[0, 1]


class Player(ac.Sprite):
    PATH = ":resources:images/animated_characters/robot/robot_"
    DIRECTION_LEFT = 1
    DIRECTION_RIGHT = 0

    def __init__(self) -> None:
        super().__init__()

        self.idx: float = 0
        self.state: State = "Idle"
        self.direction: Direction = self.DIRECTION_RIGHT
        self.frames: dict[State, list[list[ac.Texture]]] = {
            "Idle": [ac.load_texture_pair(f"{self.PATH}idle.png")],  # type: ignore
            "Walk": [
                ac.load_texture_pair(f"{self.PATH}walk{i}.png") for i in range(8)  # type: ignore
            ],
        }

        self.texture = self.frames["Idle"][self.idx][self.DIRECTION_RIGHT]

    def update_animation(self, delta_time: float = 1 / 60) -> None:
        self.idx += 30 * delta_time

        if self.idx >= len(self.frames[self.state]):
            self.idx = 0

        self.texture = self.frames[self.state][int(self.idx)][self.direction]


class Game(ac.View):
    def __init__(self) -> None:
        super().__init__()

        ac.set_background_color((150, 150, 240))

        self.engin: ac.PhysicsEngineSimple

    def setup(self) -> None:
        self.player = Player()
        self.player.position = (1280 // 2, 720 // 2)

        self.engin = ac.PhysicsEngineSimple(self.player, ac.SpriteList())

    def on_show_view(self) -> None:
        self.setup()

    def on_draw(self) -> None:
        self.clear()

        self.player.draw()  # type: ignore

    def on_update(self, delta_time: float):
        self.engin.update()

        self.player.update_animation(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == ac.key.LEFT and symbol != ac.key.RIGHT:
            self.player.direction = self.player.DIRECTION_LEFT
            self.player.state = "Walk"
            self.player.change_x = -10

        if symbol == ac.key.RIGHT and symbol != ac.key.LEFT:
            self.player.direction = self.player.DIRECTION_RIGHT
            self.player.state = "Walk"
            self.player.change_x = 10

    def on_key_release(self, symbol: int, _modifiers: int):
        if symbol == ac.key.LEFT and symbol != ac.key.RIGHT:
            self.player.direction = self.player.DIRECTION_LEFT
            self.player.state = "Idle"
            self.player.change_x = 0

        if symbol == ac.key.RIGHT and symbol != ac.key.LEFT:
            self.player.direction = self.player.DIRECTION_RIGHT
            self.player.state = "Idle"
            self.player.change_x = 0


def main():
    window = ac.Window(1280, 720, "Isometric")  # type: ignore
    window.show_view(Game())
    window.run()


if __name__ == "__main__":
    main()
