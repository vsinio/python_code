class LittleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)

class SecClass(metaclass=LittleMeta):
    def __init__(self, first, second):
        self.first = first
        self.second = second



