with open("scores.txt", "r") as file:
    lines = file.readlines() \\lenth of liste
with open("parta.txt", "w") as part1:
    part1.writelines(lines[:5])
with open("partb.txt", "w") as part2:
    part2.writelines(lines[5:])
