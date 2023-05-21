from Pen import *

""""
SchoolPen is a child class from Pen. 
"""


class SchoolPen(Pen):
    __default_schoolpen = None
    __PRICE_OF_PEN = 10
    __PRICE_OF_PENCIL = 7
    __PRICE_OF_ERASIER = 4
    """
               brand (str): The brand of the pen.
               colour (str): The colour of the pen.
               material (str): The material of the pen.
               size (int): The size of the pen.
               num_pencils (int): The number of pencils.
               num_pens (int): The number of pens.
               num_erasers (int): The number of erasers.
           """
    def __init__(self, brand, colour, material, size, num_pencils, num_pens, num_erasers):
        super().__init__(brand, colour, material, size)
        self.numPencils = num_pencils
        self.numPens = num_pens
        self.numErasers = num_erasers

    """
           Returns the default instance of the SchoolPen class.
           """
    @staticmethod
    def get_instance():
        if SchoolPen.__default_schoolpen is None:
            SchoolPen.__default_schoolpen = SchoolPen("default", "default", "default", 5, 10, 12, 2)
        return SchoolPen.__default_schoolpen

    """
            Adds a pencil to the school pen.
            """
    def add_pencil(self):
        self.numPencils += 1
        return self.numPencils

    """
               Adds a pen to the school pen.
               """
    def add_pen(self):
        self.numPens += 1
        return self.numPens

    """
                   Remove(take away one pen) a pen of the school pen.
                   """
    def remove_pen(self):
        if self.numPens > 0:
            self.numPens -= 1
            return self.numPens
        else:
            return 0

    """
                       Remove(take away one pencil) a pencil of the school pen.
                       """
    def remove_pencil(self):
        if self.numPencils > 0:
            self.numPencils -= 1
            return self.numPencils
        else:
            return 0

    """
             Returns a string representation of the OfficerPen object.      
             """
    def __str__(self):
        return f"Schoolpen({self.brand},{self.colour},{self.material},{self.size},{self.numPencils},{self.numPens},{self.numErasers})"

    """
             The method calculate_price calculates a sum of Pen
            """
    def calculate_price(self):

        return (
                self.numPens * self.__PRICE_OF_PEN + self.numPencils * self.__PRICE_OF_PENCIL + self.numErasers * self.__PRICE_OF_ERASIER)
