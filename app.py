from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pickle
import pdb
import os


DB = SQLAlchemy()

APP = Flask(__name__)

DB.init_app(APP)

# Set up the main route
@APP.route('/')
def main():
        return render_template('index.html')


if __name__ == '__main__':
        APP.run()