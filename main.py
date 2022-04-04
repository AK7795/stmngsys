from flask import Flask, render_template

ap = Flask(__name__)


@ap.route("/")
def hom():
    return render_template("slash.html")


@ap.route("/search")
def sea():
    return render_template("search.html")


@ap.route("/delete")
def delet():
    return render_template("deletee.html")


if __name__ == "__main__":
    ap.run()
