from Pen import *

""""
FelttipPen is a child class from Pen. 
"""


class FelttipPen(Pen):
    price_of_felttip = 15
    """
           brand(str) it is the brand of Pen
           colour(str) it is the colout of Pem
           material(str) it is the material of Pen
           size(int) it is the size of Pen
           """

    def __init__(self, brand, colour, material, size, felttip, numbers_of_felttip):
        super().__init__(brand, colour, material, size)
        self.felttip = felttip
        self.numbers_of_felttip = numbers_of_felttip

    """
         Returns a string representation of the OfficerPen object.      
         """
    def __str__(self):
        return f"Felttip({self.brand},{self.colour},{self.material},{self.size},{self.felttip},{self.numbers_of_felttip})"

    """
                The method calculate_price calculates sum of Pen
               """
    def calculate_price(self):
        return self.numbers_of_felttip * self.price_of_felttip
