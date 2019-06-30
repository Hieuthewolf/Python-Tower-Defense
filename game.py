import pygame
import os
import time
import random

#Importing enemies
from enemies.monster import *
from enemies.boss import Balrog, KingSlime, Mano, Pianus, PinkBean

#Importing constants
from constants import WaveConstants, GameConstants

# #Importing useful functions
# from usefulFunctions import createPathLayout

#Importing Towers
from towers.archerTower import ArcherTowerFar, ArcherTowerShort
from towers.supportTower import DamageTower, RangeTower

#Importing main menu
from menu.menu import ShopMenu, GameStateButton

#Game lives and money assets
life_image = pygame.image.load(os.path.join("images/lives", "heart.png"))
crystal_image = pygame.image.load(os.path.join("images/upgrade", "crystal_3.png"))
pygame.init()
game_font = pygame.font.SysFont('comicsans', 52)

# Pause/Play buttons
play = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "button_start.png")), (60, 60))
pause = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "button_pause.png")), (60, 60))

# Wave indicator
wave =  pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "wave.png")), (200, 50))

# Side-bar shop menu assets
side_bar_img = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "side_bar_img.png")), (150, 325))
buy_archer = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "bow.png")), (60, 60))
buy_crossbowman = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "crossbow.png")), (60, 60))
buy_support_dmg = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "damage_tower.png")), (60, 60))
buy_support_range = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "range_tower.png")), (60, 60))

