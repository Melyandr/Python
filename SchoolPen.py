
class SchoolPen:
    default_schoolpen = None
    CONST_ID="isn-101"

    def __init__(self, brand, colour, material,size,numPencils, numPens, numErasers):
        self.brand=brand
        self.colour=colour
        self.material=material
        self.size=size
        self.numPencils=numPencils
        self.numPens=numPens
        self.numErasers=numErasers

    @staticmethod
    def get_instance():
        if SchoolPen.default_schoolpen is None:
            SchoolPen.default_schoolpen = SchoolPen("default", "default", "default", 5, 10, 12, 2)
        return SchoolPen.default_schoolpen


    def add_pencil(self):
        self.numPencils+=1
        return self.numPencils

    def add_pen(self):
        self.numPens+=1
        return self.numPens

    def remove_pen(self):
        if self.numPens>0:
            self.numPens-=1
            return self.numPens
        else: return 0

    def remove_pencil(self):
        if self.numPencils>0:
            self.numPencils-=1
            return self.numPencils
        else: return 0


    def __str__(self):
     return f"Schoolpen({self.brand},{self.colour},{self.material},{self.size},{self.numPencils},{self.numPens},{self.numErasers},)"
