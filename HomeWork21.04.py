# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# Домашнє завдання
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5
from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(self, name: str, satiety: int = 50, energy: int = 50):
        self.name = name
        self.satiety = satiety
        self.energy = energy

    def sleep(self):
        self.energy = 100

    def eat(self, food_amount):
        self.satiety = min(100, self.satiety + food_amount)

    @abstractmethod
    def play(self, activity_level):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Pet):
    def play(self, activity_level):
        if self.satiety > 60:
            self.energy -= 2 * activity_level
            self.satiety -= activity_level

            self.energy = max(0, self.energy)
            self.satiety = max(0, self.satiety)

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self.energy > 30:
            if self.satiety > 40:
                print("Кіт грається з мишею")
            else:
                print("Кіт з'їв мишу")
        else:
            print("Кіт занадто втомлений")


class Dog(Pet):
    def play(self, activity_level):
        if self.satiety > 15:
            self.energy -= activity_level // 2
            self.satiety -= activity_level // 2

            self.energy = max(0, self.energy)
            self.satiety = max(0, self.satiety)

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self.satiety > 10:
            self.energy -= 5
            self.energy = max(0, self.energy)
        else:
            print("Собака занадто голодна")


cat = Cat("Куся")
dog = Dog("Тузя")

cat.make_sound()
dog.make_sound()

cat.eat(20)
dog.eat(10)

cat.play(5)
dog.play(6)

cat.catch_mouse()
dog.fetch_ball()

print(cat.satiety, cat.energy)
print(dog.satiety, dog.energy)