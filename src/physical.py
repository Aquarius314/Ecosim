
class Physical(object):

    __x_position = 0
    __y_position = 0
    __r = 0

    def __init__(self, x, y, r):
        self.__x_position = x
        self.__y_position = y
        self.__r = r
        return

    def get_x(self):
        return self.__x_position

    def get_y(self):
        return self.__y_position

    def get_r(self):
        return self.__r

    def move(self, x, y):
        self.__x_position += x
        self.__y_position += y
        return

    def move_to(self, x, y):
        self.__x_position = x
        self.__y_position = y
        return



# functionality: an abstract class for objects with x, y and r
