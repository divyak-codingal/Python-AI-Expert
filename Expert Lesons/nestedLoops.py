string = str (input ("Enter your word: "))
char = str (input("Enter the character: "))

i = 0
count = 0
while i < len(string):
    if (string[i]== char):
        count = count + 1
    i = i + 1
print ("Total number of times", char, " has occurred =", count)