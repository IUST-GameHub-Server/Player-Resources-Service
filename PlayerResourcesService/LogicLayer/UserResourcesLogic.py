from ..DataLayer.DataAccess import DataAccess
from types import SimpleNamespace
import json

class ResourcesLogicHandler:
    def create_user(user_info):
        user= json.loads(user_info, object_hook=lambda d: SimpleNamespace(**d))
        DataAccess.create_user(user.email)

    def collect_user_resources(user_info):
        user= json.loads(user_info, object_hook=lambda d: SimpleNamespace(**d))
        result={
            "coins":DataAccess.get_coins(user.email),
            "tickets":DataAccess.get_tickets(user.email),
            "gems":DataAccess.get_gems(user.email)
        }
        return json.dumps(result)
    
    def update_user_resource(user_info):
        user= json.loads(user_info, object_hook=lambda d: SimpleNamespace(**d))
        DataAccess.set_coins(user.email, user.coins)
        DataAccess.set_gems(user.email, user.gems)
        DataAccess.set_tickets(user.email, user.tickets)
        result={
            "coins":DataAccess.get_coins(user.email),
            "tickets":DataAccess.get_tickets(user.email),
            "gems":DataAccess.get_gems(user.email)
        }
        return json.dumps(result)