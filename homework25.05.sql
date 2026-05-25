-- Завдання 4
-- Створіть однотабличну базу даних «Овочі та фрукти»,
-- яка зберігатиме таку інформацію:
-- ■ Назва;
-- ■ Тип (овоч або фрукт);
-- ■ Колір;
-- ■ Калорійність;
-- ■ Короткий опис.

-- CREATE TABLE FRUITS(
-- 	ID SERIAL,
-- 	NAME VARCHAR(50),
-- 	FRUIT_TYPE VARCHAR(30),
-- 	COLOR VARCHAR(40),
-- 	CALOPIES INT,
-- 	FRUIT_DESCRIPTION VARCHAR(100)
-- )


-- INSERT INTO FRUITS (NAME, FRUIT_TYPE, COLOR, CALOPIES, FRUIT_DESCRIPTION) VALUES
-- ('Apple', 'Pome', 'Red', 52, 'Sweet and crunchy fruit'),
-- ('Banana', 'Berry', 'Yellow', 89, 'Soft and sweet tropical fruit'),
-- ('Orange', 'Citrus', 'Orange', 47, 'Juicy and tangy citrus fruit'),
-- ('Strawberry', 'Aggregate', 'Red', 33, 'Small and sweet red berries'),
-- ('Grape', 'Berry', 'Purple', 69, 'Sweet and juicy small fruit'),
-- ('Pineapple', 'Multiple', 'Brown and Yellow', 50, 'Tropical fruit with tough outer skin'),
-- ('Kiwi', 'Berry', 'Brown and Green', 61, 'Tangy fruit with fuzzy skin'),
-- ('Watermelon', 'Berry', 'Green and Red', 30, 'Large fruit with juicy red flesh'),
-- ('Mango', 'Drupe', 'Yellow and Red', 60, 'Sweet tropical stone fruit'),
-- ('Blueberry', 'Berry', 'Blue', 57, 'Small sweet blue fruit');

-- Завдання 5
-- Створіть наступні запити для таблиці з інформацією про
-- овочі та фрукти із попереднього завдання:

-- ■ Відображення всієї інформації з таблиці овочів та фруктів;
-- SELECT *
-- FROM FRUITS


-- ■ Відображення усіх овочів;
-- SELECT *
-- FROM FRUITS
-- WHERE FRUIT_TYPE = 'Berry'


-- ■ Відображення усіх фруктів;
-- SELECT *
-- FROM FRUITS
-- WHERE FRUIT_TYPE = 'Citrus'


-- ■ Відображення усіх назв овочів та фруктів;
-- SELECT NAME
-- FROM FRUITS;


-- ■ Відображення усіх кольорів. Кольори мають бути унікальними;
-- SELECT DISTINCT COLOR
-- FROM FRUITS;


-- ■ Відображення фруктів певного кольору;
-- SELECT *
-- FROM FRUITS
-- WHERE FRUIT_TYPE = 'Citrus' AND COLOR = 'Orange'


-- ■ Відображення овочів певного кольору;
-- SELECT *
-- FROM FRUITS
-- WHERE FRUIT_TYPE = 'VEGETABLE' AND COLOR = 'Green'
