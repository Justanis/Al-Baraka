with open("scores.txt","r") as file:
    lines=file.readlines()
    lines.sort(reverse=True)
with open("sorted.txt","w") as sorted_file :
    sorted_file.writelines(lines)    