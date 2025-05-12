def file() :
    with open("names.txt","w")as file :
        for i in range (6):
            name = input(f"enter your name: \n")
            file.write(name+"\n")

def display():
    with open("names.txt","r") as file :
        content=file.read()
        return content

def n_words():
    with open("names.txt","r") as file :
        content = file.read()
        word_content =len(content.split())
        return word_content  
    
def count_word(word_to_count) : 
    with open("names.txt","r") as file :
        content=file.read().lower()
        word_count=content.count(word_to_count.lower())
        return word_count
    
a=display()
print ("file content : \n",a )
b=n_words()
print ("nember of words in the file: ",b)
word_to_count=input("enter the name :")
d=count_word(word_to_count)
print(f"the word {word_to_count} appears {d} times in the file")

        