import pyrebase

config = {
  "apiKey": "AIzaSyA0pOPKrSYSh8MToDEd7K6ZjfRJ23gc0kU",
  "authDomain": "catfarm-e3e93.firebaseapp.com",
  "databaseURL": "https://catfarm-e3e93.firebaseio.com",
  "storageBucket": "catfarm-e3e93.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.stream(stream_handler)
