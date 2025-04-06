#                                                          NUMBER GUESSING GAME 
#--------------------------------------------------------------------------------------------------------------------------------------#
logo = [
    '''

  ________                              ___________.__              _______               ___.                  
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________  
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ 
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|    
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/        

'''
]
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game(lives):
    import random
    answer = random.randint(1,101)
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess a number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            return answer
        elif guess > answer or guess < answer:
            if lives == 1:
                print("You have run out of guesses. Refresh the page to run again.")
                return None
            if guess>answer: 
                print("Too high")
            else:
                print("Too Low")
            print("Guess again")
        lives -= 1 

if difficulty == "easy":
    total_lives = 10
elif difficulty == "hard":
    total_lives = 5
else:
    print("Invalid Input!")

game(total_lives)
#--------------------------------------------------------------------------------------------------------------------------------------#
