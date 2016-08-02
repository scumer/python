# coding=utf-8

import redis

con = redis.Redis()

print con.keys()