#Adding music
pygame.mixer.pre_init(44100, 16, 2, 4096)

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((GameConstants.DIMENSIONS['game'][0], GameConstants.DIMENSIONS['game'][1]))
        self.enemies = [PinkBean('pink_bean')]
        self.attack_towers = []
        # self.support_towers = [DamageTower('support_tower_damage', (436, 527)), RangeTower('support_tower_range', (600, 600))]
        self.support_towers = []
        self.dead_enemies = set()

        # Attack tower names and support tower names
        self.att_tower_names = ["bowman", "crossbowman"]
        self.sup_tower_names = ["support_damage", "support_range"]

        self.money = 1000
        self.background_img = pygame.image.load(os.path.join("images", "bg.png"))
        self.background_img = pygame.transform.scale(self.background_img, (GameConstants.DIMENSIONS['game'][0], GameConstants.DIMENSIONS['game'][1]))

        # self.path = createPathLayout(Constants.PATH_CORNERS)

        self.width = GameConstants.DIMENSIONS['game'][0]
        self.height = GameConstants.DIMENSIONS['game'][1]

        # Testing purposes
        self.clicks = []

        # Spawning enemies
        self.timer = time.time()
        
        # Lives and life font
        self.font = game_font
        self.lives = 10

        # Music
        self.music = pygame.mixer.music
        self.music.load("maple.mp3")
        self.music.set_volume(0.7)
        self.music.play(-1)

        # Selecting tower logistics
        self.select_tower = None

        # Adding items to the shop
        self.shop_menu = ShopMenu(side_bar_img.get_width() // 2 - 10, 115, side_bar_img)
        self.shop_menu.add_button("bowman", buy_archer, 400)
        self.shop_menu.add_button("crossbowman", buy_crossbowman, 600)
        self.shop_menu.add_button("support_damage", buy_support_dmg, 800)
        self.shop_menu.add_button("support_range", buy_support_range, 1250)

        # Dragging towers around
        self.drag_object = None

        # Logistics involving generating monster waves
        self.current_wave = 0
        self.cur_wave_amounts = WaveConstants.ENEMY_WAVES_AMOUNT[self.current_wave]

        # Pausing the game
        self.pause_game = True
        self.game_state_button = GameStateButton(play, pause, 10, self.height - 70)

    def spawn_enemies(self):
        """
        Spawns enemies based on the current wave
        """
        if sum(self.cur_wave_amounts):
            ENEMY_WAVES_MONSTER_NAMES = {
                0: [Monster_1('monster_1'), Monster_2('monster_2'), Monster_3('monster_3'), Monster_4('monster_4')],
                1: [Monster_1('monster_1'), Monster_2('monster_2'), Monster_3('monster_3'), Monster_4('monster_4')],
                2: [Monster_1('monster_1'), Monster_2('monster_2'), Monster_3('monster_3'), Monster_4('monster_4')],
                3: [Monster_1('monster_1'), Monster_2('monster_2'), Monster_3('monster_3'), Monster_4('monster_4')],
                4: [Monster_5('monster_5'), Monster_6('monster_6'), Monster_7('monster_7'), Monster_8('monster_8')],
                5: [Monster_5('monster_5'), Monster_6('monster_6'), Monster_7('monster_7'), Monster_8('monster_8')],
                6: [Monster_5('monster_5'), Monster_6('monster_6'), Monster_7('monster_7'), Monster_8('monster_8')],
                7: [Monster_5('monster_5'), Monster_6('monster_6'), Monster_7('monster_7'), Monster_8('monster_8')],
                8: [Monster_1('monster_1'), Monster_2('monster_2'), Monster_3('monster_3'), Monster_4('monster_4'), Monster_5('monster_5'), Monster_6('monster_6'), Monster_7('monster_7'), Monster_8('monster_8'), Monster_9('monster_9'), Monster_10('monster_10')],
                9: [Monster_1('monster_1'), Monster_2('monster_2'), Monster_3('monster_3'), Monster_4('monster_4'), Monster_5('monster_5'), Monster_6('monster_6'), Monster_7('monster_7'), Monster_8('monster_8'), Monster_9('monster_9'), Monster_10('monster_10')]
            }
            for i, amount in enumerate(self.cur_wave_amounts):
                if amount:
                    self.enemies.append(ENEMY_WAVES_MONSTER_NAMES[self.current_wave][i])
                    self.cur_wave_amounts[i] -= 1
                    break
        else:
            if not self.enemies:
                self.current_wave += 1
                self.cur_wave_amounts = WaveConstants.ENEMY_WAVES_AMOUNT[self.current_wave]
                self.pause_game = True
                self.game_state_button.image = self.game_state_button.images[0]
            

    def buy_tower(self, name):
        x, y = pygame.mouse.get_pos()
        tower_obj_pair = {"bowman": ArcherTowerFar("bowman", (x, y)), "crossbowman": ArcherTowerShort("crossbowman", (x, y)), "support_damage": DamageTower("support_damage", (x, y)), "support_range": RangeTower("support_range", (x, y))}
        try:
            tower_obj = tower_obj_pair[name]
            self.drag_object = tower_obj
            tower_obj.being_dragged = True
        except Exception as error:  
            print(str(error) + "Invalid Name")

    def run(self):
        ongoing = True
        clock = pygame.time.Clock()

        while ongoing:
            clock.tick(200)

            if not self.pause_game:
                # Monster waves
                if time.time() - self.timer >= random.randint(1, 6) / 3:
                    self.timer = time.time()
                    self.spawn_enemies()

            # Check for objects being dragged
            pos = pygame.mouse.get_pos()    
            if self.drag_object:
                self.drag_object.move(pos[0], pos[1])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ongoing = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If dragging an item and then clicking on a spot
                    if self.drag_object:
                        if self.drag_object.name in self.att_tower_names:
                            self.attack_towers.append(self.drag_object)
                        else:
                            self.support_towers.append(self.drag_object)

                        self.drag_object.being_dragged = False
                        self.drag_object = None
                    else:
                        # Checking for the current state of the game (Paused or play)
                        if self.game_state_button.click(pos[0], pos[1]):
                            self.pause_game = not self.pause_game
                            self.game_state_button.switch_img()

                        #Clicking on main menu
                        main_menu_item_name = self.shop_menu.get_clicked_item(pos[0], pos[1])
                        if main_menu_item_name: 
                            if self.money >= self.shop_menu.get_it_cost(main_menu_item_name):
                                self.money -= self.shop_menu.get_it_cost(main_menu_item_name)
                                self.buy_tower(main_menu_item_name)

                        # self.clicks.append(pos)
                        # print(self.clicks)

                        button_clicked = False
                        
                        #Currently pressing on an item on the menu
                        if self.select_tower:       
                            button_clicked = self.select_tower.menu.get_clicked_item(pos[0], pos[1])
                            if button_clicked:
                                if button_clicked == "upgrade":
                                    if self.select_tower.get_upgrade_cost() != "MAX":
                                        if self.money >= self.select_tower.get_upgrade_cost():
                                            self.money -= self.select_tower.get_upgrade_cost()
                                            self.select_tower.upgrade()

                        # If we're not on the menu of an item
                        if not button_clicked:
                            for t in self.attack_towers:
                                if t.click(pos[0], pos[1]):
                                    t.selected = True
                                    self.select_tower = t
                                else:
                                    t.selected = False

                            for t in self.support_towers:
                                if t.click(pos[0], pos[1]):
                                    t.selected = True
                                    self.select_tower = t
                                else:
                                    t.selected = False

            if not self.pause_game:
                # Appending to a new list enemeies that are off the screen as indicated by the e.move() return value
                delete_enemies = []
                for e in self.enemies:
                    if not e.move():
                        delete_enemies.append(e)

                # Deleting enemies off the screen
                for e in delete_enemies:
                    self.lives -= 1
                    self.enemies.remove(e)

                # Looping through the towers and attack enemies if any are in range
                for t in self.attack_towers:
                    self.money += t.attack(self.enemies, self.dead_enemies)

                for t in self.support_towers:
                    t.support(self.attack_towers)

                # Terminating Game Over condition
                if self.lives <= 0:
                    print("Game Over")
                    ongoing = False

            self.draw()

        pygame.quit()

    def draw(self):
        self.window.blit(self.background_img, (0, 0))

        # Testing purposes of mouse movement
        # for p in self.clicks:
        #     pygame.draw.circle(self.window, (255, 0, 0), (p[0], p[1]), 10, 0)   

        # Drawing towers
        for a in self.attack_towers:
            a.draw(self.window)
        for s in self.support_towers:
            s.draw(self.window)

        # Drawing enemies
        for e in self.enemies:
            e.draw(self.window)
        
        # Drawing animation of dead enemies
        for dead_enemy in self.dead_enemies:
            dead_enemy.die(self.window)

        # Draw the tower being dragged
        if self.drag_object:
            self.drag_object.draw(self.window)

        #Drawing lives
        life_txt = self.font.render(str(self.lives), 1, (255, 255, 255))
        life_img = pygame.transform.scale(life_image, (40, 40))
        life_start_pos = life_img.get_width()

        self.window.blit(life_txt, (life_start_pos + 25, 11))
        self.window.blit(life_img, (life_start_pos - 25, 8))

        #Drawing crystal currency
        crystal_txt = self.font.render(str(self.money), 1, (255, 255, 255))
        crystal_img = pygame.transform.scale(crystal_image, (40, 40))
        crystal_start_pos = crystal_img.get_width() 

        self.window.blit(crystal_txt, (crystal_start_pos + 25, 63))
        self.window.blit(crystal_img, (crystal_start_pos - 25, 60))

        #Draw menu
        self.shop_menu.draw(self.window)

        #Drawing game state button
        self.game_state_button.draw(self.window)

        #Drawing the wave indicator
        self.window.blit(wave, (self.width - wave.get_width() + 30, -10)) #Wave BG
        wave_txt = self.font.render("Wave: " + str(self.current_wave + 1), 1, (255, 255, 255))
        self.window.blit(wave_txt, (self.width - wave_txt.get_width() // 2 - wave.get_width() // 2 + 15, 5))

        pygame.display.update()

    

g = Game()
g.run()