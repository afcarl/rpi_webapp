from flask import Blueprint, render_template

blueprint = Blueprint("data", __name__)

@blueprint.route("/")
def notes():
    return render_template("base.html")
