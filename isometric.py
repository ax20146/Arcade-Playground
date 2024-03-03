# /isometric.py

import arcade as ac


class Game(ac.View):
    def __init__(self) -> None:
        super().__init__()

        ac.set_background_color((150, 150, 240))

        self.scene: ac.Scene

    def setup(self) -> None:
        self.scene = ac.Scene()

        for i in range(2):
            wall = ac.Sprite(
                ":resources:images/isometric_dungeon/stoneTile_W.png"
            )
            wall.position = (-i * 256 // 2 + 300, -i * 512 // 3.48 // 2 + 500)
            self.scene.add_sprite("Wall", wall)

    def on_show_view(self) -> None:
        self.setup()

    def on_draw(self) -> None:
        self.clear()

        self.scene.draw()  # type: ignore


def main():
    window = ac.Window(1280, 720, "Isometric")  # type: ignore
    window.show_view(Game())
    window.run()


if __name__ == "__main__":
    main()
