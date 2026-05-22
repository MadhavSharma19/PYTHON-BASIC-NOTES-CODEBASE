def details(brand,name,color="black"):
    return f"I want a {name} from {brand} which is {color} in color"

def details_after(brand,name,color="black"):
    return f"I have a {name} from {brand} which is {color} in color because of my dad 🥲"

b=input("enter brand :")
n=input("enter name  :")
print(details(b,n))
c=input("enter color :")
print(details_after(b,n,c))




