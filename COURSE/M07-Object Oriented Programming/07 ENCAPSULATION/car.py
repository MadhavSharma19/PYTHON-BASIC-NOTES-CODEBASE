class car:
    def __init__(self):
        self._carkey="yes"
       

class padosi(car):
    def permission(self):
        print(f"car ki chabi milegi? = {self._carkey}")

        

ob=padosi()

print(ob.permission())
