# Will contain all the constants needed for the game
from usefulFunctions import import_images_name

class Constants:
    """
    A collection of game-specific constants.
    """ 
    #Dimensions are of the form (width, height)
    DIMENSIONS = {
        'game': (1350, 700),
        'path': (35, 35),
        'monster': (64, 64),
        'boss': (100, 100),
        'att_tower': (135, 135),
        'supp_tower': (80, 80),
        'menu': (130, 70),
    }

    # ENEMY_SPEED = {
    #     'slime': 5,
    #     'cubeSlime': 5,
    #     'angrySlime': 5,
    #     'testEnemy': 5,
    #     'golem': 5, 
    #     'balrog': 5,
    #     'monster_1': 5,
    #     'monster_2': 5,
    #     'monster_3': 5,
    #     'monster_4': 5
    # }

    HEALTH = {
        # Monsters
        'monster_1': 5,
        'monster_2': 10,
        'monster_3': 15,
        'monster_4': 20,

        # Bosses
        'balrog': 200,
        'king_slime': 100,
        'mano': 500, 
        'pianus': 1000,
        'pink_bean': 5000
    }

    ENEMY_CRYSTALS = {
        # Monsters
        'monster_1': 1000,
        'monster_2': 1000,
        'monster_3': 1000,
        'monster_4': 1000,

        # bosses
        'mano': 5000,
        'king_slime': 1000,
        'balrog': 20000, 
        'pianus': 50000,
        'pink_bean': 100000
    }

    TOWER_ATT_SPEED = {
        'bowman': 10,
        'crossbowman': 20
    }

    TOWER_RADIUS_RANGE = {
        'bowman': 200,
        'crossbowman': 150,
        'support_damage': 150,
        'support_range': 150
    }

    UPGRADE_COST = {
        'bowman': [2750, 5500, "MAX"],
        'crossbowman': [1000, 5000, "MAX"],
        'support_damage': [350, 900, "MAX"],
        'support_range': [500, 1250, "MAX"]
    }

    # Enemy waves are in the format of a wave #: (amount of monsters in each category)
    # The tuple formed are formatted (monster 1, monster 2, monster 3, monster 4)
    ENEMY_WAVES_AMOUNT = {
        1: (10, 5, 7, 10),
        2: (6, 10, 8, 12),
        3: (9, 10, 12, 8),
        4: (10, 8, 12, 9),
        5: (12, 10, 9, 15)
    }

    # Enemy waves are in the format of wave #: (name of monster in each category)
    # The tuple formed are formatted (monster 1, monster 2, monster 3, monster 4)
    ENEMY_WAVES_MONSTER = {

    }

    # After every round, there will be a boss
    # --> below is the round #: boss name (key, value) pairing
    BOSS_WAVES = {
        1: (10, 5, 7, 10),
        2: (6, 10, 8, 12),
        3: (9, 10, 12, 8),
        4: (10, 8, 12, 9),
        5: (12, 10, 9, 15)
    }

    # Names of attack and support towers 
    ATT_TOWER_NAMES = ['bowman', 'crossbowman']
    SUP_TOWER_NAMES = ['support_damage', 'support_range']

    # Names of monsters and bosses in the waves
    MONSTER_NAMES = ['monster_1', 'monster_2', 'monster_3', 'monster_4', 'monster_5', 'monster_6', 'monster_7', 'monster_8', 'monster_9', 'monster_10']
    BOSS_NAMES = ['mano', 'king_slime', 'balrog', 'pianus', 'pink_bean']

    # Collection of all the moving sprite images
    ENEMY_MOVING_SPRITE_IMAGES = {
        # Monsters
        'monster_1': import_images_name("images/enemies/monster/monster_1", "9_enemies_1_walk_0", 0, 20, (100, 100)),
        'monster_2': import_images_name("images/enemies/monster/monster_2", "1_enemies_1_walk_0", 0, 20, (100, 100)),
        'monster_3': import_images_name("images/enemies/monster/monster_3", "7_enemies_1_walk_0", 0, 20, (100, 100)),
        'monster_4': import_images_name("images/enemies/monster/monster_4", "10_enemies_1_walk_0", 0, 20, (100, 100)),

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
        'monster_1': import_images_name("images/enemies/monster/monster_1", "9_enemies_1_die_0", 0, 20, (100, 100)),
        'monster_2': import_images_name("images/enemies/monster/monster_2", "1_enemies_1_die_0", 0, 20, (100, 100)),
        'monster_3': import_images_name("images/enemies/monster/monster_3", "7_enemies_1_die_0", 0, 20, (100, 100)),
        'monster_4': import_images_name("images/enemies/monster/monster_4", "10_enemies_1_die_0", 0, 20, (100, 100)),

        # Bosses
        'mano': import_images_name("images/enemies/boss/mano", "die_0", 1, 10, (150, 150)),
        'king_slime': import_images_name("images/enemies/boss/king_slime", "die_0", 1, 9, (150, 150)),
        'balrog': import_images_name("images/enemies/boss/balrog", "die_0", 1, 3, (150, 150)),
        'pianus': import_images_name("images/enemies/boss/pianus", "die_0", 1, 10, (150, 150)),
        'pink_bean': import_images_name("images/enemies/boss/pink_bean", "die_0", 1, 7)
    }
    
    # The additional buffer to // by during animation count and to * by during len(images) to slow down images 
    # --> the higher the buffer --> the slower the image rotation will be
    SLOW_ENEMY_MOVE_ANIMATION_BUFFER = { 
        'monster': 1,
        'mano': 3,
        'king_slime': 4,
        'balrog': 5,
        'pianus': 2,
        'pink_bean': 2
    }

    SLOW_ENEMY_DEATH_ANIMATION_BUFFER = { 
        'monster': 1,
        'mano': 5,
        'king_slime': 5,
        'balrog': 15,
        'pianus': 4,
        'pink_bean': 2
    }

    PATH_CORNERS = [(0, 526), (126, 526), (183, 499), (207, 452), (217, 400), (228, 356), (266, 320), (320, 307), (371, 298), (421, 263), (435, 216), (446, 165), (473, 108), (540, 87), (600, 86), (662, 88), (716, 90), (764, 78), (821, 66), (870, 71), (942, 83), (1011, 94), (1068, 92), (1127, 117), (1156, 155), (1165, 233), (1130, 270), (1061, 298), (1005, 313), (961, 343), (945, 386), (944, 435), (947, 464), (971, 496), (1024, 518), (1079, 534), (1124, 565), (1140, 615), (1149, 667), (1168, 682)]