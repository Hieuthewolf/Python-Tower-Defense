# Will contain all the constants needed for the game
from usefulFunctions import import_images_name
from enemies.monster import *

class GameConstants:
    """
    A collection of game-specific constants for the layout of the games and for the monsters
    """ 
    #Dimensions are of the form (width, height)
    DIMENSIONS = {
        'game': (1350, 700),
        'path': (35, 35),
        'monster': (80, 80),
        'boss': (150, 150),
        'att_tower': (80, 145), # The additional height is due to the archer on top and extra padding for menu
        'supp_tower': (80, 105), # The additional height helps to pad the popup menu (give or take 25)
        'magic_tower': (80, 175), # The additional height is due to the orb classifier on top and extra padding for menu
        'menu': (130, 70),
    }

    # Names of monsters and bosses in the waves
    PATH = [(0, 531), (50, 531), (136, 518), (195, 496), (232, 424), (263, 349), (358, 312), (438, 285), (475, 217), (499, 133), (581, 101), (664, 101), (733, 94), (822, 83), (889, 72), (984, 80), (1075, 88), (1175, 94), (1235, 154), (1264, 228), (1184, 286), (1094, 310), (1035, 361), (1011, 435), (1065, 486), (1136, 507), (1219, 550), (1252, 639), (1260, 677)]
    INDIVIDUAL_PATH_COORDINATES = ()

class EnemyConstants:
    """
    A collection of enemy-related constants 
    """

    # The additional buffer to // by during animation count and to * by during len(images) to slow down images 
    # --> the higher the buffer --> the slower the image rotation will be
    SLOW_ENEMY_MOVE_ANIMATION_BUFFER = { 
        'monster': 1,
        'mano': 3,
        'king_slime': 4,
        'balrog': 5,
        'pianus': 2,
        'pink_bean': 3
    }

    SLOW_ENEMY_DEATH_ANIMATION_BUFFER = { 
        'monster': 1,
        'mano': 5,
        'king_slime': 5,
        'balrog': 15,
        'pianus': 4,
        'pink_bean': 10
    }

    MONSTER_NAMES = ['monster_1', 'monster_2', 'monster_3', 'monster_4', 'monster_5', 'monster_6', 'monster_7', 'monster_8', 'monster_9', 'monster_10']
    BOSS_NAMES = ['mano', 'king_slime', 'balrog', 'pianus', 'pink_bean']

    HEALTH = {
        # Monsters
        'monster_1': 6,
        'monster_2': 8,
        'monster_3': 12,
        'monster_4': 16,
        'monster_5': 18,
        'monster_6': 24,
        'monster_7': 26,
        'monster_8': 32,
        'monster_9': 34,
        'monster_10': 40,

        # Bosses
        'balrog': 100,
        'king_slime': 200,
        'mano': 300, 
        'pianus': 400,
        'pink_bean': 500
    }

    ENEMY_CRYSTALS = {
        # Monsters
        'monster_1': 6,
        'monster_2': 8,
        'monster_3': 12,
        'monster_4': 16,
        'monster_5': 18,
        'monster_6': 24,
        'monster_7': 26,
        'monster_8': 32,
        'monster_9': 34,
        'monster_10': 40,

        # Bosses
        'mano': 1000,
        'king_slime': 2000,
        'balrog': 3000, 
        'pianus': 4000,
        'pink_bean': 5000
    }

    # Enemy waves are in the format of a wave #: (amount of monsters in each category, total_amount)
    # The tuple formed are formatted (monster 1, monster 2, monster 3, monster 4)
    # ENEMY_WAVES_AMOUNT = {
    #     0: [1, 1, 1, 1],
    #     1: [1, 1, 1, 1],
    #     2: [1, 1, 1, 1],
    #     3: [1, 1, 1, 1],
    #     4: [1, 1, 1, 1],
    #     5: [1, 1, 1, 1],
    #     6: [1, 1, 1, 1],
    #     7: [1, 1, 1, 1],
    #     8: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #     9: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #     10: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    # }
    

    ENEMY_WAVES_AMOUNT = {
        0: [35, 25, 15, 10],
        1: [10, 35, 25, 15],
        2: [15, 10, 35, 25],
        3: [10, 15, 25, 35],
        4: [50, 35, 25, 15],
        5: [15, 50, 35, 25],
        6: [25, 15, 50, 35],
        7: [15, 25, 35, 50],
        8: [15, 15, 15, 15, 15, 15, 15, 15, 35, 35],
        9: [20, 20, 20, 20, 20, 20, 20, 20, 50, 50]
    }

    # After every round, there will be a boss
    # --> below is the round #: boss name (key, value) pairing
    BOSS_WAVES = {
        0: 'mano',
        1: 'king_slime',
        2: 'balrog',
        3: 'pianus',
        4: 'pink_bean'
    }

