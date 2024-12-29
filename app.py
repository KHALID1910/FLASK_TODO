from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mytodo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db=SQLAlchemy(app)

class MyTodo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__ (self) -> str:
        return f"{self.sno} - {self.title}"

# todo = MyTodo(title="first", desc="my 1st todo")
#     db.session.add(todo)
#     db.session.commit()

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    # return "<p>Hello, World!</p>"
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo = MyTodo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo=MyTodo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route("/update")
def update():
    # return "<p>Hello, World!</p>"
    return render_template('index.html')

@app.route("/delete")
def delete():
    # return "<p>Hello, World!</p>"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port='8000')