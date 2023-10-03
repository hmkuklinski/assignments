#task 1: decomposing money
entry = int(input("Enter a number 1-9999: "))
while entry <1 or entry>9999:
    print("Invalid entry. Please enter a number within the range.")
    entry = int(input("Enter a number 1-9999"))
    
num_grands = int(entry/1000)
remain = entry % 1000
print(num_grands, " grands")

num_hundreds = int(remain/100)
remain %= 100
print(num_hundreds, " Benjamins")

num_tens = int(remain/10)
remain %= 10
print(num_tens, " sawbucks")

print(remain, " bucks")

    
#task 2: unscramble words
wordfile = open("words.txt","r")
word_list = [] #creates an empty list for our words

words = wordfile.readlines()  #reads and returns a list of lines from file

for word in words:
    word= word.lower() #ensures words are all lower case
    word = word.strip() #deletes the extra spaces before/after a word and the \n 
    word_list.append(word) #adds the word to the list

word_set = set(word_list) #set will delete any duplicates
word_list = word_set

#allows user to select a word
selected_word = input("Enter a word: ")
while len(selected_word) < 3: #invalid length 
    selected_word = input("Invalid word length. Please enter a new word: ")
    if len(selected_word)>3:
        break

if len(selected_word)>6: #makes alterations if the length is too long
    selected_word = selected_word[0:5]




