#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymssql


conn = pymssql.connect(host=r"192.168.33.189", user="xuhui", password="085517", database="PACS_TEST")
#conn = pymssql.connect(host="192.168.33.220:1433", user="sa", password="winning", database="PACS6.0")
print conn

cur = conn.cursor()
#print cur

cur.execute('SELECT * FROM Pacs_AETitle')

ret = cur.fetchall()
print ret
conn.close()
