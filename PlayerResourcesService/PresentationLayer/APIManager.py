from ..LogicLayer.UserResourcesLogic import UserResourcesLogic
from flask import Flask

app = Flask(__name__)
config=""

@app.route('/show_acquired_resources')
def show_acquired_resources(email):
    return "Not Implemented"

@app.route('/show_additional_allowed_activities')
def show_additional_allowed_activities (email):
    return "Not Implemented"


@app.route('/show_possible_obtainable_resources')
def show_possible_obtainable_resources (email):
    return "Not Implemented"

@app.route('/show_purchased_resources')
def show_purchased_resources (email):
    return "Not Implemented"
