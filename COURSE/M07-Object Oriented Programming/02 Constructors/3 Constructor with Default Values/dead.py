class isdead:

    def __init__(self,name="happiness"): #default value
        self.name=name


        pass

    def ask(self):
        return f"{self.name} is dead"


ob1= isdead()
ob2= isdead("JULIUS CEASER")

print(ob1.ask())
print(ob2.ask())

