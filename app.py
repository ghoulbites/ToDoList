from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/testGet", )
def testReturn():
    return {
        "_id": 12,
        "firstName": "Mike",
        "lastName": "Hanna",
        "content": "This is some sample text",
        "for": 41
    }

app.run(debug=True, port=5000)
