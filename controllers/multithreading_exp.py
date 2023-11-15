import threading
import time

def task():
    """
        background process handled by thread
    """
    print('Task started....', threading.current_thread().name)
    #some CPU intensive task
    time.sleep(10)
    print('Task finished !')
    return {'status': 'Thread ran successfully'}

def thread_handler():
    task_thread = threading.Thread(target=task)
    task_thread.start()
    return {'status': 'thread is running in background'}





