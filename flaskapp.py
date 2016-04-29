from flask import Flask
from flask import render_template
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('mongodb://admin:NC2efArdRDlT@127.7.235.130:27017/')
mon_db = client.flaskproject


def get_data():
    text = str
    cursor = mon_db.books.find()
    for data in cursor:
        text = data
    return text

x = 5
@app.route("/")
def main():
    return render_template('index.html', mongo=get_data()['title'])


@app.route("/showSignUp")
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
