# Will contain all the constants needed for the game
from usefulFunctions import import_images_name
from enemies.monster import *

class GameConstants:
    """
    A collection of game-specific constants for the layout of the games and for the monsters
    """ 
    #Dimensions are of the form (width, height)
    DIMENSIONS = {
        'game': (1350, 750),
        'path': (35, 35),
        'monster': (70, 70),
        'boss': (150, 150),
        'att_tower': (80, 135), # The additional height is due to the archer on top and extra padding for menu
        'supp_tower': (80, 105), # The additional height helps to pad the popup menu (give or take 25)
        'magic_tower': (80, 110), # The additional height is due to the orb classifier on top and extra padding for menu
        'menu': (130, 70),
    }


    # Names of monsters and bosses in the waves
    PATH = {
        'map_1': [
                    [(1, 564), (102, 565), (177, 551), (220, 506), (239, 448), (251, 379), (307, 345), (386, 326), (444, 290), (470, 230), (485, 163), (532, 109), (617, 95), (686, 95), (751, 95), (800, 93), (867, 81), (927, 69), (996, 87), (1064, 94), (1130, 94), (1190, 106), (1225, 133), (1243, 190), (1246, 241), (1214, 296), (1159, 320), (1094, 333), (1041, 364), (1021, 416), (1019, 468), (1035, 519), (1081, 553), (1151, 568), (1209, 593), (1239, 645), (1250, 693), (1253, 739)]
                 ],
        'map_2': [
                    [(345, 748), (328, 678), (280, 631), (205, 610), (146, 582), (109, 515), (119, 450), (166, 400), (237, 382), (303, 355), (339, 301), (350, 230), (384, 176), (446, 147), (511, 143), (570, 145), (617, 144), (673, 148), (733, 178), (760, 225), (760, 269), (760, 333), (760, 385), (760, 441), (774, 499), (809, 532), (853, 575), (909, 576), (950, 576), (983, 504), (999, 448), (1003, 387), (1003, 324), (1003, 267), (1003, 218), (1003, 169), (1003, 124), (1003, 70), (1003, 24), (1003, 1)],
                    [(345, 748), (328, 678), (280, 631), (205, 610), (146, 582), (109, 515), (119, 450), (166, 400), (237, 382), (303, 355), (339, 301), (350, 230), (384, 176), (446, 147), (511, 143), (570, 145), (617, 144), (673, 148), (733, 178), (760, 225), (760, 269), (760, 333), (760, 385), (760, 441), (774, 499), (809, 532), (853, 576), (909, 575), (950, 576), (1017, 576), (1084, 574), (1136, 575), (1194, 576), (1254, 574), (1304, 576), (1344, 575)],
                 ],
        'map_3': [
                    [(0, 589), (60, 589), (122, 592), (176, 591), (227, 587), (283, 590), (326, 591), (380, 581), (422, 551), (449, 507), (460, 450), (485, 390), (526, 364), (582, 357), (642, 377), (681, 410), (739, 417), (797, 399), (836, 361), (860, 310), (867, 248), (899, 205), (951, 181), (1014, 176), (1074, 176), (1129, 176), (1180, 180), (1235, 202), (1280, 230), (1324, 231), (1346, 228)],
                    [(0, 589), (60, 589), (122, 592), (176, 591), (227, 587), (283, 590), (326, 591), (380, 581), (422, 551), (449, 507), (460, 450), (485, 390), (526, 364), (582, 357), (642, 377), (691, 459), (699, 503), (718, 539), (745, 572), (790, 589), (847, 589), (895, 591), (937, 589), (984, 591), (1021, 589), (1065, 588), (1109, 591), (1153, 591), (1202, 591), (1242, 593), (1282, 586), (1316, 592), (1346, 592)]
                 ],
        'map_4': [
                    [(74, 748), (117, 711), (168, 680), (235, 661), (281, 632), (318, 590), (356, 557), (389, 524), (424, 486), (466, 446), (456, 377), (455, 313), (493, 260), (556, 232), (621, 223), (688, 223), (747, 229), (806, 240), (849, 255), (880, 223), (914, 180), (951, 141), (993, 111), (1035, 89), (1073, 77), (1126, 91), (1164, 128), (1199, 164), (1239, 204), (1274, 238), (1308, 268), (1345, 300)],
                    [(74, 748), (117, 711), (168, 680), (235, 661), (281, 632), (318, 590), (356, 557), (389, 524), (424, 486), (466, 446), (528, 455), (585, 462), (645, 462), (701, 463), (762, 457), (811, 435), (850, 396), (869, 343), (862, 290), (849, 256), (879, 225), (915, 178), (951, 143), (996, 110), (1034, 90), (1073, 76), (1126, 92), (1165, 125), (1199, 163), (1238, 202), (1273, 236), (1309, 269), (1347, 301)]
                 ]
    }

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

    ENEMY_WAVES_AMOUNT = {
        0: [1, 1, 1, 1],
        1: [1, 1, 1, 1],
        2: [1, 1, 1, 1],
        3: [1, 1, 1, 1],
        4: [1, 1, 1, 1],
        5: [1, 1, 1, 1],
        6: [1, 1, 1, 1],
        7: [1, 1, 1, 1],
        8: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        9: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }

    # Enemy waves are in the format of a wave #: (amount of monsters in each category, total_amount)
    # The tuple formed are formatted (monster 1, monster 2, monster 3, monster 4)
    # ENEMY_WAVES_AMOUNT = {
    #     0: [35, 25, 15, 10],
    #     1: [10, 35, 25, 15],
    #     2: [15, 10, 35, 25],
    #     3: [10, 15, 25, 35],
    #     4: [50, 35, 25, 15],
    #     5: [15, 50, 35, 25],
    #     6: [25, 15, 50, 35],
    #     7: [15, 25, 35, 50],
    #     8: [15, 15, 15, 15, 15, 15, 15, 15, 35, 35],
    #     9: [20, 20, 20, 20, 20, 20, 20, 20, 50, 50]
    # }

    # After every round, there will be a boss
    # --> below is the round #: boss name (key, value) pairing
    BOSS_WAVES = {
        0: 'mano',
        1: 'king_slime',
        2: 'balrog',
        3: 'pianus',
        4: 'pink_bean'
    }

    # Collection of all the moving sprite images
    ENEMY_MOVING_SPRITE_IMAGES = {
        # Monsters
        'monster_1': import_images_name("images/enemies/monster/monster_1", "9_enemies_1_walk_0", 0, 20, (70, 70)),
        'monster_2': import_images_name("images/enemies/monster/monster_2", "1_enemies_1_walk_0", 0, 20, (70, 70)),
        'monster_3': import_images_name("images/enemies/monster/monster_3", "7_enemies_1_walk_0", 0, 20, (70, 70)),
        'monster_4': import_images_name("images/enemies/monster/monster_4", "10_enemies_1_walk_0", 0, 20, (70, 70)),
        'monster_5': import_images_name("images/enemies/monster/monster_5", "2_enemies_1_walk_0", 0, 20, (70, 70)),
        'monster_6': import_images_name("images/enemies/monster/monster_6", "8_enemies_1_walk_0", 0, 20, (70, 70)),
        'monster_7': import_images_name("images/enemies/monster/monster_7", "3_enemies_1_walk_0", 0, 20, (70, 70)),
        'monster_8': import_images_name("images/enemies/monster/monster_8", "6_enemies_1_walk_0", 0, 20, (70, 70)),
        'monster_9': import_images_name("images/enemies/monster/monster_9", "4_enemies_1_walk_0", 0, 20, (70, 70)),
        'monster_10': import_images_name("images/enemies/monster/monster_10", "5_enemies_1_walk_0", 0, 20, (70, 70)),

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
        'monster_1': import_images_name("images/enemies/monster/monster_1", "9_enemies_1_die_0", 0, 20, (70, 70)),
        'monster_2': import_images_name("images/enemies/monster/monster_2", "1_enemies_1_die_0", 0, 20, (70, 70)),
        'monster_3': import_images_name("images/enemies/monster/monster_3", "7_enemies_1_die_0", 0, 20, (70, 70)),
        'monster_4': import_images_name("images/enemies/monster/monster_4", "10_enemies_1_die_0", 0, 20, (70, 70)),
        'monster_5': import_images_name("images/enemies/monster/monster_5", "2_enemies_1_die_0", 0, 20, (70, 70)),
        'monster_6': import_images_name("images/enemies/monster/monster_6", "8_enemies_1_die_0", 0, 20, (70, 70)),
        'monster_7': import_images_name("images/enemies/monster/monster_7", "3_enemies_1_die_0", 0, 20, (70, 70)),
        'monster_8': import_images_name("images/enemies/monster/monster_8", "6_enemies_1_die_0", 0, 20, (70, 70)),
        'monster_9': import_images_name("images/enemies/monster/monster_9", "4_enemies_1_die_0", 0, 20, (70, 70)),
        'monster_10': import_images_name("images/enemies/monster/monster_10", "5_enemies_1_die_0", 0, 20, (70, 70)),

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
        'bowman': [2250, 5500, "MAX"],
        'crossbowman': [2000, 5000, "MAX"],
        'support_damage': [750, 1950, "MAX"],
        'support_range': [900, 2150, "MAX"],
        'magic_fire': [2750, 6500, "MAX"],
        'magic_ice': [2750, 6500, "MAX"],
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
