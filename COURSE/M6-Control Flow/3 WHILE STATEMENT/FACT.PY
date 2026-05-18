f=1
num=int(input("enter number:"))
x=num
while(num!=0):
    f *=num
    num=num-1
    
print(f"factorial of {x} is ={f}")
