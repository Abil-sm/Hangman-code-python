import random
logo=''' _                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                 '''
stages=[ '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']
print("Let's play")
print(logo)
words=["aardvark","baboon","camel","dragon","lion","noodles","pizza","hangman","whale","animal","burger","tour","entertainment","television","news","comic","cartoon","food","human","humanity","earth","sun","space","year",'day','month',"football","basketball","rugby","badminton","sports"]
correct=random.choice(words)
display=("")
length=len(correct)
for letter in range(length):
    display+="_"
print(display)
game_over=False
correct_letters=[]
lifes=6
while not game_over:
    choice=input("Guess a letter").lower()
    placeholder=("")
    for letter in correct:
        if letter==choice:
            placeholder+=choice
            correct_letters.append(choice)
        elif letter in correct_letters:
            placeholder+=letter
        else:
            placeholder+="_"
    if choice not in correct:
        lifes-=1
    print(f"{placeholder}({lifes},6)")
    print(stages[lifes])
    if "_" not in placeholder:
        game_over=True
        input("You win!!!CONGRATULATIONS!!!!!")
    if lifes==0:
        game_over=True
        input(f"You ran out of lives,so you lose.Nice try.The correct answer was {correct}")


