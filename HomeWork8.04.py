# Створіть клас Recipe з атрибутами
#  name – назва страви
#  ingredients – список продуктів
#  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item) – перевіряє чи є інгредієнт в
# рецепті
#  __gt__(self, other) – перевіряє чи є час приготування self
# більшим за other
#  display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список.
# Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом
# приготування, скористайтесь функцією min
# Приклад
# рецептів:
# Recipe("Піца",
# ["борошно", "вода", "дріжджі", "томат", "сир"],
# "Готуємо тісто, додаємо інгредієнти та запікаємо",
# 30)
#
# Recipe("Салат",
#        ["томат", "огірок", "зелень", "олія"],
#        "Нарізаємо овочі, додаємо зелень та поливаємо
# олією",10)
#
# Recipe("Суп",
#        ["вода", "картопля", "морква", "м'ясо"],
#        "Варимо всі інгредієнти до готовності", 45)
class Recipe:
    def __init__(self, name:str, ingredients:list, text:str, time:float):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.time = time

    def __str__(self):
        return self.name

    def __contains__(self, item):
        return item in self.ingredients

    def __gt__(self, other):
        return self.time > other.time

    def display_info(self):
        print(self.name)
        print(self.ingredients)
        print(self.text)
        print(self.time)


dish1 = Recipe("Піца",
["борошно", "вода", "дріжджі", "томат", "сир"],
"Готуємо тісто, додаємо інгредієнти та запікаємо",30)

dish2 = Recipe("Салат",
["томат", "огірок", "зелень", "олія"],
"Нарізаємо овочі, додаємо зелень та поливаємо олією",10)

dish3 = Recipe("Суп",
["вода", "картопля", "морква", "м'ясо"],
"Варимо всі інгредієнти до готовності", 45)

dishes = [dish1, dish2, dish3]

for dish in dishes:
    if "томат" in dish:
     print(dish)

fastest_recipt = min(dishes, key=lambda x: x.time)

fastest_recipt.display_info()



