import json



def load_posts(filename):
    """
    Форматирование файла джейсон в список словарей
    """
    with open(filename, encoding='utf-8') as f:
        posts = json.load(f)
        return posts

