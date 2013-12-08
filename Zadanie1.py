from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    tekst= "Hello World!"
    return tekst
if __name__ == "__main__":
    app.run()
