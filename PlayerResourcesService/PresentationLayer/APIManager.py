from ..LogicLayer.UserResourcesLogic import ResourcesLogicHandler
from flask import Flask, request

app = Flask(__name__)

@app.route('/create_user_resources',methods=['PUT'])
def create_user_resources():
    return ResourcesLogicHandler.create_user(request.data)

@app.route('/update_user_resources',methods=['POST'])
def update_user_resources():
    return ResourcesLogicHandler.update_user_resource(request.data)

@app.route('/get_user_resources',methods=['GET'])
def get_user_resources():
    return ResourcesLogicHandler.collect_user_resources(request.data)