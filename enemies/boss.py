from .enemy import BossEnemy

# Creates instances of the different bosses (could all be compiled as one instance but separating them just in case
# one boss could have a different attribute from the rest)

class Mano(BossEnemy):
    def __init__(self, name, map_label):
        super().__init__(name, map_label)

class KingSlime(BossEnemy):
    def __init__(self, name, map_label):
        super().__init__(name, map_label)

class Balrog(BossEnemy):
    def __init__(self, name, map_label):
        super().__init__(name, map_label)

class Pianus(BossEnemy):
    def __init__(self, name, map_label):
        super().__init__(name, map_label)

class PinkBean(BossEnemy):
    def __init__(self, name, map_label):
        super().__init__(name, map_label)