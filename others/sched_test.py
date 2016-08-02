# -*- coding: utf-8 -*-

import time
import os
import threading
import sched
# from threading import Timer

# schedule = sched.scheduler(time.time, time.sleep)

def prt():
	print 'Main:', os.getpid(), threading.current_thread()
	print time.strftime('%H:%M:%S',time.localtime(time.time()))



def sched_task():
	prt()
	schedule = sched.scheduler(time.time, time.sleep)
	schedule.enter(5, 0, sched_task,())
	schedule.run()


def main():
	sched_task() #
	print '------'


if __name__ == '__main__':
	main()