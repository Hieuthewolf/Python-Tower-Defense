from constants import GameConstants, TowerConstants

def distance(a, b):
    """Returns the Euclidian distance between the two tuple coordinates."""
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

#Defining the Object class that we will be using for our path, for our mobs, obstacles, projectiles, towers
class GameObjects:
    def __init__(self, name, coord):
        self.name = name
        self.coord = coord

        #self.dimensions[0] = width; self.dimensions[1] = height
        if name in GameConstants.MONSTER_NAMES:
            self.dimensions = GameConstants.DIMENSIONS['monster'] #monsters
        elif name in TowerConstants.ATT_TOWER_NAMES:
            self.dimensions = GameConstants.DIMENSIONS['att_tower'] #attack tower
        elif name in TowerConstants.SUP_TOWER_NAMES:
            self.dimensions = GameConstants.DIMENSIONS['supp_tower'] #Support tower
        else:
            self.dimensions = GameConstants.DIMENSIONS['boss'] #bosses

    def does_collides(self, other_object):
        abs_xDist = abs(other_object.coord[0] - self.coord[0])
        abs_yDist = abs(other_object.coord[1] - self.coord[1])

        if other_object.name in TowerConstants.ATT_TOWER_NAMES or TowerConstants.SUP_TOWER_NAMES:
            space_requiredX = GameConstants.DIMENSIONS['supp_tower'][0] + 12
            if other_object.name in TowerConstants.ATT_TOWER_NAMES:
                space_requiredY = GameConstants.DIMENSIONS['supp_tower'][1] 
            else:
                space_requiredX = GameConstants.DIMENSIONS['att_tower'][1]
        else:
            space_requiredX = (other_object.dimensions[0] // 2) 
            space_requiredY = (other_object.dimensions[1] // 2) 
        
        return abs_xDist < space_requiredX and abs_yDist < space_requiredY


    def distance(self, other_object):
        return distance(self.coord, other_object.coord)

    

        

    



