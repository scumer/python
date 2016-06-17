# -*- coding: utf-8 -*-

import time
import os
import threading
import sched
from threading import Timer

timer_interval=1



def sayhello():
	print 'Timer:', os.getpid(), threading.current_thread()
	print time.strftime('%H:%M:%S',time.localtime(time.time()))
	Timer(5.0, sayhello).start() #Timer一次性定时  5s


def main():
	sayhello()

	while True:
		time.sleep(6)
		print 'Main:', os.getpid(), threading.current_thread()
		print '--main running--',
		print time.strftime('%H:%M:%S',time.localtime(time.time()))
		pass 

# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数 
# 第二个参数以某种人为的方式衡量时间 
schedule = sched.scheduler(time.time, time.sleep)
 
def perform_command(cmd, inc): 
    # 安排inc秒后再次运行自己，即周期运行 
    # schedule = sched.scheduler(time.time, time.sleep)
    print 'Main:', os.getpid(), threading.current_thread()
    print time.strftime('%H:%M:%S',time.localtime(time.time()))
    schedule.enter(inc, 0, perform_command, (cmd, inc)) 
    # os.system(cmd) 
        
def timming_exe(cmd, inc = 60): 
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动 
    print 'timming_exe'

    schedule.enter(inc, 0, perform_command, (cmd, inc)) 
    # 持续运行，直到计划时间队列变成空为止 
    schedule.run() 

# print("show time after 10 seconds:") 
# timming_exe("echo %time%", 5)
# if __name__ == '__main__':
# 	main()

def sched_fun():
	# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数 
	# 第二个参数以某种人为的方式衡量时间 
	# global schedule
	# schedule = sched.scheduler(time.time, time.sleep) 
	# enter用来安排某事件的发生时间，从现在起第n秒开始启动 
	inc=5
	cmd=''
	# schedule.enter(inc, 0, perform_command, (cmd, inc))
	# schedule.run()
	perform_command(5, 5)

sched_fun()
# 持续运行，直到计划时间队列变成空为止

