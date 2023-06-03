
from models.pen import Pen


class OfficerPen(Pen):
    __PRICE_OF_MAP = 50
    __PRICE_OF_CURVIMETR = 35
    __PRICE_OF_COPYBOOK = 12
    people_who_use = {"scout", "contrscout"}

    def __init__(self, brand, colour, material, size, curvimetr, number_of_maps, number_of_copybooks):
        """
        brand(str) it is the brand of Pen
        colour(str) it is the colout of Pem
        material(str) it is the material of Pen
        size(int) it is the size of Pen
        curvimetr(int) it shows how many items(curvimetrs) are in Pen
        number_of_maps(int) it is a number, what shows how many maps are in Pen
        number_of_copybooks(int) it is a number, what shows how many copybooks are in Pen
        """
        super().__init__(brand, colour, material, size)
        self.curvimetr = curvimetr
        self.number_of_maps = number_of_maps
        self.number_of_copybooks = number_of_copybooks

    def calculate_price(self):
        """
        The method calculate_price calculates sum of Pen
        """
        return self.curvimetr * self.__PRICE_OF_CURVIMETR + self.number_of_maps * self.__PRICE_OF_MAP + self.number_of_copybooks * self.__PRICE_OF_COPYBOOK

    def __str__(self):
        """
        Returns a string representation of the OfficerPen object.
        """
        return f"OfficerPen({self.brand},{self.colour},{self.material},{self.size},{self.curvimetr},{self.number_of_maps},{self.number_of_copybooks})"

    def __repr__(self):
        return f"OfficerPen({self.brand},{self.colour},{self.material},{self.size}," \
               f"{self.curvimetr},{self.number_of_maps},{self.number_of_copybooks})"
