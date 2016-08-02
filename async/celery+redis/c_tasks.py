# coding=utf-8

from celery import Celery

# app = Celery('tasks', broker='redis://localhost:6379/0')
# app = Celery(__name__, broker='redis://', backend='rpc://')
# app = Celery('c_tasks', broker='redis://', backend='redis://')

celery_app = Celery(__name__)
# logger = setup_logger(__name__)

config = {
    'BROKER_URL': 'redis://',
    'CELERY_RESULT_BACKEND': 'rpc://',
}
celery_app.conf.update(config)


@celery_app.task
def add(x, y):
    # return x + y
    print '*add*'
    print 'add argv:', x,y
    return x+y



@celery_app.task
def tsub(x,y):
    print '*tsub*'
    print 'tsub argv:', x,y



# def make_celery():
#     celery_app.conf.update(config)
#     base_task = celery_app.Task

#     class ContextTask(base_task):
#         abstract = True

#         def __call__(self, *args, **kwargs):
#             with flask_app.app_context():
#                 return base_task.__call__(self, *args, **kwargs)

#     celery_app.Task = ContextTask
#     return celery_app

if __name__ == '__main__':
    celery_app.start(['celery', '-A', 'c_tasks','worker','-l','info'])