"""Module docstring"""
import unittest

TEXT = "La, la-la-la, la-la La-la-la, la-la-la The Kirin used to speak and sing We"
PATTERN = 'Kirin'
def rabin_karp(text, pattern):
    """Функция, реализующая метод Рабина-Карпа"""
    result = ([])
    pattern_sum, work_sum = (0,0)
    for i in range (0,len(pattern)):
        pattern_sum += ord(pattern[i])
    if len(text)<len(pattern):
        print ("!ALARM! Подстрока короче строки!")
    else:
        for i in range (0,len(pattern)):
            work_sum += ord(text[i])
        for i in range (0,len(text)-len(pattern)):
            if work_sum == pattern_sum:
                if text.startswith(pattern, i):
                    result.append(i)
            work_sum += (ord(text[i+len(pattern)]) - ord(text[i]))
            if i == (len(text)-len(pattern)-1):
                if pattern != "":
                    if text.startswith(pattern, i+1):
                        result.append(i+1)
    return result

print ("Подстрока", PATTERN, ";найдена начиная с:", rabin_karp(TEXT, PATTERN))

class RabinKarpTest(unittest.TestCase):
    """Тесты для метода Рабина-Карпа"""

    def setUp(self):
        """Инициализация"""
        self.text1 = 'axaxaxax'
        self.pattern1 = 'xax'
        self.text2 = 'bababab'
        self.pattern2 = 'bab'

    def test_return_type(self):
        """Проверка того, что функция возвращает список"""
        self.assertIsInstance(
            rabin_karp(self.text1, "x"), list,
            msg="Функция должна возвращать список"
        )

    def test_returns_empty(self):
        """Проверка того, что функция, когда следует, возвращает пустой список"""
        self.assertEqual(
            [], rabin_karp(self.text1, "z"),
            msg="Функция должна возвращать пустой список, если нет вхождений"
        )
        self.assertEqual(
            [], rabin_karp("", self.pattern1),
            msg="Функция должна возвращать пустой список, если текст пустой"
        )
        self.assertEqual(
            [], rabin_karp("", ""),
            msg="Фун-я должна возвращать пустой список, если текст пустой, даже if образец пуст"
        )

    def test_finds(self):
        """Проверка того, что функция ищет все вхождения непустых образцов"""
        self.assertEqual(
            [1, 3, 5], rabin_karp(self.text1, self.pattern1),
            msg="Функция должна искать все вхождения"
        )
        self.assertEqual(
            [0, 2, 4], rabin_karp(self.text2, self.pattern2),
            msg="Функция должна искать все вхождения"
        )

    def test_finds_all_empties(self):
        """Проверка того, что функция ищет все вхождения пустого образца"""
        self.assertEqual(
            list(range(len(self.text1))), rabin_karp(self.text1, ""),
            msg="Пустая строка должна находиться везде"
        )
# Запуск тестов
if __name__ == '__main__':
    unittest.main()
