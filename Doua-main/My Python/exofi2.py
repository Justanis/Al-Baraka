with open ("std.txt","w") as file :
    for i in range(2):
        name = input(f"enter your name :\n").ljust (20)
        grade = input(f"enter your grade: \n").ljust (3)
        file.write(name+grade+"\n")

with open("std.txt","r") as file :
    content = file.read() 
    print("the info are : \n",content)       
