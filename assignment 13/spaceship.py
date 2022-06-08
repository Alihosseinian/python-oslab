import time
import arcade
import math
import random
import threading
#################################################################################################################
SPRITE_SCALING_PLAYER = 0.5
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "SpaceCraft"
#################################################################################################################
class Spaceship(arcade.Sprite):
    def __init__(self):
    
        super().__init__(':resources:images/space_shooter/playerShip3_orange.png',SPRITE_SCALING_PLAYER)
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.width = 48
        self.height = 48
        self.center_x = SCREEN_WIDTH//2
        self.center_y = 50
        self.change_x = 0
        self.change_y = 0
        self.angle = 0
        self.change_angle = 0
        self.bullet_list =arcade.SpriteList()
        self.speed = 2.5
    
    def rotate(self):
        self.angle += self.change_angle * self.speed

    def fire(self):
        self.bullet_list.append(Bullet(self))  

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        return super().draw(filter=filter, pixelated=pixelated, blend_function=blend_function)
#################################################################################################################
class Bullet(arcade.Sprite):
    
    def __init__(self, trigger): 
        super().__init__(':resources:images/space_shooter/laserRed01.png',0.8)
        
        arcade.sound.play_sound(trigger.gun_sound)
        self.speed = 10
        self.angle = trigger.angle
        self.center_x = trigger.center_x
        self.center_y = trigger.center_y

    def update(self):
        angle_radious = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_radious)
        self.center_y += self.speed * math.cos(angle_radious)
#################################################################################################################
class Enemy(arcade.Sprite):
    
    def __init__(self):
        super().__init__(':resources:images/space_shooter/playerShip1_green.png',0.3)
        self.speed = 2.5
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = SCREEN_HEIGHT+10  
        self.angle = 180
        self.width = 50
        self.height = 50

    def hit(self):
        arcade.play_sound(arcade.sound.Sound('akh.wav'), 1.0, 0.0,False)

    def update(self):
        self.center_y -= self.speed  
#################################################################################################################
class SpaceCraft(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.ship=Spaceship()
        self.score=0
        self.heartimg = "heart.png"
        self.heal_list = arcade.SpriteList() 
        self.heal_list.append(arcade.Sprite(self.heartimg, 0.03 , center_x=30 , center_y=50))
        self.heal_list.append(arcade.Sprite(self.heartimg, 0.03 , center_x=80 , center_y=50))
        self.heal_list.append(arcade.Sprite(self.heartimg, 0.03 , center_x=130 , center_y=50))
        self.enemy_list=[]
        self.set_mouse_visible(False)
        self.end_thread=False
        self.my_thread=threading.Thread(target=self.add_enemy)
        self.my_thread.start()  
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture("background.png")

    def add_enemy(self):
        while True:
            time.sleep(random.randint(3,6))
            self.enemy_list.append(Enemy())
            if self.end_thread:
                break

    def on_draw(self):
        arcade.start_render()
        if(not(len(self.heal_list))):
            arcade.draw_text('Game Over',SCREEN_WIDTH//2-90,SCREEN_HEIGHT//2,arcade.color.WHITE,width=20,font_size=25)
            self.end_thread=True
            self.close()
        else:
            arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background_image)
            arcade.draw_text(f"Score: {self.score}",SCREEN_WIDTH-80 , 30, arcade.color.RED,bold=True)

            self.heal_list.draw()
            self.ship.draw()
            self.ship.bullet_list.draw()
            for i in range(len(self.enemy_list)):
                self.enemy_list[i].draw()
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.ship.fire() 

        elif symbol == arcade.key.LEFT:
            self.ship.change_angle = 5
            self.ship.rotate()  

        elif symbol == arcade.key.RIGHT:
            self.ship.change_angle = -5    
            self.ship.rotate()

    def on_update(self, delta_time):
        self.ship.bullet_list.update()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].update()
        for bullet in self.ship.bullet_list:
            for enemy in self.enemy_list:
                if(arcade.check_for_collision(bullet,enemy)):
                    self.score += 1
                    enemy.hit()
                    self.enemy_list.remove(enemy)
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
        for enemy in self.enemy_list:
            if(arcade.check_for_collision(self.ship,enemy)):
                enemy.hit()
                self.enemy_list.remove(enemy)
                hp=self.heal_list.pop()
                hp.remove_from_sprite_lists()
            elif enemy.top < 0:
                self.enemy_list.remove(enemy)
                hp=self.heal_list.pop()
                hp.remove_from_sprite_lists()
#################################################################################################################
window = SpaceCraft()
window.center_window()
arcade.run()