# Програма складається з трьох потоків. Перший
# просить в користувача вводити числа, поки не введено
# порожній рядок, та зберігає числа в список.
# Інші два потоки чекають поки перший завершить
# роботу, і вже потім запускаються. Один рахує суму чисел в
# списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран

import threading



def ask_input(numbers):
    while True:
        number_input = input("Enter a number: ")
        if number_input == " ":
            break
        number_input = int(number_input)
        numbers.append(number_input)



def find_sum(numbers, result):
    print("Start finding sum")
    result["sum"] = sum(numbers)


def find_average(numbers, result):
    print("Start finding average")
    result["average"] = sum(numbers) / len(numbers)


numbers = []
result = {}

thread_ask = threading.Thread(
    target=ask_input,
    args=(
     numbers,
    ),
)

thread_sum = threading.Thread(
    target=find_sum,
    args=(
        numbers,
        result,
    ),
)
thread_average = threading.Thread(
    target=find_average,
    args=(
        numbers,
        result,
    ),
)

thread_ask.start()
thread_ask.join()

thread_sum.start()
thread_average.start()

thread_sum.join()
thread_average.join()

print(numbers)
print(result)

