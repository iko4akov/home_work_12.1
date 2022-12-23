from flask import Flask, request, render_template, send_from_directory

from functions import load_posts
# импортируем блюпринт главной страницы
from main.view import index_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# регистрируем блюпринт главной сраницы
app.register_blueprint(index_blueprint)


# Создаем вьюшку
@app.route("/search")
def search_page():
    s = request.args['s']
    posts = load_posts(POST_PATH)
    return render_template('post_list.html', s=s, posts=posts)


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
