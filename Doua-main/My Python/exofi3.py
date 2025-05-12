def adding ():
    with open ("student.txt","a") as file :
        name = input(f"enter student name :\n")
        grade = input(f"enter student grade:\n")
        name = name[ :25].ljust(25,)
        grade = grade [ :3].ljust(3,)
        file.write(name+grade+"\n")
def display ():
    with open("student.txt","r")  as file :
        content = file.read()
        print(content) 

while True :
    choice = int(input("enter choice 1 or 2 or 3 :"))
    if choice==1 :
        adding()
    elif choice==2 :
        display()
        print("file content : \n")
    elif choice==3:
        break
