from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
        return "CS172 Crawler Final Project"

if __name__ == "__main__":
    app.run()
