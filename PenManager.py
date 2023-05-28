from SchoolPen import *
from FelttipPen import *
from OfficerPen import *
from MarkerPen import *


class PenManager:
    """
        Manages a collection of pens.
        """
    pen_list = []

    def add_pen(self, pen):
        """
                Adds a pen to the pen list.
                """
        self.pen_list.append(pen)

    # def filtered_by_brand(self, list):
    #     list(filter(lambda pen: pen.brand == "Kite", list))
    #     for object_for_output in list:
    #         print(object_for_output)
    def filtered_by_brand(self, pen_list):
        filtered_pen = (filter(lambda pen: pen.brand == "Kite", pen_list))
        for object_for_output in filtered_pen:
            print(object_for_output)

    def filtered_by_material(self, pen_list):
        filtered_pen = filter(lambda pen: pen.material == "cloth", pen_list)
        for object_output in filtered_pen:
            print(object_output)


def main():
    """
       The main function that demonstrates the usage of pen objects and the pen manager.
       """
    pen_manager = PenManager()

    school_pen1 = SchoolPen("nike", "white", "cloth", 5, 10, 12, 2)
    school_pen2 = SchoolPen("adidas", "brown", "cloth", 5, 5, 8, 4)
    school_pen3 = SchoolPen.get_instance()
    felttip_pen1 = FelttipPen("Kite", "orange", "cotton", 3, "for school", 15)
    felttip_pen2 = FelttipPen("Kite", "grey", "cotton", 3, "for building", 15)
    officer_pen1 = OfficerPen("nike", "white", "tree", 5, 1, 2, 3)
    marker_pen1 = MarkerPen("puma", "black", "cloth", 4, "for school", 10)
    officer_pen2 = OfficerPen("champion", "white", "tree", 5, 1, 2, 3)
    marker_pen2 = MarkerPen("puma", "black", "cloth", 4, "for school", 10)

    print(felttip_pen1.calculate_price())
    print(school_pen1.calculate_price())
    print(officer_pen1.calculate_price())
    print(marker_pen1.calculate_price())

    pen_manager.add_pen(school_pen1)
    pen_manager.add_pen(felttip_pen1)
    pen_manager.add_pen(officer_pen1)
    pen_manager.add_pen(marker_pen1)
    pen_manager.add_pen(school_pen2)
    pen_manager.add_pen(felttip_pen2)
    pen_manager.add_pen(officer_pen2)
    pen_manager.add_pen(marker_pen2)

    school_pen1.add_pen()
    school_pen1.remove_pencil()

    for object_for_output in pen_manager.pen_list:
        print(object_for_output)

    print("\n\nlamda expression")
    # filtered_by_brand = list(filter(lambda pen: pen.brand == "Kite", pen_manager.pen_list))
    # for object_for_output in filtered_by_brand:
    #     print(object_for_output)
    pen_manager.filtered_by_brand(pen_manager.pen_list)
    print("\n\nsecond lambda expression, sorted by material")
    pen_manager.filtered_by_material(pen_manager.pen_list)
    # filtered_by_material = list(filter(lambda pen: pen.material == "cloth", pen_manager.pen_list))
    # for object_for_output in filtered_by_material:
    #     print(object_for_output)
    # #
    #
    #
    # for i in range(0,1000,5):
    #     array.append(i)
    #
    #
    #
    #
    # arr1 = [i for i in range(0,100,5)]
    #
    # arr2 = [i for i in range(101)]


# print(arr2[::5])
if __name__ == "__main__":
    main()
