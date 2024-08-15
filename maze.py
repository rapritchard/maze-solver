import time
import random
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._seed = random.seed() if seed is None else seed
    
    def _create_cells(self):
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append(Cell(self._win))
                
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = (i * self._cell_size_x) + self._x1
        y1 = (j * self._cell_size_y) + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Get left cell
            if (j - 1 >= 0 and self._cells[i][j - 1 ].visited is False):
                to_visit.append((i, j - 1))
            # Get right cell
            if (j + 1 < self._num_rows and self._cells[i][j + 1].visited is False):
                to_visit.append((i, j + 1))
            # Get top cell
            if (i - 1 >= 0 and self._cells[i - 1][j].visited is False):
                to_visit.append((i - 1, j))
            # Get bottom cell
            if (i + 1 < self._num_cols and self._cells[i + 1][j].visited is False):
                to_visit.append((i + 1, j))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                break
            rand_cell = random.choice(to_visit)
            i2, j2 = rand_cell
            # Is left cell
            if i2 < i:
                self._cells[i][j].has_left_wall = False
                self._cells[i2][j2].has_right_wall = False
            # Is right cell
            if i2 > i:
                self._cells[i][j].has_right_wall = False
                self._cells[i2][j2].has_left_wall = False
            # Is top cell
            if j2 < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i2][j2].has_bottom_wall = False
            # Is bottom cell
            if j2 > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i2][j2].has_top_wall = False
            self._break_walls_r(i2, j2)
                
    
    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self._num_cols - 1][self._num_rows - 1]

        entrance.has_top_wall = False
        self._draw_cell(0, 0)
        exit.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)