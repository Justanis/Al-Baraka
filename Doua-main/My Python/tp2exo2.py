file = open("scores.txt","w")
file.write("17\n")
file.write("03\n")
file.write("02\n")
file.write("05\n")
file.write("26\n")
file.write("28\n")
file.write("01\n")
file.write("0\n")

file.close
with open ("scores.txt","r") as file :
    line = file.readline()
    while line :
          print (line.strip())
          line = file.readline()
     