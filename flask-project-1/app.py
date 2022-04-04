from distutils.log import debug
from FLASK import flask

app = flask()

@app.route('/')
def testApp():
    return "Success"

if __name__ == '__main__':
    app.run(debug=True)