class sum:
    num1=8

    def __init__(self,num2,num3):
        self.num2=num2
        self.num3=num3
        
    def sum_n(self):
        print(f"sum= {self.num2}+{self.num3}")
        
    
    @classmethod
    def sum_num(cls,user_name):
        print(f"user name = {user_name}")

        print(f"sum= {cls.num1}+{cls.num3}")