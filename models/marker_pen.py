from models.pen import Pen


class MarkerPen(Pen):
    PRICE_OF_MARKER = 22
    people_who_use = {"child from kindergarden", "child from primary school"}

    def __init__(self, brand, colour, material, size, type_of_marker, number_of_marker):
        """
        brand(str) it is the brand of Pen
        colour(str) it is the colout of Pem
        material(str) it is the material of Pen
        size(int) it is the size of Pen
        type_of_marker(str) it is type(where we can use it)
        number_of_marker(int) it is a number, what shows how many markers are in Pen
        """
        super().__init__(brand, colour, material, size)
        self.type_of_marker = type_of_marker
        self.number_of_marker = number_of_marker

    def calculate_price(self):
        """
        The method calculate_price calculate sum of Pen
        """
        return self.number_of_marker * self.PRICE_OF_MARKER

    def __str__(self):
        """
        Returns a string representation of the MarkerPen object.
        """
        return f"MarkerPen({self.brand},{self.colour},{self.material},{self.size},{self.type_of_marker},{self.number_of_marker})"

    def __repr__(self):
        return f"MarkerPen({self.brand},{self.colour},{self.material},{self.size},{self.type_of_marker},{self.number_of_marker})"

    def __iter__(self):
        return self.people_who_use