# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями

import random
import json


def load_data(filename="game.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data["wins"], data["loses"]
    except FileNotFoundError:
        return 0, 0


def save_data(wins, loses, filename="game.json"):
    data = {
        "wins": wins,
        "loses": loses
    }
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def start_new_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I guessed a number from 1 to 100")

    while True:
        user_number = int(input("Enter your number: "))
        attempts += 1

        if user_number > secret_number:
            print("Too big")
        elif user_number < secret_number:
            print("Too small")
        else:
            print(f"You guessed in {attempts} attempts!")

            if attempts <= 5:
                print("You WIN")
                return True
            else:
                print("You LOSE")
                return False


def show_result(wins, loses):
    print(f"Wins: {wins}")
    print(f"Loses: {loses}")


wins, loses = load_data()

result = start_new_game()

if result:
    wins += 1
else:
    loses += 1

save_data(wins, loses)

show_result(wins, loses)




