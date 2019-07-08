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
    PATH = {
        'map_1': [
                    [(0, 531), (50, 531), (136, 518), (195, 496), (232, 424), (263, 349), (358, 312), (438, 285), (475, 217), (499, 133), (581, 101), (664, 101), (733, 94), (822, 83), (889, 72), (984, 80), (1075, 88), (1175, 94), (1235, 154), (1264, 228), (1184, 286), (1094, 310), (1035, 361), (1011, 435), (1065, 486), (1136, 507), (1219, 550), (1252, 639), (1260, 677)],
                 ],
        'map_2': [
                    [(350, 696), (336, 642), (288, 601), (229, 584), (182, 569), (140, 542), (116, 492), (108, 421), (139, 384), (182, 368), (241, 353), (281, 336), (324, 307), (345, 275), (362, 222), (373, 185), (386, 153), (449, 135), (506, 134), (551, 134), (598, 135), (655, 134), (699, 152), (732, 183), (750, 232), (752, 278), (754, 329), (757, 370), (760, 412), (772, 458), (793, 488), (837, 519), (901, 531), (953, 517), (983, 476), (997, 437), (997, 381), (997, 325), (997, 265), (997, 208), (997, 165), (997, 117), (997, 68), (997, 29)]
                    # [(336, DIMENSIONS['game'][1]), (336, 622), (253, 580), (159, 551), (110, 458), (168, 377), (272, 344), (341, 275), (375, 173), (475, 131), (592, 129), (709, 150), (760, 219), (768, 317), (773, 414), (830, 501), (941, 511), (993, 446), (997, 324), (1001, 222), (995, 135), (989, 50)]
                    # [(333, DIMENSIONS['game'][1]), (333, 625), (271, 588), (201, 570), (131, 532), (116, 451), (166, 377), (245, 350), (313, 320), (341, 248), (377, 176), (443, 136), (538, 133), (631, 134), (707, 147), (753, 198), (757, 253), (755, 317), (755, 384), (760, 441), (792, 488), (846, 518), (907, 521), (960, 492), (989, 448), (1000, 395), (1000, 301), (998, 244), (998, 185), (998, 138), (997, 93), (995, 21)]
                    # [(354, DIMENSIONS['game'][1]), (354, 657), (312, 598), (235, 578), (167, 557), (115, 503), (122, 419), (190, 371), (268, 348), (320, 316), (346, 279), (363, 201), (410, 150), (535, 121), (615, 131), (697, 140), (742, 183), (753, 280), (748, 352), (746, 405), (765, 469), (806, 499), (866, 520), (943, 520), (981, 486), (1004, 415), (1005, 350), (1001, 297), (997, 205), (996, 149), (995, 94), (996, 36)],
                    # [(344, DIMENSIONS['game'][1]), (344, 643), (303, 585), (183, 561), (122, 501), (146, 387), (241, 350), (328, 304), (361, 213), (427, 138), (549, 131), (672, 135), (746, 185), (750, 274), (751, 355), (754, 422), (784, 483), (843, 514), (935, 523), (987, 484), (1004, 418), (998, 341), (994, 266), (995, 195), (989, 125), (988, 68), (989, 18)],
                    # [(346, DIMENSIONS['game'][1]), (346, 654), (303, 597), (229, 577), (148, 549), (116, 468), (160, 378), (249, 350), (341, 305), (359, 214), (430, 137), (540, 125), (642, 126), (732, 166), (747, 255), (757, 353), (771, 445), (821, 513), (889, 531), (961, 521), (1003, 425), (997, 342), (994, 253), (994, 189), (996, 97), (997, 29)],
                    # [(346, DIMENSIONS['game'][1]), (346, 659), (313, 609), (254, 584), (196, 564), (145, 541), (118, 482), (126, 407), (176, 369), (254, 347), (313, 318), (337, 266), (360, 194), (399, 152), (463, 130), (534, 127), (592, 127), (666, 130), (724, 150), (748, 194), (758, 242), (754, 309), (755, 351), (757, 401), (763, 447), (778, 483), (819, 506), (875, 519), (912, 518), (955, 497), (982, 466), (996, 432), (1004, 370), (997, 311), (993, 255), (991, 203), (991, 179), (991, 126), (989, 79), (990, 36), (990, 15)],
                    # [(346, DIMENSIONS['game'][1]), (346, 659), (313, 609), (254, 584), (196, 564), (145, 541), (118, 482), (126, 407), (176, 369), (254, 347), (313, 318), (337, 266), (360, 194), (399, 152), (463, 130), (534, 127), (592, 127), (666, 130), (724, 150), (748, 194), (758, 242), (754, 309), (755, 351), (757, 401), (763, 447), (778, 483), (819, 506), (875, 519), (912, 518), (969, 518), (1035, 514), (1098, 515), (1163, 522), (1221, 518), (1272, 515), (1319, 520)]
                 ],
        'map_3': [],
        'map_4': []
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

    # Enemy waves are in the format of a wave #: (amount of monsters in each category, total_amount)
    # The tuple formed are formatted (monster 1, monster 2, monster 3, monster 4)
    ENEMY_WAVES_AMOUNT = {
        0: [1],
        # 0: [35, 25, 15, 10],
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
