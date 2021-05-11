from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.TIMESTAMP, default=db.func.now())
    updated_on = db.Column(db.TIMESTAMP, default=db.func.now(), onupdate=db.func.now())

class Task(BaseModel):
    __tablename__ = 'tasks'

    status = db.Column(db.String(80))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, status, content):
        self.status = status
        self.content = content

class User(BaseModel):
    __tablename__ = 'users'

    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

class Word(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100))

    def __init__(self, word):
        self.word = word

tags = db.Table('tasks_words',
    db.Column('task_id', db.Integer, db.ForeignKey('tasks.id')),
    db.Column('word_id', db.Integer, db.ForeignKey('words.id')),
    db.Column('count', db.Integer)
)

@app.route('/')
def index():
    task = Task(status='dsfsaf',content='fdsafds')
    db.session.add(task)
    db.session.commit()
    return "Hello, World!"

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)