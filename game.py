import pygame
import os
import time
import random

# For leaderboard stuff
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://hieuthewolf:hieutrung123@cluster0-qcx63.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["Python_Tower_Defense"]
collection = db["high_scores"]

#Initializing pygame
pygame.init()

#Importing enemies
from enemies.monster import *
from enemies.boss import Balrog, KingSlime, Mano, Pianus, PinkBean

#Importing constants
from constants import EnemyConstants, GameConstants, TowerConstants
from objectFormation import GameObjects

#Importing Towers
from towers.archerTower import ArcherTowerFar, ArcherTowerShort
from towers.supportTower import DamageTower, RangeTower
from towers.magicTower import FireTower, IceTower

#Importing main menu
from menu.menu import ShopMenu, GameStateButton

#Importing function to grab explosion images
from usefulFunctions import import_images_num_extended

from screens.ending_screen import EndingScreen

# Darken bg filter
dark_bg = pygame.image.load(os.path.join("images/screens", "dark.png")).convert_alpha()

#Game lives and money assets
life_image = pygame.image.load(os.path.join("images/lives", "heart.png"))
crystal_image = pygame.image.load(os.path.join("images/upgrade", "crystal_3.png"))
game_font = pygame.font.SysFont('comicsans', 52)

# Pause/Play buttons
play_round = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "button_start.png")), (60, 60))
pause_round = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "button_pause.png")), (60, 60))
play_music = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "button_music.png")), (60, 60))
pause_music = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "button_music_off.png")), (60, 60))

# Wave indicator
wave =  pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "wave.png")), (200, 50))

# Side-bar shop menu assets
side_bar_img = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "side_bar_img.png")), (150, 325))
buy_archer = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "bow.png")), (60, 60))
buy_crossbowman = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "crossbow.png")), (60, 60))
buy_support_dmg = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "damage_tower.png")), (60, 60))
buy_support_range = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "range_tower.png")), (60, 60))
buy_magic_fire = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "fire.png")), (60, 60))
buy_magic_ice = pygame.transform.scale(pygame.image.load(os.path.join("images/shop", "ice.png")), (60, 60))

# End game explosion
explosion = import_images_num_extended("images/screens/", 1, 51, (GameConstants.DIMENSIONS['game'][0], GameConstants.DIMENSIONS['game'][1]))

#Adding music
pygame.mixer.pre_init(44100, 16, 2, 4096)

