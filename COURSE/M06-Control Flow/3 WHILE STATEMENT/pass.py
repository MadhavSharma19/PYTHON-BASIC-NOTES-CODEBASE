i_pass= 1313
u_pass=int(input("enter password: "))

while(i_pass!=u_pass):
    print("invalid password! try again")
    u_pass=int(input("re-enter password:"))
    
    if(i_pass==u_pass):
        break



if(i_pass==u_pass):
    print("WELCOME SIR JI!")
