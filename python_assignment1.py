#task 1: decomposing money
input = int(input("Enter a number 1-9999: "))
while input <1 or input>9999:
    print("Invalid entry. Please enter a number within the range.")
    input = int(input("Enter a number 1-9999"))
    
num_grands = int(input/1000)
remain = input % 1000
print(num_grands, " grands")

num_hundreds = int(remain/100)
remain %= 100
print(num_hundreds, " Benjamins")

num_tens = int(remain/10)
remain %= 10
print(num_tens, " sawbucks")

print(remain, " bucks")

    
#task 2: unscramble words
wordfile = open("words.txt")
words = wordfile.readlines() #reads the data from our file and stores them in a variable 
print(words[0:10]) #prints out the number of words in our list as specified by numbers afterwards
