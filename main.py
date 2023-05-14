import SchoolPen
from SchoolPen import *
def main():

    school_pen1=SchoolPen("nike", "white","tree",5,10,12,2)
    school_pen2=SchoolPen("adidas", "brown","tree",5,5,8,4)
    school_pen3=SchoolPen.get_instance()

    list=[]
    list.append(school_pen1)
    list.append(school_pen2)
    list.append(school_pen3)
    school_pen1.add_pen()
    school_pen1.remove_pencil()
    for object in list:
        print(object)

if __name__ == "__main__":
    main()
