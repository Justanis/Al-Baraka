def adding ():
    with open ("studeent.txt","a") as file :
        name = input(f"enter student name :\n")
        Id= input(f"enter student Id:\n")
        name = name[ :25].ljust(25,)
        Id = Id [ :15].ljust(15,)
        file.write(name+Id+"\n")
def search ():
    with open("studeent.txt","r") as file :
     for line in file :
        name = line[:25].strip()
        Id= line[25:].strip()
        if Id == seaarch:
           return name
    return None

while True :
    choice = int(input("enter choice 1 or 2 or 3 :"))
    if choice==1 :
        adding()
    elif choice==2 :
        seaarch=input("enter the id of student ")
        a=search()
        if a :
           print(f"the student with id {seaarch} is {a} ")
        else:
           print ("student not found")
    elif choice == 3 :
       break
       