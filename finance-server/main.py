from flask import Flask

app = Flask(__name__,static_folder="uploads",static_url_path="/uploads")

from route.user_route import *
from route.file_route import *
from db import *

if __name__ == '__main__':
    app.run(debug=True,port=5000)