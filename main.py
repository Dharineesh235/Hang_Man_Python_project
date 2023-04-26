import random
from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo

#choose a random word from imported word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#the game ends when "end_of_game" becomes True
end_of_game = False
#lets declare total avail chances
lives = 6

#The solution for reference
#If you want uncomment the below line
# print(f'Pssst, the solution is {chosen_word}.')

#Our project has desired logo. lets use the imported logo
print(logo)

#Declare an empty List and fill it with "_" as empty answer with random chosen word's length
display = []
for _ in range(word_length):
    display += "_"

#This loop will execute the necessary things of the game
while not end_of_game:
    #Lets get the guessed value of our user
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f'You already guessed the word "{guess}"')
    
    #lets check each letter of the chosen_word with the user_input
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    #lets decide, what if user loss?
    if guess not in chosen_word:
        print(f'You guessed "{guess}" but it is not in the word, you lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Print the clear output without , and ""
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])