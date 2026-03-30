# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик
class Cart:
    def __init__(self,client,items):
        self.client=client
        self.items=items

    def add_new_item(self,item):
        self.items.append(item)
        print(f"{item} додано в кошик")

    def delete_item_from_cart(self,item):
        self.items.remove(item)
        print(f"{item} видалено з кошика")

    def show_info(self):
        print(f"{self.client}, ваш кошик наповнено такими товарами: {self.items}")

client1 = Cart("John",["pen", "pencil"])

client1.add_new_item("book")
client1.delete_item_from_cart("pen")
client1.show_info()


# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.

class Phone:
    def __init__(self,number,battery_level):
        self.number=number
        self.battery_level=battery_level

    def discharge(self, amount):
        self.battery_level -= amount

        if self.battery_level < 20:
            print("Заряд менше 20%, поставте тлф на зарядку!")


    def show_info(self):
        print(f"Для номеру {self.number}, заряд тлф складає {self.battery_level}%")


phone1 = Phone("45",100)
phone1.discharge(90)
phone1.show_info()



