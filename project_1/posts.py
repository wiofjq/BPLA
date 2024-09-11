from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from database import login, reg

bp = Blueprint("posts", __name__)

# Команды для БПЛА
@bp.route("/management", methods=("GET", "POST"))
def management():
    if request.method == "POST":

        if "angle" in request.form:
            angle = request.form["angle"]
            current_app.logger.info(f'Задан angle: {angle}')

        elif "altitude" in request.form:
            altitude = request.form["altitude"]
            current_app.logger.info(f'Задан altitude: {altitude}')

        elif "forward" in request.form:
            forward = request.form["forward"]
            current_app.logger.info(f'Задан forward: {forward}')

        elif "back" in request.form:
            back = request.form["back"]
            current_app.logger.info(f'Задан back: {back}')
        else:
            current_app.logger.info(f'error')

    return render_template("posts/management.html")

# Создание нового поьзователя
@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Проверка введенных данных
        if password and username and reg(username, password):
            current_app.logger.info(f'New user create {username}')
            flash(f"Создан новый пользователь: {username}.", category="success")
        else:
            flash("Неправельные данные.", category="error")
    return render_template("posts/new_user.html")

# Авторизация пользователя
@bp.route("/", methods=("GET", "POST"))
def authorization():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Проверка введенных данных
        if password and username and login(username, password):
            current_app.logger.info(f'Authorization {username}')
            flash(f"Вы успешно авторизованы, {username}!", category="success")
            return redirect(url_for("posts.management"))
        else:
            flash("Ошибка доступа.", category="error")
    return render_template("posts/authorization.html")



@bp.route("/posts")
def posts():
    return render_template("posts/posts.html")
    # return render_template("posts/posts.html", posts=posts)
