class isdead:

    def __init__(self,name):
        self.name=name


        pass

    def ask(self):
        return f"{self.name} is dead"

ob= isdead("JULIUS CEASER")
print(ob.ask())

