import pyrebase
from flask import Flask, render_template, request

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyAInt6Z0EXxsRgA8W3QfItFpHlhqSy5jdw",
    "authDomain": "challecara-app.firebaseapp.com",
    "databaseURL": "https://challecara-app.firebaseio.com",
    "projectId": "challecara-app",
    "storageBucket": "challecara-app.appspot.com",
    "messagingSenderId": "393001281058",
    "appId": "1:393001281058:web:d47fd2dacfaaa7a1ae0c7b",
    "measurementId": "G-W581ZTLB6F"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()


@app.route("/sign_up_do", methods=["POST"])
def sign_up_do():
        if request.method == "POST":
                result = request.form
                user = auth.create_user_with_email_and_password(result['email'], result['password'])
                auth.send_email_verification(user['idToken'])
                user = auth.refresh(user['refreshToken'])
                data = {"name": result['name']}
                db.child("users").push(data, user['idToken'])
                return 'finished!!'
        else:
                render_template('login/sign_up.html')

@app.route("/sign_up")
def sign_up():
    return render_template('login/sign_up.html')

@app.route("/sign_in")
def sign_in():
        return render_template('login/sign_in.html')

@app.route("/sign_in_do", methods=['POST'])
def sign_in_do():
        result = request.form
        user = auth.sign_in_with_email_and_password(result['email'], result['password'])
        x = auth.get_account_info(user['idToken'])
        return x


@app.route("/")
def home():
        return 'HOME'



app.run(host="localhost", debug=True)

