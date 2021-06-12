import flask
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='webAppFlaskFolder/templates')

#from crawler import Query(?)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home_post():
    userQuery = request.form['search']

    queryResult = Query.search(userQuery)
    return render_template('index.html', query=userQuery, resultList=queryResult)

@app.route('/', methods=['POST'])
def results():
    userQuery = request.form['search']

    queryResult = Query.search(userQuery)
    return render_template('index.html', query=userQuery, resultList=queryResult)

if __name__ == '__main__':
    app.run(debug = True)
