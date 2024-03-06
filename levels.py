# /levels.py

import arcade as ac


class Game(ac.View):
    def __init__(self) -> None:
        super().__init__()

        ac.set_background_color((150, 150, 240))

        self.scene: ac.Scene

    def setup(self) -> None:
        self.scene = ac.Scene()

        self.map = ac.load_tilemap("assets/Plains.tmx")

        self.scene = ac.Scene.from_tilemap(self.map)

        print(self.map.sprite_lists)

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
