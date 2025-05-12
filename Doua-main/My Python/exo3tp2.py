with open("scores.txt","r") as file :
     lines = file.readlines()
     for line in lines [2:4]:
       print(line.strip())