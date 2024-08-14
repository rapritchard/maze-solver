from graphics import Window, Point, Line

def main():
    start_point = Point(10, 10)
    end_point = Point(50, 10)
    line = Line(start_point, end_point)
    win = Window(800, 600)
    win.draw_line(line)
    win.wait_for_close()
    
if __name__ == "__main__":
    main()