from abc import ABC, abstractmethod

"""
class Pen is a father class what has 4 descendant. Pen has one abstract method.
"""


class Pen(ABC):
    """
          brand(str) it is the brand of Pen
          colour(str) it is the colout of Pem
          material(str) it is the material of Pen
          size(int) it is the size of Pen
          """
    def __init__(self, brand, colour, material, size):
        self.brand = brand
        self.colour = colour
        self.material = material
        self.size = size

    """
     it will calculate total price
     """
    @abstractmethod
    def calculate_price(self):
        pass
