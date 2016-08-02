# coding=utf-8
import time

from c_tasks import add, tsub

def on_success(self, retval, task_id, args, kwargs):
    print 'on_success'


# result = add.delay(1,2)
# result = add.delay(1,2)
result = add.apply_async(args=(1,2), link=tsub.s(4))
# print result.get()


# print result.backend

# while not result.ready():
#     # print 'False'
#     time.sleep(2)
#     result.status
# print result.get(timeout=1)

