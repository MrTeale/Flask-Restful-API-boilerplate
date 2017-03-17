from src.config import config

def authentication(email, password):
    firebase = config()
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    if user['idToken'] != None:
        return user['idToken']
    else:
        print("ERROR: User is not logged in")
        return
