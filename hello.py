
from flask import Flask
app = Flask(__name__)

this is not good

@app.route("/")
def index():
    return "<p>Hello .. Welcome to the World of Learning!</p>" 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug=True) 
