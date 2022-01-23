import random
fruit_lists = ["Apple","Apricot","Avocado","Banana","Blackberry","Blueberry","Cherry","Coconut",
"Cucumber","Durian","Dragonfruit","Fig","Gooseberry","Grape","Guava","Jackfruit","Plum","Kiwifruit",
"Kumquat","Lemon","Lime","Mango","Watermelon","Mulberry","Orange","Papaya","Passionfruit","Peach",
"Pear","Persimmon","Pineapple","Pineberry","Quince","Raspberry","Soursop","Strawberry","Tamarind"]
chosenword = random.choice(fruit_lists)
wordlen = len(chosenword)
display = []
lives = 7
chosen_word = chosenword.lower()

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


print(logo)
print("Your job is to guess a fruit name.")
for i in range(wordlen):
    display += "_"
print(display)
b = "_"
while b in display:
    
    print(f"You have {lives} lives")
    
    guess = input("Guess an alphabet: ")
    for i in range(wordlen):
        if(chosen_word[i]==guess):
            display[i] = guess
    if guess not in display:
        lives -= 1
        print(stages[lives])
        if (lives==0):
            print("LIFE OVER\nYOU LOSE!")
            print(f"The given fruit is {chosen_word}")
            exit()
    print(display)

print(" ".join(display))
print("YOU WON")
