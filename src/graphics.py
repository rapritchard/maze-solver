from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.start_point.x,
            self.start_point.y,
            self.end_point.x,
            self.end_point.y,
            fill=fill_color,
            width=2,
        )
