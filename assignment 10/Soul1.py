import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 250
BOTTOM_MARGIN = 210

class Background(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 700, 550, "window")
        arcade.set_background_color(arcade.color.WHITE)
        
    def on_draw(self):
        arcade.start_render()
        for row in range(10):
            for column in range(10):
                new_col = column * COLUMN_SPACING + LEFT_MARGIN
                new_row = row * ROW_SPACING + BOTTOM_MARGIN
                if (column+row)%2==0:
                    arcade.draw_rectangle_filled(new_col, new_row, 10,10, arcade.color.RED,45)
                else:
                    arcade.draw_rectangle_filled(new_col, new_row, 10,10, arcade.color.BLUE,45)

        arcade.finish_render()
        return super().on_draw()

background=Background()
arcade.run()