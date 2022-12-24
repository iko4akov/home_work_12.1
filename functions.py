import json
from json import JSONDecodeError


def load_posts(filename):
    """
    Форматирование файла джейсон в список словарей
    """
    try:
        with open(filename, encoding='utf-8') as f:
            posts = json.load(f)
            return posts
    except FileNotFoundError:
        print("File отсутствует")
    except JSONDecodeError:
        print("Файл не удается преобразовать")


def add_post(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)
        return "posts.json перезаписан"

