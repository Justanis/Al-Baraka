with open("merged.txt","w") as outfile :
    for fname in ["scores.txt","scors.txt"]:
        with open(fname) as infile :
           outfile.write(infile.read())