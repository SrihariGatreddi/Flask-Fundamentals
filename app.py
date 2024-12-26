from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to avoid unnecessary warnings

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route("/")
def hello_world():
    todo =Todo(title="First Todo", desc="Start Investing in Stocks")
    db.session.add(todo)
    db.session.commit()
    allTodo=Todo.query.all()
    return render_template('index.html' ,allTodo=allTodo)


@app.route('/show')
def products():
    allTodo=Todo.query.all()
    print(allTodo)
    return 'this is product page'


if __name__ == "__main__":
    # Ensure database tables are created in the application context
    with app.app_context():
        db.create_all()  # Create tables if they don't already exist
    app.run(debug=True)
