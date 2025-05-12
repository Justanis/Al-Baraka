with open ("name.txt","r") as file :
    for line in file :
        name,grade=line.strip().split(',')
        grade = float(grade)
        if grade >= 15 and grade <= 20  :
              with open("hight.txt", "a") as p1:
                 p1.write(line)
        elif grade >= 10 and grade <15  :
             with open("mid.txt", "a") as p2:
                 p2.write(line)
        else :
             with open("low.txt", "a") as p3:
                  p3.write(line)    