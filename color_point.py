from point import Point

class ColorPoint(Point):
    """
    Color point class inheriting from Point class
    """
    def __init__(self, x, y, color):
        # check if x and y are numbers
        if not isinstance(x, (int, float)):
            raise TypeError("x must be an number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be an number")
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        """
        Overwrite this method to return a string representation of the point
        :return: string representation of the point
        """
        return f"{self.color}: P<{self.x},{self.y}>"

if __name__ == "__main__": # guard against import runs
    p1 = ColorPoint(1, 2, "red")
    p2 = ColorPoint(3, 4, "green")
    p3 = ColorPoint(5, 6, "blue")
    p4 = ColorPoint(-2, -3, "yellow")
    color_points = [p1, p2, p3, p4]
    print(p1.color)
    print(p1)
    print(color_points)
    color_points.sort()
    print(color_points)
    # p5 = ColorPoint("bob", "james", "red")
    # print(p5)