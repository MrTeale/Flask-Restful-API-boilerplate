import pyrebase

def config():
    config = {
        "apiKey": "AIzaSyB4pbzsdSqylKwKpjG3xJwSCHf0vovy22s",  # Replace apiKey with yours
        "authDomain": "journalled-32fcb.firebaseapp.com",  # Replace projectId with yours
        "databaseURL": "https://journalled-32fcb.firebaseio.com/",  # Replace databaseName with yours
        "storageBucket": "journalled-32fcb.appspot.com"  # Replace storageBucket with yours
        #  Uncomment line below in order to access as an admin (requires .json file with credentials)
        # "serviceAccount": "path/to/serviceAccountCredentials.json"
    }

    firebase = pyrebase.initialize_app(config)
    return firebase
