with open ("compute.txt","r") as file :   
    content= file.read()
    n_w=len(content.strip())
    print(n_w)

with open ("output.txt","w") as outfile :
    with open ("copute.txt","r") as file :
        content=file.read()
        words = content.split()
        s=int(n_w /2)
        for word in words [s:] :
            outfile.write(word+ "\n")