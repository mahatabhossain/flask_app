from flask import request, jsonify
from redis_server import redis_server_connection

def set_data():
    try:
        print('Set data called')
        body = request.get_json()
        name = body['name']
        company = body['company']

        print (name, company)
        redis_conn = redis_server_connection()
        # redis_conn.set('name', name)

        # set multiple key value at once
        redis_conn.msetnx({"name": name, "company": company})

        return 'Data set inot redis DB'

    except Exception as e:
        print(str(e))
        return str(e)


def get_data():
    try:
        print('Get data called')
        redis_conn = redis_server_connection()
        # data = redis_conn.get('name')

        data = redis_conn.mget(['name', 'company'])
        print(data)
        return jsonify({'name': list(map(lambda x: x.decode("utf8"), data))})
    except Exception as e:
        print(str(e))
        return str(e)
    

def update_data():
    try:
        print('Update data called')
        body = request.get_json()
        name = body['name']
        company = body['company']

        redis_conn = redis_server_connection()
        redis_conn.flushdb()

        redis_conn.mset({'company': company, 'name': name})
        return jsonify({'status': 'Updated'})

    except Exception as e:
        print(str(e))
        return str(e)
    
    
def delete_data():
    try:
        print('Delete data called')
        redis_conn = redis_server_connection()
        # redis_conn.delete('company')
        
        redis_conn.flushdb()

        return jsonify({'status': 'Deleted'})

    except Exception as e:
        print(str(e))
        return str(e)
