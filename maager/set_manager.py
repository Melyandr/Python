from maager.pen_manager import PenManager
from models.felttip_pen import FelttipPen
from models.marker_pen import MarkerPen
from models.officer_pen import OfficerPen
from models.school_pen import SchoolPen


class SetManager:

    def __len__(self):
        size = 0
        for obj in self.regular_manager:
            size += len(obj)
        return size
        # return len(self.general_list)

    def __iter__(self):
        for pen_obj in self.regular_manager:
            for pen_set in pen_obj:
                yield pen_set

    def __getitem__(self, pen_index):
        if pen_index < 0 or pen_index >= len(self):
            raise IndexError("index out of range")
        else:
            return self[pen_index]

    def __init__(self, regular_manager):
        self.regular_manager = regular_manager

        self.general_list = []
        for pen_obj in self.regular_manager:

            for words in pen_obj.people_who_use:
                self.general_list.append(words)

    def __next__(self):
        if self.general_list.index >= len(self.general_list):
            raise StopIteration
        item = self.general_list[self.index]
        self.general_list.index += 1
        return item


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
    marker_pen3 = MarkerPen("puma", "black", "cloth", 4, "for school", 10)

    pen_manager.add_pen(school_pen1)
    pen_manager.add_pen(felttip_pen1)
    pen_manager.add_pen(officer_pen1)
    pen_manager.add_pen(marker_pen1)
    pen_manager.add_pen(school_pen2)
    pen_manager.add_pen(felttip_pen2)
    pen_manager.add_pen(officer_pen2)
    pen_manager.add_pen(marker_pen2)

    set_manager = SetManager(pen_manager)
    print(set_manager.general_list)
    print(set_manager.__len__())
    print(len(set_manager))
    pen_manager.add_pen(marker_pen3)
    print(len(set_manager))