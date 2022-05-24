"""
Interactive simulation for Monte Hall problem
"""

import random
import simplegui

# global constants
CANVAS_WIDTH = 540
CANVAS_HEIGHT = 180
CONTROL_WIDTH = 100
CENTER_VERT = 0.3
CENTER_HORIZ = 0.8

MIN_DOORS = 3
MAX_DOORS = 10

SELECT = 0
CHOOSE = 1
SHOW = 2


class MontyHallGUI:
    """
    Interactive demo for Monty Hall
    """
    
    def __init__(self):
        """
        Initialize the simulation
        """
        self._frame = simplegui.create_frame("Monty Hall problem", CANVAS_WIDTH, 
                                             CANVAS_HEIGHT, CONTROL_WIDTH)
        self._frame.set_canvas_background("White")
        self._frame.add_button("Clear", self.clear, CONTROL_WIDTH)
        self._frame.add_button("Add door", self.add_door, CONTROL_WIDTH)
        self._frame.set_mouseclick_handler(self.click)
        self._frame.add_label("")
        self._win_label = self._frame.add_label("Wins = 0")
        self._lose_label = self._frame.add_label("Loses = 0")
        self.clear()
        self._frame.set_draw_handler(self.draw)
        self._frame.start()
    
    def clear(self):
        """
        Clear the simulatin
        """
        self._game_state = SELECT
        self._wins = 0
        self._loses = 0
        self._num_doors = MIN_DOORS
        self._win_label.set_text("Wins = " + str(self._wins))
        self._lose_label.set_text("Loses = " + str(self._loses))
        self._prize_door = random.randrange(self._num_doors)
        
        
    def click(self, pos):
        """
        Convert a canvas click to a door number, reject invalid click when staying or switching
        """
        door_width = CANVAS_WIDTH / self._num_doors
        door_num = min(pos[0] / door_width, self._num_doors)
        if self._game_state == SELECT:
            self.process_door(door_num)
        elif self._game_state == CHOOSE:
            if door_num == self._selected_door or door_num == self._show_door:
                self.process_door(door_num)
        elif self._game_state == SHOW:
           self.process_door(door_num)
                
                
    def process_door(self, door_num):
        """
        Process a valid door number based on state
        """
        if self._game_state == SELECT:
            self._game_state = CHOOSE
            self._selected_door = door_num
            if door_num == self._prize_door:
                show_doors = range(self._num_doors)
                show_doors.remove(door_num)
                self._show_door = random.choice(show_doors)
            else:
                self._show_door = self._prize_door              
        elif self._game_state == CHOOSE:
            if door_num == self._prize_door:
                self._wins += 1
                self._win_label.set_text("Wins = " + str(self._wins))
            else:
                self._loses += 1   
                self._lose_label.set_text("Loses = " + str(self._loses))
            self._game_state = SHOW
        elif self._game_state == SHOW:
            self._prize_door = random.randrange(self._num_doors)
            self._game_state = SELECT
    
    def add_door(self):
        """
        Add a door to the simulation
        """
        self._num_doors = min(self._num_doors + 1, MAX_DOORS)
    
        
    def draw_door(self, canvas, door_pos, color):
        """
        Draw a single door with positin and color
        """
        door_width = CANVAS_WIDTH / self._num_doors
        canvas.draw_polygon([door_pos,
                             [door_pos[0] + door_width, door_pos[1]],
                             [door_pos[0] + door_width, door_pos[1] + CANVAS_HEIGHT],
                             [door_pos[0], door_pos[1] + CANVAS_HEIGHT]],
                             4, "Black", color)
        
    
    def draw(self, canvas):
        """
        Draw the doors
        """
        door_width = CANVAS_WIDTH / self._num_doors
        for door_num in range(self._num_doors):
            door_pos = [door_width * door_num, 0]
            if self._game_state == SELECT:
                self.draw_door(canvas, door_pos, "White")
            elif self._game_state == CHOOSE:
                if  door_num == self._selected_door:
                    self.draw_door(canvas, door_pos, "LightGreen")
                elif  door_num == self._show_door:
                    self.draw_door(canvas, door_pos, "LightGreen")
                else:
                    self.draw_door(canvas, door_pos, "LightGray")
            elif self._game_state == SHOW:
                if  door_num == self._prize_door:
                    self.draw_door(canvas, door_pos, "Gold")
                else:
                    self.draw_door(canvas, door_pos, "LightGray")

               

MontyHallGUI()       