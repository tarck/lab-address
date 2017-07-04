from flask import Flask
from flask import Flask, render_template
import csv

app = Flask(__name__)

f = open("KEN_ALL_ROME.CSV", "r")
reader = csv.reader(f)

@app.route('/')
def index():
    return 'Hello World!'

@app.route("/<code>")
def hello(code):
    for i in reader:
        if i[0] == '640947':
            city = i[3].decode('shift-jis')
            break

	return render_template("test.html", message=city)

if __name__ == '__main__':
    app.run()
