class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.area=width*height
r=Rectangle(5,10)
print("Area:",r.area)