class EnemyImagesConstants:
    """
    A collection of monster sprite images 
    """

    # Collection of all the moving sprite images
    ENEMY_MOVING_SPRITE_IMAGES = {
        # Monsters
        'monster_1': import_images_name("images/enemies/monster/monster_1", "9_enemies_1_walk_0", 0, 20, (80, 80)),
        'monster_2': import_images_name("images/enemies/monster/monster_2", "1_enemies_1_walk_0", 0, 20, (80, 80)),
        'monster_3': import_images_name("images/enemies/monster/monster_3", "7_enemies_1_walk_0", 0, 20, (80, 80)),
        'monster_4': import_images_name("images/enemies/monster/monster_4", "10_enemies_1_walk_0", 0, 20, (80, 80)),
        'monster_5': import_images_name("images/enemies/monster/monster_5", "2_enemies_1_walk_0", 0, 20, (80, 80)),
        'monster_6': import_images_name("images/enemies/monster/monster_6", "8_enemies_1_walk_0", 0, 20, (80, 80)),
        'monster_7': import_images_name("images/enemies/monster/monster_7", "3_enemies_1_walk_0", 0, 20, (80, 80)),
        'monster_8': import_images_name("images/enemies/monster/monster_8", "6_enemies_1_walk_0", 0, 20, (80, 80)),
        'monster_9': import_images_name("images/enemies/monster/monster_9", "4_enemies_1_walk_0", 0, 20, (80, 80)),
        'monster_10': import_images_name("images/enemies/monster/monster_10", "5_enemies_1_walk_0", 0, 20, (80, 80)),

        # Bosses
        'mano': import_images_name("images/enemies/boss/mano", "move_0", 1, 11, (150, 150)),
        'king_slime': import_images_name("images/enemies/boss/king_slime", "move_0", 1, 8, (150, 150)),
        'balrog': import_images_name("images/enemies/boss/balrog", "move_0", 1, 6, (150, 150)),
        'pianus': import_images_name("images/enemies/boss/pianus", "move_0", 1, 13, (150, 150)),
        'pink_bean': import_images_name("images/enemies/boss/pink_bean", "move_0", 1, 23)
    }

    # Collection of all death animation sprite images
    ENEMY_DEATH_SPRITE_IMAGES = {
        # Monsters 
        'monster_1': import_images_name("images/enemies/monster/monster_1", "9_enemies_1_die_0", 0, 20, (80, 80)),
        'monster_2': import_images_name("images/enemies/monster/monster_2", "1_enemies_1_die_0", 0, 20, (80, 80)),
        'monster_3': import_images_name("images/enemies/monster/monster_3", "7_enemies_1_die_0", 0, 20, (80, 80)),
        'monster_4': import_images_name("images/enemies/monster/monster_4", "10_enemies_1_die_0", 0, 20, (80, 80)),
        'monster_5': import_images_name("images/enemies/monster/monster_5", "2_enemies_1_die_0", 0, 20, (80, 80)),
        'monster_6': import_images_name("images/enemies/monster/monster_6", "8_enemies_1_die_0", 0, 20, (80, 80)),
        'monster_7': import_images_name("images/enemies/monster/monster_7", "3_enemies_1_die_0", 0, 20, (80, 80)),
        'monster_8': import_images_name("images/enemies/monster/monster_8", "6_enemies_1_die_0", 0, 20, (80, 80)),
        'monster_9': import_images_name("images/enemies/monster/monster_9", "4_enemies_1_die_0", 0, 20, (80, 80)),
        'monster_10': import_images_name("images/enemies/monster/monster_10", "5_enemies_1_die_0", 0, 20, (80, 80)),

        # Bosses
        'mano': import_images_name("images/enemies/boss/mano", "die_0", 1, 10, (150, 150)),
        'king_slime': import_images_name("images/enemies/boss/king_slime", "die_0", 1, 9, (150, 150)),
        'balrog': import_images_name("images/enemies/boss/balrog", "die_0", 1, 3, (150, 150)),
        'pianus': import_images_name("images/enemies/boss/pianus", "die_0", 1, 10, (150, 150)),
        'pink_bean': import_images_name("images/enemies/boss/pink_bean", "die_0", 1, 7)
    }

class TowerConstants:
    """
    A collection of tower-related constants
    """

    TOWER_ATT_SPEED = {
        'bowman': 10,
        'crossbowman': 20
    }

    TOWER_RADIUS_RANGE = {
        'bowman': 200,
        'crossbowman': 150,
        'support_damage': 150,
        'support_range': 150,
        'magic_fire': 250,
        'magic_ice': 250
    }

    UPGRADE_COST = {
        'bowman': [2750, 5500, "MAX"],
        'crossbowman': [1000, 5000, "MAX"],
        'support_damage': [350, 900, "MAX"],
        'support_range': [500, 1250, "MAX"],
        'magic_fire': [500, 1250, "MAX"],
        'magic_ice': [500, 1250, "MAX"],
    }

    ORIGINAL_PRICE = {
        'bowman': 400,
        'crossbowman': 600,
        'support_damage': 800,
        'support_range': 1250,
        'magic_fire': 1500,
        'magic_ice': 2000
    }

    # Names of attack, support towers, and magic towers
    ATT_TOWER_NAMES = ['bowman', 'crossbowman']
    SUP_TOWER_NAMES = ['support_damage', 'support_range']
    MAGIC_TOWER_NAMES = ['magic_fire', 'magic_ice']
