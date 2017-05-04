from src.config import config

def get_info(email, password):
    firebase = config()
    auth = firebase.auth()
    user = auth.get_account_info(email, password)

    return user

def create_user(email, password):
    firebase = config()
    auth = firebase.auth()

    # Make sure you have email/password Auth allowed on your dashboard
    user = auth.create_user_with_email_and_password(email, password)

    if user['idToken'] != None:
        # auth.send_email_verification(user['idToken'])
        auth.get_account_info(user['idToken'])
        return user['idToken']
    else:
        error = "ERROR: User is not logged in"
        return error

def refresh_user_token(email, password):
    firebase = config()
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    user = auth.refresh(user['refreshToken'])

    if user['idToken'] != None:
        return user['idToken']
    else:
        error = "ERROR: User is not logged in"
        return error
