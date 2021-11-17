from flask import Flask

app = Flask(__name__)

count = 0


@app.route("/")
def hello():
    global count
    count += 1
    return 'Hello, World! <a href="/page2">Page 2</a>'


@app.route("/page2")
def page2():
    global count
    count += 1
    return 'Hello, again! <a href="/">Main page</a>'


@app.route("/stats")
def stats():
    global count
    count += 1
    return f'Visits: {count} <a href="/">Main page</a>'


app.run()
