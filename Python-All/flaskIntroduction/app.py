from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)
db.app = app


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_one = db.Column(db.String(200), nullable=False)
    content_two = db.Column(db.String(200), nullable=False)
    # completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Słówko %r>" % self.id


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        # text_content_vocabulary = request.form['content_vocabulary']
        # text_content_translate = request.form['content_translate']
        new_text = Todo(
            content_one=request.form["content_one"],
            content_two=request.form["content_two"],
        )

        try:
            db.create_all()
            db.session.add(new_text)
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for("index"))
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
