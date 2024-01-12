from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
from randomuser import randomusers


load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():

    paramas = request.args
    
    return render_template('index.html', context={'users': randomusers(paramas['n'], paramas['gender'])})


if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"), port=os.getenv("PORT"))
