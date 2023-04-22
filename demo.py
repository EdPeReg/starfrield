import arcade

WIDTH = 800
HEIGHT = 600

class Demo(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        # Calling the parent class constructor
        super().__init__(width, height, title)

        arcade.set_background_color(color=arcade.color.ARMY_GREEN)
    def on_draw(self):
        """Called once per friend to render everything in the screen"""

        arcade.start_render()
        arcade.draw_circle_filled(WIDTH // 2, HEIGHT // 2, 50, arcade.color.AFRICAN_VIOLET)

if __name__ == '__main__':
    demo = Demo(WIDTH, HEIGHT, "This is a demo")
    demo.run()
