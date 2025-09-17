class Shape:
    def _init_(self,name= "Geric Shape"):
        self.name = name
        print("shape constructor called for : {self.name}")

        def calculate_area (self):
            print("Calculating area for generic shape(does nothing).")

class Rectangle(Shape):
    def _init_(self,length,width):
        super()._init_("Rectangle")
        self.length = lenghth
        self.wigth = width

    def calculate_area(self):
        super()._init_("Rectangle(from calculate_area)")
        area  = self.lenght * self.width
        print("Area of self.name")
        return area

    my_rectangle = (5,10)

