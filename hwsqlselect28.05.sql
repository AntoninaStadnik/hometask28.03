-- SELECT *
-- FROM FRUITS
-- ■ Відображення усіх овочів з калорійністю, менше вказаної.
-- SELECT CALOPIES, COUNT(*)
-- FROM FRUITS 
-- GROUP BY CALOPIES

-- ■ Відображення усіх фруктів з калорійністю у вказаному
-- діапазоні.
-- SELECT CALOPIES
-- FROM FRUITS
-- WHERE CALOPIES BETWEEN 33 AND 69

-- ■ Відображення усіх овочів, у назві яких є вказане слово.
-- Наприклад, слово: капуста.
-- SELECT NAME, FRUIT_TYPE
-- FROM FRUITS
-- WHERE NAME ILIKE '%BERRY%'

-- ■ Відображення усіх овочів та фруктів, у короткому описі
-- яких є вказане слово. Наприклад, слово: гемоглобін.
-- SELECT NAME, FRUIT_DESCRIPTION
-- FROM FRUITS
-- WHERE FRUIT_DESCRIPTION ILIKE '%SWEET%'

-- ■ Показати усі овочі та фрукти жовтого або червоного
-- кольору
-- SELECT NAME, COLOR
-- FROM FRUITS
-- WHERE COLOR = 'Red' OR COLOR = 'Yellow'


-- ■ Показати кількість овочів.
-- SELECT COUNT(*)
-- FROM FRUITS
-- WHERE FRUIT_TYPE = 'Berry'

-- ■ Показати кількість фруктів.
-- SELECT COUNT(*)
-- FROM FRUITS
-- WHERE FRUIT_TYPE = 'Citrus'

-- ■ Показати кількість овочів та фруктів заданого кольору.
-- SELECT COUNT(*)
-- FROM FRUITS
-- WHERE COLOR = 'Red'

-- ■ Показати кількість овочів та фруктів кожного кольору.
-- SELECT COLOR, COUNT(*) AS COUNT_ITEMS
-- FROM FRUITS
-- GROUP BY COLOR

-- ■ Показати колір мінімальної кількості овочів та фруктів.


-- ■ Показати колір максимальної кількості овочів та фруктів.


-- ■ Показати мінімальну калорійність овочів та фруктів.
-- SELECT NAME, COUNT(*), MIN(CALOPIES)
-- FROM FRUITS
-- GROUP BY NAME

-- ■ Показати максимальну калорійність овочів та фруктів.
-- SELECT NAME, COUNT(*), MAX(CALOPIES) 
-- FROM FRUITS
-- GROUP BY NAME

-- ■ Показати середню калорійність овочів та фруктів.
-- SELECT NAME, COUNT(*), AVG(CALOPIES)
-- FROM FRUITS
-- GROUP BY NAME

-- ■ Показати фрукт з мінімальною калорійністю.
-- SELECT NAME, CALOPIES
-- FROM FRUITS
-- ORDER BY CALOPIES
-- LIMIT 1

-- ■ Показати фрукт з максимальною калорійністю.
-- SELECT NAME, CALOPIES
-- FROM FRUITS
-- ORDER BY CALOPIES DESC
-- LIMIT 1
