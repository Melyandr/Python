from models.pen import *


class SchoolPen(Pen):
    __default_schoolpen = None
    __PRICE_OF_PEN = 10
    __PRICE_OF_PENCIL = 7
    __PRICE_OF_ERASIER = 4
    people_who_use = {"schooler", "teacher"}

    def __init__(self, brand, colour, material, size, num_pencils, num_pens, num_erasers):
        """
        brand (str): The brand of the pen.
        colour (str): The colour of the pen.
        material (str): The material of the pen.
        size (int): The size of the pen.
        num_pencils (int): The number of pencils.
        num_pens (int): The number of pens.
        num_erasers (int): The number of erasers.
        """
        super().__init__(brand, colour, material, size)
        self.num_pencils = num_pencils
        self.num_pens = num_pens
        self.num_erasers = num_erasers

    @staticmethod
    def get_instance():
        """
        Returns the default instance of the SchoolPen class.
         """
        if SchoolPen.__default_schoolpen is None:
            SchoolPen.__default_schoolpen = SchoolPen("default", "default", "default", 5, 10, 12, 2)
        return SchoolPen.__default_schoolpen

    def add_pencil(self):
        """
        Adds a pencil to the school pen.
        """
        self.num_pencils += 1
        return self.num_pencils

    def add_pen(self):
        """
        Adds a pen to the school pen.
        """
        self.num_pens += 1
        return self.num_pens

    def remove_pen(self):
        """
        Remove(take away one pen) a pen of the school pen.
        """
        if self.num_pens > 0:
            self.num_pens -= 1
            return self.num_pens
        else:
            return 0

    def remove_pencil(self):
        """
        Remove(take away one pencil) a pencil of the school pen.
        """
        if self.num_pencils > 0:
            self.num_pencils -= 1
            return self.num_pencils
        else:
            return 0

    def __str__(self):
        """
        Returns a string representation of the OfficerPen object.
        """
        return f"Schoolpen({self.brand},{self.colour},{self.material},{self.size},{self.num_pencils},{self.num_pens},{self.num_erasers})"

    def calculate_price(self):
        """
        The method calculate_price calculates a sum of Pen
        """
        return (
                self.num_pens * self.__PRICE_OF_PEN + self.num_pencils * self.__PRICE_OF_PENCIL + self.num_erasers * self.__PRICE_OF_ERASIER)

    def __repr__(self):
        return f"Schoolpen({self.brand},{self.colour},{self.material},{self.size},{self.num_pencils},{self.num_pens},{self.num_erasers})"
