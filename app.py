from flask import flask
app = flask(__name__)

@app.route("/")
def hello_world():
    return "hello world from ITU IEEE RAS"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")