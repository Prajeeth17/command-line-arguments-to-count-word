#Program to count number of words in a text file using command-line arguments
#Developed by: Prajeeth K T
#Reg.No: 22002267
import sys
count=0
with open(sys.argv[1],'r') as f:
    for line in f:
        word = line.split()
        count+=len(word)
print("Word Count in File = ",count)