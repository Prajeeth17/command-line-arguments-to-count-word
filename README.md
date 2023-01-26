# Command line arguments to count word
## AIM:
To write a python program for getting the word count from the contents of a file using command line arguments.

## EQUIPEMENT'S REQUIRED: 
PC
Anaconda - Python 3.7

## ALGORITHM: 

### Step 1:
Import sys
### Step 2: 
Open file using open()
### Step 3: 
Use for loop
### Step 4:  
Use len() to count number of words
### Step 5: 
Print the number of words
### Step 6: 
Give the command to display the number of words

## PROGRAM:
```python
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
```
### OUTPUT:
![](./cmd.png)

## RESULT:
Thus the program is written to find the word count from the contents of a file using command line arguments.