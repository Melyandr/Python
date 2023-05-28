from functools import wraps

from models.felttip_pen import FelttipPen
from models.marker_pen import MarkerPen
from models.officer_pen import OfficerPen
from models.school_pen import SchoolPen
from pathlib import Path
from wrapt import decorator


def decorator_file_write(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("\n\n\n\n\n decorating")
        print(func.__name__)
        with open("../9laba.txt", "a") as file:
            file.write(f"{func.__name__}: ")
            for key, value in kwargs.items():
                file.write(str(key))
                file.write("=")
                file.write(str(value))
                file.write(", ")
            file.write("\n\n")

        return result

    return wrapper



def decorator_exception(func):
    counter = 0
    @wraps(func)
    def inner(self, pen_object):
        nonlocal counter
        if counter < 3:
            func(self, pen_object)
            counter += 1
        else:
            raise Exception("too many calls")

    return inner


class PenManager:
    """
     Manages a collection of pens.
    """

    pen_list = []

    def __len__(self):
        print("the length is ")
        return len(self.pen_list)

    def __getitem__(self, key):
        print("your object is  ")
        return self.pen_list[key]

    def __iter__(self):
        print("now we will iterated in list")
        return iter(self.pen_list)

    def add_pen(self, pen_object):
        """
        Adds a pen to the pen list.
        """
        self.pen_list.append(pen_object)

    def filtered_by_brand(self, pen_list):
        filtered_pen = (filter(lambda pen: pen.brand == "Kite", pen_list))
        for output_object in filtered_pen:
            print(output_object)

    def filtered_by_material(self, pen_list):
        filtered_pen = filter(lambda pen: pen.material == "cloth", pen_list)
        for object_output in filtered_pen:
            print(object_output)

    def output_price(self, pen_list):  # level 1
        print("method output_price works")
        list_price = [pens.calculate_price() for pens in pen_list]
        for i in list_price:
            print(i)
        return list_price

    def enumerate_object(self, pen_list):  # level 1
        enum_objects = enumerate(pen_list)
        print("method enumerate_object works ")
        for index, i in enum_objects:
            print(index, i.__class__.__name__)


    def zip_method_realization(self, pen_list):  # level 1
        print("method zip_method_realization works")
        price_list = self.output_price(pen_list)
        zip_objects = zip(pen_list, price_list)
        print(list(zip_objects))
        for price, i in zip_objects:
            print(f"{pen} {price} {price.__class__.__name__}")

    # def decorator_file_write(func):
    #     #     def inner(self, pen_object):
    #     #         file = open("C:\\python\\laba7\\9laba.txt", "w")
    #     #         result = func(pen_object)
    #     #         file.write(str(result))
    #     #         file.close()
    #     #         return result
    #     #
    #     #     return inner
    @decorator_file_write
    @decorator_exception
    def is_digit(self, pen_object):  # level 1
        print("method is_digit works")
        pen_with_attribute = pen_object.get_attributes_by_type(int)
        print("function any()")
        are_there_digits = [char.isdigit() for char in pen_with_attribute]
        print(any(are_there_digits))
        are_all_letters = [char.isalpha() for char in pen_with_attribute]
        print(all(are_all_letters))




if __name__ == "__main__":

    pen_manager = PenManager()

    school_pen1 = SchoolPen("nike", "white", "cloth", 3, 10, 12, 2)
    school_pen2 = SchoolPen("adidas", "brown", "cloth", 5, 5, 8, 4)

    felttip_pen1 = FelttipPen("Kite", "orange", "cotton", 5, "for school", 10)
    felttip_pen2 = FelttipPen("Kite", "grey", "cotton", 3, "for building", 16)
    officer_pen1 = OfficerPen("nike", "white", "tree", 7, 1, 2, 3)
    marker_pen1 = MarkerPen("puma", "black", "cloth", 4, "for school", 10)
    officer_pen2 = OfficerPen("champion", "white", "tree", 5, 1, 2, 3)
    marker_pen2 = MarkerPen("puma", "black", "cloth", 4, "for school", 10)

    # print(felttip_pen1.calculate_price())
    # print(school_pen1.calculate_price())
    # print(officer_pen1.calculate_price())
    # print(marker_pen1.calculate_price())

    pen_manager.add_pen(school_pen1)
    pen_manager.add_pen(felttip_pen1)
    pen_manager.add_pen(officer_pen1)
    pen_manager.add_pen(marker_pen1)
    pen_manager.add_pen(school_pen2)
    pen_manager.add_pen(felttip_pen2)
    pen_manager.add_pen(officer_pen2)
    pen_manager.add_pen(marker_pen2)

    print(len(pen_manager))  # first level
    print("\n")
    print(pen_manager[3])  # first level

    print("\n\n")
    for pen in pen_manager:  # first level
        print(pen)

    print("\n\n")
    pen_manager.output_price(pen_manager.pen_list)

    print("\n\n")
    pen_manager.enumerate_object(pen_manager.pen_list)

    print("\n\n")
    pen_manager.zip_method_realization(pen_manager.pen_list)

    print("\n\n get_attributes_by_type works")
    attribute = school_pen1.get_attributes_by_type(str)
    print(attribute)

    print("\n\n")

    pen_manager.is_digit(pen_object=school_pen1)  # level 3
    pen_manager.is_digit(school_pen2)
    pen_manager.is_digit(felttip_pen1)
    # pen_manager.is_digit(felttip_pen2)
    # if i add this object i will catch Exception(too many arguments)
    print("vebebebe")

    # pen_manager.get_brander(school_pen1)
