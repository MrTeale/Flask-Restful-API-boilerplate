import pyrebase

def config():
    config = {
        "apiKey": "apiKey",  # Replace apiKey with yours
        "authDomain": "projectID.firebaseapp.com",  # Replace projectId with yours
        "databaseURL": "https://databaseName.firebaseio.com/",  # Replace databaseName with yours
        "storageBucket": "storageBucket.appspot.com"  # Replace storageBucket with yours
        #  Uncomment line below in order to access as an admin (requires .json file with credentials)
        # "serviceAccount": "path/to/serviceAccountCredentials.json"
    }

    firebase = pyrebase.initialize_app(config)
    return firebase
