from constants import GameConstants, EnemyConstants, TowerConstants
import math

#Defining the Object class that we will be using for our path, for our mobs, obstacles, projectiles, towers
class GameObjects:
    """
    Base structural class for our enemies and towers to keep track of dimensions and collisions
    @param (STR) name: name of object 
    @param (TUPLE) coord: (x, y) coordinates of object 
    """
    def __init__(self, name, coord):
        self.name = name
        self.coord = coord

        #self.dimensions[0] = width; self.dimensions[1] = height
        if name in EnemyConstants.MONSTER_NAMES:
            self.dimensions = GameConstants.DIMENSIONS['monster'] #monsters
        elif name in TowerConstants.ATT_TOWER_NAMES:
            self.dimensions = GameConstants.DIMENSIONS['att_tower'] #attack tower
        elif name in TowerConstants.SUP_TOWER_NAMES:
            self.dimensions = GameConstants.DIMENSIONS['supp_tower'] #Support tower
        elif name in TowerConstants.MAGIC_TOWER_NAMES:
            self.dimensions = GameConstants.DIMENSIONS['magic_tower']
        else:
            self.dimensions = GameConstants.DIMENSIONS['boss'] #bosses

        self.width, self.height = self.dimensions[0], self.dimensions[1]

    def does_collides(self, other_object):
        """
        Detects if one object collides with another (for now the radial distance is hardcoded as 90 --> good baseline)
        @param (OBJECT) other_object: the other object we're comparing with (i.e. tower, enemy)

        --> return: Bool
        """
        abs_xDist = abs(other_object.coord[0] - self.coord[0])
        abs_yDist = abs(other_object.coord[1] - self.coord[1])

        radial_dist = math.sqrt((abs_xDist ** 2) + (abs_yDist ** 2))

        if radial_dist < 90:
            return True
        return False

    

        

    



