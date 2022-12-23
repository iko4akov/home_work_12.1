# Импортируем класс блюпринт из фласк
from flask import Blueprint, render_template

# Создаем блюпринт и присваиваем ему имя
loader_blueprint = Blueprint("loader_blueprint", __name__)


# Создаем вьюшку
@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_index():
    return render_template("post_form.html")