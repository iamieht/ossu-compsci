"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list) 
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def obstacles(self):
        """
        Generator that yields the obstacles in the order they were added.
        """
        for obstacle in self._obstacle_list:
            yield obstacle
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = poc_grid.Grid(self._grid_height, self._grid_width)

        distance_field = [[self._grid_height * self._grid_width
                           for dummy_col in range(self._grid_width)]
                          for dummy_row in range(self._grid_height)]

        for obstacle in self.obstacles():
            visited.set_full(obstacle[0], obstacle[1])

        boundary = poc_queue.Queue()
        list_type = self._zombie_list if entity_type == ZOMBIE else self._human_list

        for cells in list_type:
            boundary.enqueue(cells)
            visited.set_full(cells[0], cells[1])
            distance_field[cells[0]][cells[1]] = 0

        while boundary:
            current_cell = boundary.dequeue()
            neighbor_cells = visited.four_neighbors(
                current_cell[0], current_cell[1])

            for cell in neighbor_cells:
                if visited.is_empty(cell[0], cell[1]):
                    visited.set_full(cell[0], cell[1])
                    boundary.enqueue(cell)
                    distance_field[cell[0]][cell[1]
                                            ] = distance_field[current_cell[0]][current_cell[1]] + 1

        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        human_list = []

        for human in self._human_list:
            neighbors = self.eight_neighbors(human[0], human[1])
            neighbors.append(human)
            max_list = []

            for cell in neighbors:
                if self.is_empty(cell[0], cell[1]):
                    if len(max_list) == 0:
                        max_list.append(cell)
                    elif zombie_distance_field[cell[0]][cell[1]] == zombie_distance_field[max_list[0][0]][max_list[0][1]]:
                        max_list.append(cell)
                    elif zombie_distance_field[cell[0]][cell[1]] > zombie_distance_field[max_list[0][0]][max_list[0][1]]:
                        max_list = [cell]

            human_list.append(random.choice(max_list))

        self._human_list = human_list
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        pass

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))
