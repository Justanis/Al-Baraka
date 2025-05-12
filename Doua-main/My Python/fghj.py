try :
   with open("nonexistent.txt","r") as file :
    print(file.read())
except   FileNotFoundError:
    print("file not found") 