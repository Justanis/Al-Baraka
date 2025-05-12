with open("scores.txt", "r") as file:
   for line in file:
      if "17" in line:
        print(line.strip())