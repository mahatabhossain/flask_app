from flask import Blueprint
from controllers.multithreading_exp import thread_handler

exp_router = Blueprint('miscellaneous_router', __name__)

@exp_router.get('/check/thread')
def thread_checker():
    return thread_handler()