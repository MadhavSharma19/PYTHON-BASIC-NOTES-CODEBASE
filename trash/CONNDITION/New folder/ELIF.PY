#WAP to check temperature condition:

temp=int(input("enter temprature: ")) #0

if temp>40: #false 0not greater thn 40
    print("hot!🥵")

elif temp>=20 and temp<=40:
    print("warm!😥")


elif temp<20:
    print("cold!🥶")