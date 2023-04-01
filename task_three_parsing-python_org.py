"""
Необходимо получить HTML-код страницы www.python.org, и посчитать сколько раз какие символы встречается в коде страницы.
Формат вывода определяете сами. Вывод программы разместите в файле readme.md.
"""

import requests
from bs4 import BeautifulSoup
import string


def symbol_count(link):
    """
    Я решила что подсчет комментариев HTML и других невидимых элементов может не иметь смысла для анализа, поэтому
    данный код использует filter() функцию для удаления всех непечатаемых символов из видимого текста,
    а string.printable определяет, какие символы можно печатать.
    """
    result = ''
    response = requests.get(link)
    html = response.text

    # Разбираем HTML-код с помощью BeautifulSoup и извлекаем видимый текст
    soup = BeautifulSoup(html, 'html.parser')
    visible_text = soup.get_text()

    # Удаляем все непечатаемые символы и преобразовать их в нижний регистр
    clean_text = ''.join(filter(lambda x: x in string.printable, visible_text))

    # Подсчет вхождений каждого символа
    char_counts = {}
    for char in clean_text:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char, count in char_counts.items():
        result += f"Character '{char}' occurs {count} times in the page code.\n"
    return result


symbol = symbol_count('https://www.python.org')
print(symbol)
