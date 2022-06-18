"""
GUI for the Fifteen puzzle
"""

import simplegui

# constants
TILE_SIZE = 60


class FifteenGUI:
    """
    Main GUI class
    """

    def __init__(self, puzzle):
        """
        Create frame and timers, register event handlers
        """
        self._puzzle = puzzle
        self._puzzle_height = puzzle.get_height()
        self._puzzle_width = puzzle.get_width()

        self._frame = simplegui.create_frame("The Fifteen puzzle",
                                             self._puzzle_width * TILE_SIZE,
                                             self._puzzle_height * TILE_SIZE)
        self._solution = ""
        self._current_moves = ""
        self._frame.add_button("Solve", self.solve, 100)
        self._frame.add_input("Enter moves", self.enter_moves, 100)
        self._frame.add_button("Print moves", self.print_moves, 100)
        self._frame.set_draw_handler(self.draw)
        self._frame.set_keydown_handler(self.keydown)
        self._timer = simplegui.create_timer(250, self.tick)
        self._timer.start()
        self._frame.start()

    def tick(self):
        """
        Timer for incrementally displaying computed solution
        """
        if self._solution == "":
            return
        direction = self._solution[0]
        self._solution = self._solution[1:]
        try:
            self._puzzle.update_puzzle(direction)
        except:
            print "invalid move:", direction

    def solve(self):
        """
        Event handler to generate solution string for given configuration
        """
        new_puzzle = self._puzzle.clone()
        self._solution = new_puzzle.solve_puzzle()

    def print_moves(self):
        """
        Event handler to print and reset current move string
        """
        print self._current_moves
        self._current_moves = ""

    def enter_moves(self, txt):
        """
        Event handler to enter move string
        """
        self._solution = txt

    def keydown(self, key):
        """
        Keydown handler that allows updates of puzzle using arrow keys
        """
        if key == simplegui.KEY_MAP["up"]:
            try:
                self._puzzle.update_puzzle("u")
                self._current_moves += "u"
            except:
                print "invalid move: up"
        elif key == simplegui.KEY_MAP["down"]:
            try:
                self._puzzle.update_puzzle("d")
                self._current_moves += "d"
            except:
                print "invalid move: down"
        elif key == simplegui.KEY_MAP["left"]:
            try:
                self._puzzle.update_puzzle("l")
                self._current_moves += "l"
            except:
                print "invalid move: left"
        elif key == simplegui.KEY_MAP["right"]:
            try:
                self._puzzle.update_puzzle("r")
                self._current_moves += "r"
            except:
                print "invalid move: right"

    def draw(self, canvas):
        """
        Draw the puzzle
        """
        for row in range(self._puzzle_height):
            for col in range(self._puzzle_width):
                tile_num = self._puzzle.get_number(row, col)
                if tile_num == 0:
                    background = "rgb(128, 128, 255)"
                else:
                    background = "Blue"
                tile = [[col * TILE_SIZE, row * TILE_SIZE],
                        [(col + 1) * TILE_SIZE, row * TILE_SIZE],
                        [(col + 1) * TILE_SIZE, (row + 1) * TILE_SIZE],
                        [col * TILE_SIZE, (row + 1) * TILE_SIZE]]
                canvas.draw_polygon(tile, 1, "White", background)
                canvas.draw_text(str(tile_num),
                                 [(col + .2) * TILE_SIZE,
                                  (row + 0.8) * TILE_SIZE],
                                 2 *  TILE_SIZE // 3, "White")



