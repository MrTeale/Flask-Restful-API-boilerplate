from src.config import config

def database():
    firebase = config()
    db = firebase.database()
    users = db.child("journalled-32fb").get()
    #Other options can be found at https://github.com/thisbejim/Pyrebase
    return users.val()

def save_data_timestamp(data, childName):
    firebase = config()
    db = firebase.database()
    db.child(childName).push(data)
    return

def save_data_customKey(keyName, dataValue, childName):
    firebase = config()
    db = firebase.database()
    data = {keyName: dataValue}
    db.child("users").child(childName).set(data)
    return

def update_data_customKey(keyName, dataValue, childName):
    firebase = config()
    db = firebase.database()
    data = {keyName: dataValue}
    db.child("users").child(childName).update(data)
    return
