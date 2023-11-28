import random as rd 

questions = { "structure_donnee" : {"dict" : "{:,}" , "list" : "[,]" , "tuple" : "{}" }  , "structure_controle" : { "if":"if" , "while":"while" , "for":"for" , "def":"def" } }

general_input = ""
while general_input != "stop" : 
    general_input = input("choisissez un jeux parmis ... : " )
    if general_input == "Python" :
        usr_inp = "" 

        points = 0 
        correct = False
        while usr_inp != "stop" : 
            correct = False
            q_type = rd.sample(sorted(questions), 1 ) 
            q = rd.sample(sorted(questions[q_type[0]]), 1 ) 
            sol  = questions[q_type[0]][q[0]]

            usr_inp = input("nombre de points :" + str(points) + "\n"   + q[0] + " : "  ) 

            if usr_inp == sol : 
             correct = True
             points += 1 

            print(str(correct) + " la bonne sollution est : "+  sol)


#Hangman game 

def possible_words():
    words = ["string", "tuple", "boolean", "float", "bytes", "while", "variable", "loop"]
    return rd.choice(words)

def game():
    print("==========================================================")
    print("Welcome to the HANGMAN GAME python-themed!")
    print("==========================================================")
   

    chosen_word = possible_words()
    letters_word = len(chosen_word)
    guess_word = ["_"] * letters_word
    wrong_letters = []
    lives = 5
    
    while "_" in guess_word and lives > 0:
        print("\nWord To Guess:", " ".join(guess_word))
        print("\nWrong Letters:", " ".join(wrong_letters))
        print(f"\nRemaining lives: {'❤️ ' * lives}\n")

        choice = input("Choose 'l' to guess a letter or 'w' to guess the word: ").lower()

        if choice == 'l':
            usr_letter = input("\nTry a letter: ").lower()
            if usr_letter in wrong_letters or usr_letter in guess_word:
                print("Letter already tested, try another one!")
            elif usr_letter in chosen_word:
                for i in range(letters_word):
                    if chosen_word[i] == usr_letter:
                        guess_word[i] = usr_letter
                if "_" not in guess_word:
                    print("\nCongratulations, you guessed the word!!! You won the game!!!\U0001F600")
            else:
                wrong_letters.append(usr_letter)
                lives -= 1
                if lives == 0:
                    print(f"\nYou have no more lives... you lost \U0001F612. The word was: {chosen_word}")

        
        elif choice == 'w':
            usr_word = input("\nTry to guess the word: ").lower()
            if usr_word == chosen_word:
                print("\nCongratulations, you guessed the word!!! You won the game!!!\U0001F600")
                break
            else:
                if lives > 0:
                    lives -= 1
                    print("\nThe word is not the correct one, you lost one life... ")
                else:
                    print(f"\nYou have no more lives... you lost \U0001F612. The word was: {chosen_word}")
        print("==========================================================")
       

if general_input == "Hangman game":
    game()





