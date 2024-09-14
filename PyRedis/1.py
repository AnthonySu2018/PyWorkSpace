import redis

r = redis.StrictRedis(host='192.168.8.129', port=6379, db=0)

r.set('foo', 'bar')
print(r.get('foo'))