from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'#type of database is defined and name also defined through link provided name is todo and type is sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to avoid unnecessary warnings

db = SQLAlchemy(app)#Initializes the SQLAlchemy object with the Flask application instance.
#Establishes the connection between Flask and the database defined in SQLALCHEMY_DATABASE_URI.


class Todo(db.Model):#class name could be anything here Todo is the class name 
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:#it used to return the data when the Todo is called ,i.e sno and title are returned
        return f"{self.sno} - {self.title}"


@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=="POST":
        
        
        
    todo =Todo(title="First Todo", desc="Start Investing in Stocks")#an instance of Todo class created
    db.session.add(todo)                                            #and added to the active session 
    db.session.commit()                                              #changes are saved
    allTodo=Todo.query.all()                                        #all the objects/rows of the database is quiered and stored using Todo.queryall()
    return render_template('index.html' ,allTodo=allTodo)           #all to objects are displayed on web through html file


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
