"""This script prompts a user to enter a message to encode or decode
 using a classic Caesar shift substitution (3 letter shift)"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    """ Rien """
    return "Hello world !"
@app.route('/hello/fanina')
def optional():
    """ Rien """
    return "Hello "
if __name__ == "__main__":
    app.run()
