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

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
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

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        distance_field = [x[:] for x in [[self._grid_width * self._grid_height] * self._grid_width] * self._grid_height]
        boundary = poc_queue.Queue()
        if entity_type == HUMAN:
            entity_type = self._human_list
        elif entity_type == ZOMBIE:
            entity_type = self._zombie_list

        for entity in entity_type:
            boundary.enqueue(entity)
            visited.set_full(entity[0], entity[1])
            distance_field[entity[0]][entity[1]] = 0

        while boundary.__len__() > 0:
            current_cell = boundary.dequeue()
            neighbor_cells = self.four_neighbors(current_cell[0], current_cell[1])
            for nebor in neighbor_cells:
                if visited.is_empty(nebor[0], nebor[1]) and self.is_empty(nebor[0], nebor[1]):
                    visited.set_full(nebor[0], nebor[1])
                    boundary.enqueue(nebor)
                    distance_field[nebor[0]][nebor[1]] = distance_field[current_cell[0]][current_cell[1]] + 1

        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        new_human_list = []
        for human in self._human_list:
            neighbor_cells = self.eight_neighbors(human[0], human[1])
            neighbor_cells.append(human)
            max_distance = 1
            max_move = [human]
            for nebor in neighbor_cells:
                if zombie_distance_field[nebor[0]][nebor[1]] == self._grid_height * self._grid_width:
                    continue
                elif zombie_distance_field[nebor[0]][nebor[1]] == max_distance:
                    max_move.append(nebor)
                elif zombie_distance_field[nebor[0]][nebor[1]] > max_distance:
                    max_distance = zombie_distance_field[nebor[0]][nebor[1]]
                    max_move[:] = []
                    max_move.append(nebor)
            new_human_list.append(random.choice(max_move))
        self._human_list = new_human_list

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_zombie_list = []
        for zombie in self._zombie_list:
            neighbor_cells = self.four_neighbors(zombie[0], zombie[1])
            neighbor_cells.append(zombie)
            min_distance = (self._grid_height * self._grid_width) - 1
            min_move = [zombie]
            for nebor in neighbor_cells:
                if human_distance_field[nebor[0]][nebor[1]] == min_distance:
                    min_move.append(nebor)
                elif human_distance_field[nebor[0]][nebor[1]] < min_distance:
                    min_distance = human_distance_field[nebor[0]][nebor[1]]
                    min_move[:] = []
                    min_move.append(nebor)
            new_zombie_list.append(random.choice(min_move))
        self._zombie_list = new_zombie_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors


poc_zombie_gui.run_gui(Apocalypse(30, 40))
#CodeSkulptor: https://py2.codeskulptor.org/#user49_eDoLgY9LS6_13.py