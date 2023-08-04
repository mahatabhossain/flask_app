from flask import Blueprint
from controllers.redis_controllar import set_data, get_data, delete_data, update_data

redis_router = Blueprint('redis', __name__)

@redis_router.post('/set')
def store_data():
    return set_data()

@redis_router.get('/get')
def fetch_data():
    return get_data()

@redis_router.delete('/delete')
def del_data():
    return delete_data()

@redis_router.put('/update')
def modify_data():
    return update_data()