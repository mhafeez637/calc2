from app.controllers.controller import ControllerBase
from flask import render_template

class SolidController(ControllerBase):
    @staticmethod
    def get():
        return render_template('solid.html')
