# from path import Path
import os
import pygame

# def createPathLayout(path_corners):
#     """
#     Create a path object for every single point possible that is traversed along the path
#     this path object will contain a does_collide definition that will allow us to detect collisions
#     :param path_corners: contains all the corners in the path where there will be a change in direction
#     :return: the path layout
#     """
#     path = []

#     for i in range(len(path_corners)- 1):
#         delta_x = path_corners[i+1][0] - path_corners[i][0]
#         delta_y = path_corners[i+1][1] - path_corners[i][1]

#         #Traversing Up or down
#         if delta_x == 0:
#             direction = 1
#             if delta_y < 0:
#                 direction = - 1

#             for dist in range(abs(delta_y)):
#                 path.append(Path((path_corners[i][0], direction * dist + path_corners[i][1])))

#         #Traversing left or right
#         else:
#             direction = 1
#             if delta_x < 0:
#                 direction = -1

#             for dist in range(abs(delta_x)):
#                 path.append(Path((direction * dist + path_corners[i][0], path_corners[i][1])))

#     path.append(Path(path_corners[-1]))

#     return path

def import_images_numbers(img_directory, starting_bound, ending_bound, scaled_dim = None):
    """
    Returns all the sprite images as a list 
    :param img_directory: the path in the OS to get to the image --> ex: "images/towers/archer_towers/archer_1/"
    :param starting_bound: the starting bound for the first number associated with the image --> ex: 001 
    :param ending_bound: the ending bound for the last number associated with the image + 1 
    :param scaled_dim = a (width, height) tuple to indicate desired scaled dimensions --> ex: (64, 64)

    :return: image list
    """
    images = []

    for i in range(starting_bound, ending_bound):
        img = pygame.image.load(os.path.join(img_directory + str(i) + ".png"))
        if scaled_dim:
            images.append(pygame.transform.scale(img, scaled_dim))
        else:
            images.append(img)

    return images

def import_images_name(img_directory, name_trail, starting_bound, ending_bound, scaled_dim = None):
    """
    Returns all the sprite images as a list 
    :param img_directory: the path in the OS to get to the image --> ex: "images/towers/archer_towers/archer_1/"
    :param name_trail: for enemies to indicate what the enemy is 
    :param starting_bound: the starting bound for the first number associated with the image --> ex: 001 
    :param ending_bound: the ending bound for the last number associated with the image + 1 
    :param scaled_dim = a (width, height) tuple to indicate desired scaled dimensions --> ex: (64, 64)

    :return: image list
    """
    images = []

    for i in range(starting_bound, ending_bound):
        num_string = str(i)
        if i < 10:
            num_string = "0" + num_string

        img = pygame.image.load(os.path.join(img_directory, name_trail + num_string + ".png"))

        if scaled_dim:
            images.append(pygame.transform.scale(img, scaled_dim))
        else:
            images.append(img)

    return images




