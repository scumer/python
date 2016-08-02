# -*- coding: utf-8 -*-

import pyodbc


try:
	#cnxn=pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.108;port=1433;DATABASE=mydata;UID=sa;PWD=passwd')
	# cnxn=pyodbc.connect('DRIVER={SQL Server};SERVER=.;port=1433;DATABASE=PACS_TEST;UID=xuhui;PWD=085517')
	cnxn = pyodbc.connect('DSN=Techsvr_DSN;UID=xuhui;PWD=085517')
	cursor = cnxn.cursor()
	result = cursor.execute('select * from Pacs_MonitorInfo')
	# result = cursor.execute('select httpport from Pacs_MonitorInfo')
	# result = cursor.fetchone()
	result = cursor.fetchall()
	for x in result:
		for y in x:
			print y,
		print ''

	# print result[0]
	# for row in cursor.tables():
	# 	# print row.table_name
	# 	for y in x:
	# 		print y,
	# 	print ''
	# raise (pyodbc.Error,('mo','oi'))
	cnxn.close()
except pyodbc.Error, e:
    print e.args[0]
    print e.args[1]
    # print e

