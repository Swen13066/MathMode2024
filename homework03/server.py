import time
from pydantic import BaseModel, validator
import flask
from flask import Flask, abort

app = Flask(__name__)
db = []
for i in range(3):
    db.append({
        'name': f'user{i}',
        'time': 1000*i,
        'text': f'text by user{i}'
    })


class Message(BaseModel):
    name: str
    text: str

    @validator("text")
    @classmethod
    def validate_text(cls, value):
        text_length = len(value)
        if text_length == 0:
            raise ValueError()
        return value


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/send", methods=['POST'])
def send_message():
    data = flask.request.json
    try:
        message = Message(**data)
    except:
        return abort(400)

    new_message = {
        'name': message.name,
        'text': message.text,
        'time': time.time()
    }
    db.append(new_message)
    return {'ok': True}


@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}


@app.route("/status")
def status():
    num_users = 0
    unic_names = []
    for user in db:
        if user['name'] not in unic_names:
            num_users += 1
            unic_names.append(user['name'])

    num_messages = len(db)

    status_info = {
        "Current Time": time.ctime(),
        "Number of Users": num_users,
        "Number of Messages": num_messages
    }

    return flask.jsonify(status_info)


@app.route('/index')
def index():
    return flask.render_template('index.html')


app.run()