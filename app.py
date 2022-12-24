from flask import Flask, request, render_template, send_from_directory

# импортируем функцию форматирования json файла в список словарей для дальнейшей работы
from functions import load_posts, add_post

# импортируем блюпринт главной страницы
from main.view import index_blueprint

# импортируем блюпринт для загрузки фото
from loader.view import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# регистрируем блюпринт главной сраницы
app.register_blueprint(index_blueprint)

# регистрируем блюпринт главной сраницы
app.register_blueprint(loader_blueprint)


# Создаем вьюшку
@app.route("/search")
def search_page():
    s = request.args['s']
    posts = load_posts(POST_PATH)
    return render_template('post_list.html', s=s, posts=posts)


@app.route("/post/upload", methods=["POST"])
def page_post_upload():
    """ Эта вьюшка обрабатывает форму, вытаскивает из запроса файл и показывает его имя"""
    #Создание нового словаря для пополнения файла с постами
    data = {}

    content = request.form.get('content')
    # Получаем объект картинки из формы
    picture = request.files.get("picture")
    # Получаем имя файла у загруженного фала
    name = picture.filename
    if content and picture:
        # Сохраняем картинку под родным именем в папку uploads
        picture.save(f"./{UPLOAD_FOLDER}/{name}")
        #Загрузка json файла для дальнейшей работы
        posts = load_posts(POST_PATH)
        # Заполняем словарь для дальнейшего добавления в общий список постов
        data['pic'] = f"./{UPLOAD_FOLDER}/{name}"
        data['contetnt'] = content
        #Добавление нового поста в общий список
        posts.append(data)
        #Перезаписывание файла json с новым постом
        add_post(POST_PATH, posts)
        return render_template('post_uploaded.html', name=name, content=content)
    elif not content and picture:
        return "Нет текста к посту"
    elif not picture and content:
        return "Необходимо загрузить фото к посту"
    else:
        return "Что- то не так с фото или текстом к посту"


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
