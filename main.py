import random

"""
The Game of Divination é um minigame de advinhar um número entre 1 e 100. Você escolhe entre três opções de dificuldade e todas elas começam com 100 pontos.
Porém, o número de tentativas são diferentes. Existe uma lógica implementada na pontuação para te ajudar a obter esse número. Guess the number!
"""

print("Welcome to the Game of Divination")

SECRET_NUMBER = random.randint(1, 101)

print("Choice which difficulty you want to play.")


def choiceLevel(level):
    if level == 1:
        print("You have chosen Easy difficulty.")
        print("You have 5 shots to guess the number.")
        print("You have 100 points. Good luck!")
        total_shots = 5
        points = 100
    elif level == 2:
        print("You have chosen Medium difficulty.")
        print("You have 3 shots to guess the number.")
        print("You have 100 points. Good luck!")
        total_shots = 3
        points = 100
    elif level == 3:
        print("You have chosen Hard difficulty.")
        print("You have 2 shots to guess the number.")
        print("You have 100 points. Good luck!")
        total_shots = 2
        points = 100
    else:
        print("You have chosen wrong number.")
        total_shots = 0
        points = 0
           
    return total_shots, points


while True:
    level = int(input("(1) Easy. (2) Medium (3) Hard. ?: "))
    total_shots, points = choiceLevel(level)
    if total_shots > 0:
        break
    
for rodada in range(0, total_shots + 1):
    print(f"You have {total_shots - rodada} shots left. The number must be between 1 and 100.")
    guess = int(input("Guess the number: "))
    print(f"You said {guess}")
    
    success = guess == SECRET_NUMBER
    more_than = guess > SECRET_NUMBER
    less_than = guess < SECRET_NUMBER
    
    if guess < 1 or guess > 100:
        print("The number must be between 1 and 100.")
        continue
    
    if success:
        print(f"Congratulations! You guessed the number {SECRET_NUMBER} in {rodada} shot(s).")
        points = points + 100
        print(f"You got {points} points.")
        break
    elif total_shots < rodada+2:
        print(f"You lost! The number was {SECRET_NUMBER}.")
        print(f"You got {points} points. Game Over.")
        break
    else:
        if more_than:
            print("The number is less than your guess.")
        elif less_than:
            print("The number is greater than your guess.")
            
        lost_points = abs(SECRET_NUMBER - guess)
        points = points - lost_points
        if points == 0:
            print(f"You have {points} points. Game Over")
            break
        
        print(f"You have {points} points.")
        
    