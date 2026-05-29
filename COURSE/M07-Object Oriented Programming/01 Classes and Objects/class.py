class Sum: 
    def __init__(self,num1,num2): #constructors
       self.num1=num1 
       self.num2=num2 

    def sum(self):
        print("SUM OF TWO NUMBERS IS:")

        return self.num1+self.num2

ob=Sum(12,13)
print(ob.sum())



