"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.pylint_controller import PylintController
from app.controllers.solid_controller import SolidController
from app.controllers.aaatesting_controller import AaatestingController
from app.controllers.oop_controller import OopController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/pylint", methods=['GET'])
def pylint_get():
    return PylintController.get()

@app.route("/solid", methods=['GET'])
def solid_get():
    return SolidController.get()

@app.route("/aaatesting", methods=['GET'])
def aaatesting_get():
    return AaatestingController.get()

@app.route("/oop", methods=['GET'])
def oop_get():
    return OopController.get()
