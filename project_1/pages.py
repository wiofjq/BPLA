from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)



@bp.route("/about")
def about():
    return render_template("pages/about.html")