class Game:
    """
    Main game screen where the entire game will be rendered in 
    @param (SURFACE) window: pygame surface to render
    @param (STR) map_label: to indicate what map will be active
    @param (STR) username: unique username identifier to grab stats that pertain specifically for that user
    """
    def __init__(self, window, map_label, username):
        self.window = window
        self.map_label = map_label
        self.username = username

        # Game dimensions
        self.width = GameConstants.DIMENSIONS['game'][0]
        self.height = GameConstants.DIMENSIONS['game'][1]

        # Tower variables
        self.archer_towers = []
        self.support_towers = []
        self.magic_towers = []

        #Enemy variables
        self.dead_enemies = set()
        self.enemies = []
        
        # Game currency
        self.money = 5000

        # Background images and schematics
        self.background_img = pygame.image.load(os.path.join("images", self.map_label + "_bg.png"))
        self.background_img = pygame.transform.scale(self.background_img, (GameConstants.DIMENSIONS['game'][0], GameConstants.DIMENSIONS['game'][1]))
        self.darken_background =  pygame.transform.scale(dark_bg, (self.width, self.height))

        # Spawning enemies
        self.timer = time.time()
        
        # Lives and life font
        self.font = game_font
        self.lives = 1

        # Selecting tower logistics
        self.tower_selected = None
        self.tower_clicked = None

        # Adding items to the shop
        if self.map_label != "map_2":
            self.shop_menu = ShopMenu(side_bar_img.get_width() // 2 - 10, 115, side_bar_img)
        else:
            self.shop_menu = ShopMenu(self.width - side_bar_img.get_width() // 2 + 5, 115, side_bar_img)

        # Adding all the buttons to the main shop
        self.add_items_to_shop(self.shop_menu)

        # Dragging the tower from the shop to a location
        self.drag_object = None

        # Logistics involving generating monster waves
        self.current_wave = 0
        self.cur_wave_amounts = EnemyConstants.ENEMY_WAVES_AMOUNT[self.current_wave][:]

        # Pausing the game
        self.pause_game = True
        self.game_state_button = GameStateButton(play_round, pause_round, self.width - play_round.get_width(),  wave.get_height() - 5)

        # Testing if the location of the tower is valid
        self.invalid_tower_placement = False
        self.invalid_tower_path_placement = False
        self.mouse_object = None

        # Music
        self.music = pygame.mixer.music
        self.music.load("maple.mp3")
        self.music.set_volume(0.5)
        self.music.play(-1)
        self.play_sound = True
        self.soundBtn = GameStateButton(play_music, pause_music, self.width - play_music.get_width() - play_round.get_width(), wave.get_height() - 5)
        self.soundBtn.switch_img()
        
        # Animating the explosion to indicate game over
        self.game_over = False
        self.game_over_animation_count = 0
        self.explosion_images = explosion
        self.ending_screen = None

        if self.tower_selected:
            self.tower_radius_surface = pygame.Surface((self.tower_selected.range * 4, self.tower_selected.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(self.tower_radius_surface, (128, 128, 128, 100), (self.tower_selected.range, self.tower_selected.range), self.tower_selected.range, 0)

        self.start_time = time.time()

    def add_items_to_shop(self, shop_menu):
        """
        Adds items to our main shop_menu
        @param (OBJECT) shop_menu: shop menu object that we can add items to

        --> return: None
        """
        shop_menu.add_button("bowman", buy_archer, 400)
        shop_menu.add_button("crossbowman", buy_crossbowman, 600)
        shop_menu.add_button("support_damage", buy_support_dmg, 800)
        shop_menu.add_button("support_range", buy_support_range, 1250)
        shop_menu.add_button("magic_fire", buy_magic_fire, 1500)
        shop_menu.add_button("magic_ice", buy_magic_ice, 2000)

    def spawn_enemies(self):
        """
        Spawn enemies based on the current wave

        --> return: None
        """
        if sum(self.cur_wave_amounts):
            ENEMY_WAVES_MONSTER_NAMES = {
                0: [Monster_1('monster_1', self.map_label), Monster_2('monster_2', self.map_label), Monster_3('monster_3', self.map_label), Monster_4('monster_4', self.map_label)],
                1: [Monster_1('monster_1', self.map_label), Monster_2('monster_2', self.map_label), Monster_3('monster_3', self.map_label), Monster_4('monster_4', self.map_label), Mano("mano", self.map_label)],
                2: [Monster_1('monster_1', self.map_label), Monster_2('monster_2', self.map_label), Monster_3('monster_3', self.map_label), Monster_4('monster_4', self.map_label)],
                3: [Monster_1('monster_1', self.map_label), Monster_2('monster_2', self.map_label), Monster_3('monster_3', self.map_label), Monster_4('monster_4', self.map_label), KingSlime("king_slime", self.map_label)],
                4: [Monster_5('monster_5', self.map_label), Monster_6('monster_6', self.map_label), Monster_7('monster_7', self.map_label), Monster_8('monster_8', self.map_label)],
                5: [Monster_5('monster_5', self.map_label), Monster_6('monster_6', self.map_label), Monster_7('monster_7', self.map_label), Monster_8('monster_8', self.map_label), Balrog("balrog", self.map_label)],
                6: [Monster_5('monster_5', self.map_label), Monster_6('monster_6', self.map_label), Monster_7('monster_7', self.map_label), Monster_8('monster_8', self.map_label)],
                7: [Monster_5('monster_5', self.map_label), Monster_6('monster_6', self.map_label), Monster_7('monster_7', self.map_label), Monster_8('monster_8', self.map_label), Pianus('pianus', self.map_label)],
                8: [Monster_1('monster_1', self.map_label), Monster_2('monster_2', self.map_label), Monster_3('monster_3', self.map_label), Monster_4('monster_4', self.map_label), Monster_5('monster_5', self.map_label), Monster_6('monster_6', self.map_label), Monster_7('monster_7', self.map_label), Monster_8('monster_8', self.map_label), Monster_9('monster_9', self.map_label), Monster_10('monster_10', self.map_label)],
                9: [Monster_1('monster_1', self.map_label), Monster_2('monster_2', self.map_label), Monster_3('monster_3', self.map_label), Monster_4('monster_4', self.map_label), Monster_5('monster_5', self.map_label), Monster_6('monster_6', self.map_label), Monster_7('monster_7', self.map_label), Monster_8('monster_8', self.map_label), Monster_9('monster_9', self.map_label), Monster_10('monster_10', self.map_label), PinkBean('pink_bean', self.map_label)],
            }

            for i, amount in enumerate(self.cur_wave_amounts):
                if amount:
                    self.enemies.append(ENEMY_WAVES_MONSTER_NAMES[self.current_wave][i])
                    self.cur_wave_amounts[i] -= 1
                    break
        else:
            if not self.enemies and self.current_wave <= 9:
                self.current_wave += 1
                if self.current_wave <= 9:
                    self.cur_wave_amounts = EnemyConstants.ENEMY_WAVES_AMOUNT[self.current_wave]
                self.pause_game = True
                self.game_state_button.image = self.game_state_button.images[0]

                reset = True
                for enemy in self.dead_enemies:
                    if enemy.dead:
                        reset = False
                        break

                if reset:
                    self.dead_enemies = set()

    def set_tower_drag_object(self, name):
        """
        Attempts to match the tower with the associated tower object and sets self.drag_object to that tower object and
        sets the tower's dragged property as True
        @param (STR) name: name of the tower object

        --> return: None
        """
        x, y = pygame.mouse.get_pos()
        tower_obj_pair = {"bowman": ArcherTowerFar("bowman", (x, y)), "crossbowman": ArcherTowerShort("crossbowman", (x, y)), "support_damage": DamageTower("support_damage", (x, y)), "support_range": RangeTower("support_range", (x, y)), "magic_fire": FireTower("magic_fire", (x, y)), "magic_ice": IceTower("magic_ice", (x, y))}
        try:
            tower_obj = tower_obj_pair[name]
            self.drag_object = tower_obj
            tower_obj.dragged = True
        except Exception as error:  
            print(error + " " + "Invalid Name")

    def run_game(self):
        """
        Main game loop to keep the game continuously running 

        --> return: None
        """
        ongoing = True
        clock = pygame.time.Clock()

        while ongoing:
            clock.tick(120)

            if not self.play_sound:
                self.music.pause()
            else:
                self.music.unpause()

            if not self.pause_game:
                # Spawn enemies
                if time.time() - self.timer >= random.randint(1, 6) / 3:
                    self.timer = time.time()
                    self.spawn_enemies()

            pos = pygame.mouse.get_pos()


            # Checking for tower collisions when we are trying to place the tower on the board
            if self.drag_object:
                self.drag_object.move(pos[0], pos[1])

                # Tower collision with the path
                if self.drag_object.get_closest_distance_to_path(GameConstants.PATH[self.map_label]) < 80:
                    self.invalid_tower_path_placement = (self.drag_object, (self.drag_object.x, self.drag_object.y))
                else:
                    self.invalid_tower_path_placement = None

                all_towers = self.archer_towers[:] + self.support_towers[:] + self.magic_towers[:]
                tower_obj = GameObjects(self.drag_object.name, (pos[0], pos[1])) #initiate a new tower_obj to update position

                for tower in all_towers:
                    if tower_obj.does_collides(tower):
                        self.invalid_tower_placement = (tower, (tower.x, tower.y))
                        break
                    else:
                        self.invalid_tower_placement = None
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ongoing = False

                if event.type == pygame.MOUSEBUTTONUP:
                    # Resets the drag object if we don't wish to buy the tower
                    if self.drag_object and self.shop_menu.get_clicked_item(pos[0], pos[1]):
                        self.drag_object = None
                        continue

                    # While we have our drag object and we press down, then we will buy that tower and place it accordingly on the board
                    if self.drag_object and not self.invalid_tower_placement and not self.invalid_tower_path_placement:
                        self.drag_object.coord = (pos[0], pos[1])

                        if self.drag_object.name in TowerConstants.ATT_TOWER_NAMES:
                            self.archer_towers.append(self.drag_object)
                        elif self.drag_object.name in TowerConstants.SUP_TOWER_NAMES:
                            self.support_towers.append(self.drag_object)
                        else:
                            self.magic_towers.append(self.drag_object)

                        if self.money >= self.shop_menu.get_item_cost(self.drag_object.name):
                            self.money -= self.shop_menu.get_item_cost(self.drag_object.name)

                        # Resets our dragging paramaters
                        self.drag_object.dragged = False
                        self.drag_object = None


                    # Not currently being moved around the map
                    elif not self.drag_object:
                        # Checking for the current wave state of the game (Paused or play)
                        if self.game_state_button.click(pos[0], pos[1]) and not self.enemies:
                            self.pause_game = not self.pause_game
                            self.game_state_button.switch_img()

                        # Checking for the current sound state of the game (Paused or play)
                        if self.soundBtn.click(pos[0], pos[1]):
                            self.play_sound = not self.play_sound
                            self.soundBtn.switch_img()

                        #Clicking on main menu      
                        shop_item_name = self.shop_menu.get_clicked_item(pos[0], pos[1])  

                        # Sets the drag object as the tower object from the shop menu if we have enough money
                        if shop_item_name: 
                            if self.money >= self.shop_menu.get_item_cost(shop_item_name):
                                self.set_tower_drag_object(shop_item_name)
                        

                        #Currently pressing on an item on the tower menu
                        if self.tower_clicked:   
                            self.tower_clicked = self.tower_selected.menu.get_clicked_item(pos[0], pos[1])
                            tower_cost = self.tower_selected.get_upgrade_cost()

                            # Upgrading item on the tower menu via the upgrade button
                            if self.tower_clicked == "upgrade" and isinstance(tower_cost, int) and self.money >= tower_cost:
                                self.money -= self.tower_selected.get_upgrade_cost()
                                self.tower_selected.upgrade()

                            # Selling the tower when clicking on the undo button on the tower menu
                            if self.tower_clicked == "sell":
                                self.money += self.tower_selected.get_sell_cost()
                                if self.tower_selected.name in TowerConstants.ATT_TOWER_NAMES: #Remove from att towers
                                    self.archer_towers.remove(self.tower_selected)
                                elif self.tower_selected.name in TowerConstants.SUP_TOWER_NAMES: #Remove from supp towers
                                    self.support_towers.remove(self.tower_selected)
                                else: #Remove from magic towers
                                    self.magic_towers.remove(self.tower_selected)

                            self.tower_selected = None
                            self.tower_clicked = False
                            

                        # If we're not on the menu of an item
                        if not self.tower_clicked:
                            all_towers = self.archer_towers[:] + self.support_towers[:] + self.magic_towers[:]
                            for t in all_towers:
                                if t.click(pos[0], pos[1]):
                                    t.selected = True
                                    self.tower_selected = t
                                    self.tower_clicked = True

                                    self.tower_radius_surface = pygame.Surface((self.tower_selected.range * 4, self.tower_selected.range * 4), pygame.SRCALPHA, 32)
                                    pygame.draw.circle(self.tower_radius_surface, (128, 128, 128, 100), (self.tower_selected.range, self.tower_selected.range), self.tower_selected.range, 0)
                                    break

                            for t in all_towers:
                                if not t.click(pos[0], pos[1]):
                                    t.selected = False
                                    
            if not self.pause_game:
                # Appending to a new list enemeies that are off the screen as indicated by the e.move() return value
                delete_enemies = []
                for e in self.enemies:
                    e.update_speed_status(set(filter(lambda tower: (tower.name == 'magic_ice'), self.magic_towers))) #Updating enemy speed if not in presence of ice towers
                    if not e.move():
                        delete_enemies.append(e)

                # Deleting enemies off the screen (bosses take away more lives)
                for e in delete_enemies:
                    if e.name in EnemyConstants.BOSS_NAMES:
                        self.lives -= 5
                    else:
                        self.lives -= 1
                    self.enemies.remove(e)


                # Looping through attack towers and attack enemies if any are in range
                for t in self.archer_towers:
                    self.money += t.attack(self.enemies, self.dead_enemies)

                # Looping through magic towers and attack enemies if they are in range
                for t in self.magic_towers:
                    self.money += t.attack(self.enemies, self.dead_enemies)

                # Looping through support towers and supporting nearby towers if they are in range
                for t in self.support_towers:
                    attack_towers = self.archer_towers[:] + self.magic_towers[:]
                    t.support(attack_towers)

                
            # Proceed to the ending_screen if we have beaten all the levels or we've ran out of all the lives
            if self.lives <= 0 or self.current_wave == 10:
                self.pause_game = True
                self.game_over = True
          
                if self.ending_screen:
                    # Formatting time to be "MM:SS"
                    total_seconds = round(time.time() - self.start_time)

                    seconds = total_seconds % 60
                    minutes = total_seconds // 60

                    if seconds < 10:
                        seconds = "0" + str(seconds)
                    if minutes < 10:
                        minutes = "0" + str(minutes)

                    formatted_time = str(minutes) + ":" + str(seconds)

                    if self.current_wave == 10:
                        wave_num = 10
                    else:
                        wave_num = self.current_wave + 1

                    # Push statistics data into database
                    if not collection.find_one({"_id": self.username+ "_" +self.map_label}):
                        collection.insert_one({"_id": self.username+ "_" +self.map_label, "username": self.username, "game_time": formatted_time, "lives": self.lives, "wave_number": wave_num, "map_label": self.map_label})
                    else:
                        collection.find_one_and_update({"_id": self.username+ "_" +self.map_label, "map_label": self.map_label}, {"$set": {"username": self.username, "game_time": formatted_time, "lives": self.lives, "wave_number": wave_num, "map_label": self.map_label}})

                    ongoing = False

                    if self.current_wave == 10:
                        ending_screen = EndingScreen(self.window, "victory", self.username, self.map_label)
                    else:
                        ending_screen = EndingScreen(self.window, "defeat", self.username, self.map_label)

                    if ending_screen.run_game() == 'restart':



                        return 'restart'
                    del ending_screen

            self.draw()

        pygame.quit()

    def draw(self):
        """
        Draws all the towers, messages, and texts on the screen while the game is continuously running

        --> return: None
        """
        self.window.blit(self.background_img, (0, 0))

        # Background gets darker and we play the explosion animation
        if self.game_over:
            self.window.blit(self.darken_background, (0, 0))
            self.window.blit(self.explosion_images[self.game_over_animation_count], (0, 0))
            self.game_over_animation_count += 1
            if self.game_over_animation_count == len(self.explosion_images):
                self.ending_screen = True
        
        # Blits the tower radius when selecting towers
        if self.tower_selected: 
            self.window.blit(self.tower_radius_surface, (self.tower_selected.x - self.tower_selected.range, self.tower_selected.y - self.tower_selected.range))

        # Drawing towers
        for a in self.archer_towers:
            a.draw(self.window)
        for s in self.support_towers:
            s.draw(self.window)
        for m in self.magic_towers:
            m.draw(self.window)

        # Drawing enemies
        for e in self.enemies:
            e.draw(self.window)
        
        # Drawing animation of dead enemies
        for dead_enemy in self.dead_enemies:
            dead_enemy.die(self.window)

        # Drawing the red circles around invalid tower placements based on other towers or the path itself
        if self.invalid_tower_placement:
            s = pygame.Surface((60 * 5, 60 * 5), pygame.SRCALPHA, 32)
            pygame.draw.circle(s, (224, 94, 94, 100), (60, 60), 60, 0)
            self.window.blit(s, (self.invalid_tower_placement[1][0] - 60, self.invalid_tower_placement[1][1] - 60))

        if self.invalid_tower_path_placement:
            s = pygame.Surface((60 * 5, 60 * 5), pygame.SRCALPHA, 32)
            pygame.draw.circle(s, (224, 94, 94, 100), (60, 60), 60, 0)
            self.window.blit(s, (self.invalid_tower_path_placement[1][0] - 60, self.invalid_tower_path_placement[1][1] - 60))

        # Draw the tower being dragged (puts the tower on higher priority when trying to blit with other images)
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


        #Redrawing the selected tower so that it has the highest priority
        if self.tower_selected:
            self.tower_selected.draw(self.window)


        #Drawing game state button
        self.game_state_button.draw(self.window)


        #Drawing music button
        self.soundBtn.draw(self.window)


        #Drawing the wave indicator
        self.window.blit(wave, (self.width - wave.get_width() + 30, -10)) #Wave BG
        if self.current_wave == 10:
            wave_txt = self.font.render("Wave: " + str(self.current_wave), 1, (255, 255, 255))
        else:
            wave_txt = self.font.render("Wave: " + str(self.current_wave + 1), 1, (255, 255, 255))

        self.window.blit(wave_txt, (self.width - wave_txt.get_width() // 2 - wave.get_width() // 2 + 15, 5))


        pygame.display.update()
