from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Boss 😼 Jenkins is working!"

if __name__ == "__main__":
    app.run()
