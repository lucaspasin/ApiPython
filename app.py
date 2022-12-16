from flask import Flask
myapp = Flask(__name__)

import routes.receiver_routes

if __name__ == "__main__":
    myapp.run(debug=True)