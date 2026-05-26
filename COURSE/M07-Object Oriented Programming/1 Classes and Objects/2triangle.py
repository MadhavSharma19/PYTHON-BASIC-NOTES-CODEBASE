class triangle:
    def __init__(self,b,h):
        self.base=b
        self.height=h
        

    def area(self):
        self.ar=0.5*(self.base)*(self.height)
        print(self.ar)



x=int(input("enter base="))
y=int(input("enter height="))


ob=triangle(x,y)

print(ob.area())