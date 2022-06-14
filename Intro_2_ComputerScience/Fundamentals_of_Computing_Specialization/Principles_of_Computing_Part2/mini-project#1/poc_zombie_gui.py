"""
Zombie Apocalypse mini-project
Click "Mouse click" button to toggle items added by mouse clicks
Zombies have four way movement, humans have eight way movement
"""

import simplegui

# Global constants
EMPTY = 0
FULL = 1
HAS_ZOMBIE = 2
HAS_HUMAN = 4
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7
CELL_COLORS = {EMPTY: "White",
               FULL: "Black",
               HAS_ZOMBIE: "Red",
               HAS_HUMAN: "Green",
               HAS_ZOMBIE|HAS_HUMAN: "Purple"}

NAME_MAP = {OBSTACLE: "obstacle",
            HUMAN: "human",
            ZOMBIE: "zombie"}

# GUI constants
CELL_SIZE = 10
LABEL_STRING = "Mouse click: Add "


class ApocalypseGUI:
    """
    Container for interactive content
    """

    def __init__(self, simulation):
        """
        Create frame and timers, register event handlers
        """
        self._simulation = simulation
        self._grid_height = self._simulation.get_grid_height()
        self._grid_width = self._simulation.get_grid_width()
        self._frame = simplegui.create_frame("Zombie Apocalypse simulation",
                                             self._grid_width * CELL_SIZE,
                                             self._grid_height * CELL_SIZE)
        self._frame.set_canvas_background("White")
        self._frame.add_button("Clear all", self.clear, 200)
        self._item_type = OBSTACLE

        label = LABEL_STRING + NAME_MAP[self._item_type]
        self._item_label = self._frame.add_button(label,
                                                  self.toggle_item, 200)
        self._frame.add_button("Humans flee", self.flee, 200)
        self._frame.add_button("Zombies stalk", self.stalk, 200)
        self._frame.set_mouseclick_handler(self.add_item)
        self._frame.set_draw_handler(self.draw)


    def start(self):
        """
        Start frame
        """
        self._frame.start()


    def clear(self):
        """
        Event handler for button that clears everything
        """
        self._simulation.clear()


    def flee(self):
        """
        Event handler for button that causes humans to flee zombies by one cell
        Diagonal movement allowed
        """
        zombie_distance = self._simulation.compute_distance_field(ZOMBIE)
        self._simulation.move_humans(zombie_distance)


    def stalk(self):
        """
        Event handler for button that causes zombies to stack humans by one cell
        Diagonal movement not allowed
        """
        human_distance = self._simulation.compute_distance_field(HUMAN)
        self._simulation.move_zombies(human_distance)


    def toggle_item(self):
        """
        Event handler to toggle between new obstacles, humans and zombies
        """
        if self._item_type == OBSTACLE:
            self._item_type = ZOMBIE
            self._item_label.set_text(LABEL_STRING + NAME_MAP[ZOMBIE])
        elif self._item_type == ZOMBIE:
            self._item_type = HUMAN
            self._item_label.set_text(LABEL_STRING + NAME_MAP[HUMAN])
        elif self._item_type == HUMAN:
            self._item_type = OBSTACLE
            self._item_label.set_text(LABEL_STRING + NAME_MAP[OBSTACLE])


    def add_item(self, click_position):
        """
        Event handler to add new obstacles, humans and zombies
        """
        row, col = self._simulation.get_index(click_position, CELL_SIZE)
        if self._item_type == OBSTACLE:
            if not self.is_occupied(row, col):
                self._simulation.set_full(row, col)
        elif self._item_type == ZOMBIE:
            if self._simulation.is_empty(row, col):
                self._simulation.add_zombie(row, col)
        elif self._item_type == HUMAN:
            if self._simulation.is_empty(row, col):
                self._simulation.add_human(row, col)


    def is_occupied(self, row, col):
        """
        Determines whether the given cell contains any humans or zombies
        """
        cell = (row, col)
        human = cell in self._simulation.humans()
        zombie = cell in self._simulation.zombies()
        return human or zombie


    def draw_cell(self, canvas, row, col, color="Cyan"):
        """
        Draw a cell in the grid
        """
        upper_left = [col * CELL_SIZE, row * CELL_SIZE]
        upper_right = [(col + 1) * CELL_SIZE, row * CELL_SIZE]
        lower_right = [(col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE]
        lower_left = [col * CELL_SIZE, (row + 1) * CELL_SIZE]
        canvas.draw_polygon([upper_left, upper_right,
                             lower_right, lower_left],
                            1, "Black", color)

    def draw_grid(self, canvas, grid):
        """
        Draw entire grid
        """
        for col in range(self._grid_width):
            for row in range(self._grid_height):
                status = grid[row][col]
                if status in CELL_COLORS:
                    color = CELL_COLORS[status]
                    if color != "White":
                        self.draw_cell(canvas, row, col, color)
                else:
                    if status == (FULL | HAS_HUMAN):
                        raise ValueError, "human moved onto an obstacle"
                    elif status == (FULL | HAS_ZOMBIE):
                        raise ValueError, "zombie moved onto an obstacle"
                    elif status == (FULL | HAS_HUMAN | HAS_ZOMBIE):
                        raise ValueError, "human and zombie moved onto an obstacle"
                    else:
                        raise ValueError, "invalid grid status: " + str(status)

    def draw(self, canvas):
        """
        Handler for drawing obstacle grid, human queue and zombie queue
        """
        grid = [[FULL] * self._grid_width for
                dummy_row in range(self._grid_height)]
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._simulation.is_empty(row, col):
                    grid[row][col] = EMPTY
        for row, col in self._simulation.humans():
            grid[row][col] |= HAS_HUMAN
        for row, col in self._simulation.zombies():
            grid[row][col] |= HAS_ZOMBIE
        self.draw_grid(canvas, grid)


# Start interactive simulation
def run_gui(sim):
    """
    Encapsulate frame
    """
    gui = ApocalypseGUI(sim)
    gui.start()
