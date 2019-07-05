# from path import Path
import os
import pygame
import math

def calculate_distance(point_A, point_B):
    """
    Calculates the distance from point A to point B with class properties kept in mind
    In the case of one point being an object and another a coordinate tuple --> point_A will always be the object
    @param point_A: either a tower object or a coordinate tuple 
    @param point_B: either a tower object or a coordinate tuple

    --> return: distance (not Euclidean) between the two points
    """
    # Both points are tower or enemy objects
    if not isinstance(point_A, tuple) and not isinstance(point_B, tuple):
        return math.sqrt((point_A.x - point_B.x) ** 2 + (point_A.y - point_B.y) ** 2)
    
    # One point is a tower or enemy object and the other point is a tuple
    elif not isinstance(point_A, tuple) and isinstance(point_B, tuple):
        return math.sqrt((point_A.x - point_B[0]) ** 2 + (point_A.y - point_B[1]) ** 2)

    # Both points are tuples
    else:
        return math.sqrt((point_A[0] - point_B[0]) ** 2 + (point_A[1] - point_B[1]) ** 2)

def import_images_numbers(img_directory, starting_bound, ending_bound, scaled_dim = None):
    """
    Returns all the sprite images as a list 
    @param img_directory: the path in the OS to get to the image --> ex: "images/towers/archer_towers/archer_1/"
    @param starting_bound: the starting bound for the first number associated with the image --> ex: 001 
    @param ending_bound: the ending bound for the last number associated with the image + 1 
    @param scaled_dim = a (width, height) tuple to indicate desired scaled dimensions --> ex: (64, 64)

    --> return: image list
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
    @param img_directory: the path in the OS to get to the image --> ex: "images/towers/archer_towers/archer_1/"
    @param name_trail: for enemies to indicate what the enemy is 
    @param starting_bound: the starting bound for the first number associated with the image --> ex: 001 
    @param ending_bound: the ending bound for the last number associated with the image + 1 
    @param scaled_dim = a (width, height) tuple to indicate desired scaled dimensions --> ex: (64, 64)

    --> return: image list
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




