import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FireBaseInit:
    credentials_file = '/home/eduarte/credentials/diagnostico_firebase_desktop.json'
    instance = None

    def __new__(cls):
        if cls.instance is None:
            print('Initializing firestore and authetenticate client')
            cred = credentials.Certificate(FireBaseInit.credentials_file)
            firebase_admin.initialize_app(cred, {
                'projectId': 'dulcineia-ee8f1',
            })
            cls.instance = super(FireBaseInit, cls).__new__(cls)
            return cls.instance
        return cls.instance

    def get_db(self):
        return firestore.client()




