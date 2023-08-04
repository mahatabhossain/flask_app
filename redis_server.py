import redis

def redis_server_connection():
# Redis parameters
    redis_host = 'localhost'
    redis_port = 6379
    redis_db = 0

    #redis connection
    redis_conn = redis.StrictRedis(
        host=redis_host,
        port=redis_port,
        db=redis_db
    )
    print("Redis server connected")
    return redis_conn


    

    

