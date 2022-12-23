# Импортируем класс блюпринт из фласк
from flask import Blueprint, render_template

# Создаем блюпринт и присваиваем ему имя
index_blueprint = Blueprint("index_blueprint", __name__)


# Создаем вьюшку
@index_blueprint.route("/")
def page_index():
    return render_template("/index.html")
