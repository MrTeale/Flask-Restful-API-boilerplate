from src.config import config

def database():
    firebase = config()
    db = firebase.database()
    users = db.child("Database").get()
    #Other options can be found at https://github.com/thisbejim/Pyrebase
    return users.val()
