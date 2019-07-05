from queue import PriorityQueue

class State(object):
    """
    Algorithm:
    --> 1) At the current position, generate list of all possible next steps towards the goal
    --> 2) Store the children in a PriorityQueue based on distances to the goal with the closest being first
    --> 3) Select the closest child and repeat this algorithm until goal is met or there is no more children

    @param val: value of the current child
    @param parent: parent of the child
    @param start: our start state which will be 0 by default
    @param goal: our end state which will be 0 by default
    """

    def __init__(self, val, parent, start = 0, goal = 0):
        self.children = [] # All neighboring possibilities
        self.parent = parent 
        self.val = val        
        self.dist = 0 

        if parent:
            self.start, self.goal = parent.start, parent.goal
            self.path = parent.path[:]
            self.path.append(val)

        else:
            self.start, self.goal = start, goal
            self.path = [val]

    def getDist(self):
        pass

    def createChildren(self):
        pass

class State_String(State):
    def __init__(self, val, parent, start = 0, goal = 0):
        super().__init__(val, parent, start, goal)
        self.dist = self.getDist()

    def getDist(self):
        """
        Gets the distance from our current state to the goal
        --> return: distance (int)
        """
        if self.val == self.goal:
            return 0

        dist = 0

        # The part of the algorithm where it changes from scenario to scenario
        for i, letter in enumerate(self.goal):
            # try:
            dist += abs(i - self.val.index(letter))
            # except:
                # dist += abs(i - self.val.find(letter))
            
        return dist

    def createChildren(self):
        """
        Creates children which in our case creates permutations of the letters and stores it in self.children
        --> return: None
        """
        if not self.children:
            for i in range(len(self.goal) - 1):
                val = self.val
                val = val[:i] + val[i+1] +val[i] + val[i+2:]
                self.children.append(State_String(val, self)) #State_String(val, self) = children

class AStar_Solve:
    def __init__(self, start, goal):
        self.path = []
        self.visited = []
        self.queue = PriorityQueue()
        self.start, self.goal = start, goal

    def solve(self):
        """
        Solves using the a-star algorithm
        --> return: None
        """

        start_state = State_String(self.start, 0, self.start, self.goal)
        counter = 0

        self.queue.put((0, counter, start_state))
        while (not self.path and self.queue.qsize()):
            closestChild = self.queue.get()[2]
            closestChild.createChildren()
            self.visited.append(closestChild.val)

            for child in closestChild.children:
                if child not in self.visited:
                    counter += 1
                    if not child.dist:
                        self.path = child.path
                        break
                
                    self.queue.put((child.dist, counter, child))

        if not self.path:
            print("No valid path")

        return self.path

if __name__ == "__main__":
    start1 = "edcba"
    goal1  = "abcde"

    a = AStar_Solve(start1, goal1)
    a.solve()

    for i in range(len(a.path)):
        print("{0}) {1}".format(i, a.path[i]))
        



        
