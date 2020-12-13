from flask import render_template

from config import setting_app

app = setting_app()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False,port=8086)
