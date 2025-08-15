from datetime import datetime
import csv

#1
file=open("notes.txt", "w")
file.write("hello world\n")
file.write("if guru is not, then who is the king then\n")
file.write("Boost is the secret of my energy.\nHe is the only boss\n")
file.close()

file=open("notes.txt", "r")
content = file.read()
#print(content)

file=open("notes1.txt", "a")
file.write(content)
file.close()

#2
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

#3
feedback = input("enter your feedback")
with open("log.txt", "a") as log:
    log.write(feedback + " @"  + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

print("your feedback work is done!!")

#4
file1=open("referenceLetter.txt", "w")
with open("E:Letter.txt", "r") as file:
    for line in file:
        file1.write(line)
        print(line.strip())
file1.close()

#5
with open("referenceLetter.txt", "r")  as file:
    while True:
        line = file.readline()
        if not line:
            break
        if "9686038349" in line:
            print(f"this word comes in line  {line.strip()}")


#6
with open("referenceLetter.txt", "r")  as file:
    for _ in range(10):
        print(file.readline().upper().strip())

#7
with open("E:Sreedhar Address route.txt", "r") as infile,  open("D:Sreedhar Address route.txt", "w") as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line)

#8
with open("industry.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Division"])

#9
with open("industry.csv", "r") as file:
    lines = file.readlines()
    for line in lines[1:]:
        columns = line.strip().split(",")
        print(columns[0])