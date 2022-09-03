from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore, db

"""
cred = credentials.Certificate("data/firebase_sdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()  # this connects to our Firestore database
collection = db.collection('users')  # opens 'places' collection
#doc = collection.document('rome')  # specifies the 'rome' document
res = collection.document('aura_test').set({
    'game': 1,
    'password': 'test',
    'user': 'aura',
    'secret_name': 'bird'
})

"""
app = Flask(__name__)


@app.route("/home")
def home():
    return render_template('home.html')


if __name__ == "main":
    app.run(debug=True)