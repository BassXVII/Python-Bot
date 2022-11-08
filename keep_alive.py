from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "<h1>hey, this was a test</h1>"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()