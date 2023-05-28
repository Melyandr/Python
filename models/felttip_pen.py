from models.pen import Pen


class FelttipPen(Pen):
    """
    Felttip is a child class from Pen
    """
    people_who_use = {"builder", "office worker"}
    price_of_felttip = 22

    def __init__(self, brand, colour, material, size, felttip, numbers_of_felttip):
        """
        brand(str) it is the brand of Pen
        colour(str) it is the colout of Pem
        material(str) it is the material of Pen
        size(int) it is the size of Pen
        """
        super().__init__(brand, colour, material, size)
        self.felttip = felttip
        self.numbers_of_felttip = numbers_of_felttip

    def __str__(self):
        """
        Returns a string representation of the OfficerPen object.
        """

        return f"Felttip({self.brand},{self.colour},{self.material}," \
               f"{self.size},{self.felttip},{self.numbers_of_felttip})"

    def calculate_price(self):
        """
        The method calculate_price calculates sum of Pen
        """
        return self.numbers_of_felttip * self.price_of_felttip

    def __repr__(self):
        return f"Felttip({self.brand},{self.colour},{self.material}," \
               f"{self.size},{self.felttip},{self.numbers_of_felttip})"
