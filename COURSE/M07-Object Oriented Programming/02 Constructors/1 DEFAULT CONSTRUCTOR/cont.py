class sum:
    
    def __init__(self,num1,num2):  #constructor
        
        self.n1=num1
        self.n2=num2

    def ans(self):
        return self.n1+ self.n2
    

ob=sum(12,13)
print(ob.ans)