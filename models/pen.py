from abc import ABC, abstractmethod

from wrapt import decorator


class Pen(ABC):
    people_who_use = set()

    def __len__(self):
        return len(self.people_who_use)

    def __init__(self, brand, colour, material, size):
        """
        brand(str) it is the brand of Pen
        colour(str) it is the colout of Pem
        material(str) it is the material of Pen
        size(int) it is the size of Pen
        """
        self.brand = brand
        self.colour = colour
        self.material = material
        self.size = size

    @abstractmethod
    def calculate_price(self):
        """
        it will calculate total price
        """
        pass

    def get_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    @abstractmethod
    def people_who_use(self):
        pass

