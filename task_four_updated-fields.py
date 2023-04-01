"""
Дан json файл. Найдите в нём все поля "updated" и поменяйте значение на текущие дату и время в формате ISO 8601.
"""

import json
import datetime

data = {}


def update_updated_fields(data):
    for key, item in data.items():
        if isinstance(item, dict):
            update_updated_fields(item)
        elif key == 'updated':
            data[key] = datetime.datetime.now().isoformat()


with open('file.json', 'r', encoding='UTF-8') as file:
    data.update(json.load(file))
    update_updated_fields(data)

with open('file.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
