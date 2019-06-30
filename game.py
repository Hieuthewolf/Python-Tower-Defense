import pygame
import os
import time
import random

#Importing enemies
from enemies.monster import Monster_1, Monster_2, Monster_3, Monster_4
from enemies.boss import Balrog, KingSlime, Mano, Pianus, PinkBean

#Importing constants
from constants import Constants

# #Importing useful functions
# from usefulFunctions import createPathLayout

#Importing Towers
from towers.archerTower import ArcherTowerFar, ArcherTowerShort
from towers.supportTower import DamageTower, RangeTower

#Importing main menu
from menu.menu import ShopMenu

#Game lives and money assets
life_image = pygame.image.load(os.path.join("images/lives", "heart.png"))
crystal_image = pygame.image.load(os.path.join("images/upgrade", "crystal_3.png"))
pygame.init()
game_font = pygame.font.SysFont('comicsans', 60)

#Side-bar shop menu assets
side_bar_img = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "side_bar_img.png")), (150, 325))
buy_archer = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "bow.png")), (60, 60))
buy_crossbowman = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "crossbow.png")), (60, 60))
buy_support_dmg = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "damage_tower.png")), (60, 60))
buy_support_range = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "range_tower.png")), (60, 60))

#Adding music
pygame.mixer.pre_init(44100, 16, 2, 4096)

clock = pygame.time.Clock()
    
class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((Constants.DIMENSIONS['game'][0], Constants.DIMENSIONS['game'][1]))
        self.enemies = [Pianus('pianus')]
        self.attack_towers = []
        # self.support_towers = [DamageTower('support_tower_damage', (436, 527)), RangeTower('support_tower_range', (600, 600))]
        self.support_towers = []
        self.dead_enemies = set()

        # Attack tower names and support tower names
        self.att_tower_names = ["bowman", "crossbowman"]
        self.sup_tower_names = ["support_damage", "support_range"]

        self.money = 1000
        self.background_img = pygame.image.load(os.path.join("images", "bg.png"))
        self.background_img = pygame.transform.scale(self.background_img, (Constants.DIMENSIONS['game'][0], Constants.DIMENSIONS['game'][1]))

        # self.path = createPathLayout(Constants.PATH_CORNERS)

        self.width = Constants.DIMENSIONS['game'][0]
        self.height = Constants.DIMENSIONS['game'][1]

        # Testing purposes
        self.clicks = []

        # Spawning enemies
        self.timer = time.time()
        
        # Lives and life font
        self.lives_font = game_font
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

        # For animating the death of a boss
        self.boss_dies = None

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

        while ongoing:
            clock.tick(80)

            # Monster waves
            if time.time() - self.timer >= 1:
                self.timer = time.time()
                self.enemies.append(random.choice([Monster_2('monster_2'), Monster_3('monster_3'), Monster_4('monster_4')]))
            
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
                self.money += t.attack(self.enemies, self.dead_enemies, self.boss_dies)

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
        for dead_e in self.dead_enemies:
            dead_e.die(self.window)

        # Drawing animation of dead boss if defeated
        if self.boss_dies:
            self.boss_dies.die(self.window)

        # Draw the tower being dragged
        if self.drag_object:
            self.drag_object.draw(self.window)

        #Drawing lives
        life_txt = self.lives_font.render(str(self.lives), 1, (255, 255, 255))
        life_img = pygame.transform.scale(life_image, (40, 40))
        life_start_pos = life_img.get_width()

        self.window.blit(life_txt, (life_start_pos + 25, 8))
        self.window.blit(life_img, (life_start_pos - 25, 8))

        #Drawing crystal currency
        crystal_txt = self.lives_font.render(str(self.money), 1, (255, 255, 255))
        crystal_img = pygame.transform.scale(crystal_image, (40, 40))
        crystal_start_pos = crystal_img.get_width() 

        self.window.blit(crystal_txt, (crystal_start_pos + 25, 60))
        self.window.blit(crystal_img, (crystal_start_pos - 25, 60))

        #Draw menu
        self.shop_menu.draw(self.window)

        pygame.display.update()

    

g = Game()
g.run()