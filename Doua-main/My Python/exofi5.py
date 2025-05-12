with open("name.txt","w") as file :
    for i in range (2) :
        name = input("enter student name : \n")
        grade = input("enter student grade : \n")
        file.write(name+ "," +grade+"\n")
with open("name.txt","r") as file :
    content=file.read()
    print ("the content of the file is :\n",content)
with open ("name.txt","r") as file :
    line = file.readline ()
    while line :
        print (line.strip())
        line=file.readline()



