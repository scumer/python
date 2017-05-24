# -*- coding: utf-8 -*-

import pymssql
import _mssql
import decimal
from base64 import b64decode

from config import SingletonMeta, Configure

class MSSQL(object):

    __metaclass__ = SingletonMeta

    """
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启
    """
    def __init__(self):
        host = Configure().get_default('DBConnect', 'Server', '.')
        user = Configure().get('DBConnect', 'DBUser')
        pwd = Configure().get_default('DBConnect', 'DBPassword', '')
        db = Configure().get('DBConnect', 'DBName')

        # if self.pwd:
        #     self.pwd = b64decode(self.pwd)        

        self.conn_info = dict(host=host,user=user,password=pwd,database=db,charset="utf8", login_timeout=2)

    def ExecProc(self, *sql):
        with pymssql.connect(**self.conn_info) as conn:
            with conn.cursor(as_dict=True) as cursor:
                cursor.callproc(*sql)
                reslist = [row for row in cursor]
                conn.commit()
                return reslist

    def ExecQuery(self, *sql):
        with pymssql.connect(**self.conn_info) as conn:
            with conn.cursor(as_dict=True) as cursor:
                cursor.execute(*sql)
                return cursor.fetchall()

    def ExecNonQuery(self, *sql):
        with pymssql.connect(**self.conn_info) as conn:
            with conn.cursor(as_dict=True) as cursor:
                cursor.execute(*sql)
                conn.commit()        

    def ExecMany(self,*sql):
        with pymssql.connect(**self.conn_info) as conn:
            with conn.cursor(as_dict=True) as cursor:
                cursor.executemany(*sql)
                conn.commit()    


if __name__ == '__main__':
    ms = MSSQL()
    # reslist = ms.ExecQuery("select * from sys_czry")
    # print reslist
    
    # reslist = ms.ExecNonQueryEx("update Dept set MemCode1=2 where DeptNo=1")
    # reslist = ms.ExecQuery("select * from sys_czry")

    # reslist = ms.ExecQuery("sp_GetServiceConfig %s" % "THDataUP")
    # reslist = ms.ExecQuery("select * from LocalConfig")
    # reslist = ms.ExecProc("sp_GetServiceConfig", ('THDataUP',))
    # reslist = MSSQL().ExecProc("sp_GetOneTask1", ('Study',))

    reslist = MSSQL().ExecProc("USP_BI_BBSJ_HZ", ('<PARAS><JGBM>+86</JGBM></PARAS>',))
    reslist = MSSQL().ExecProc("USP_BI_BBSJ_SHJHZ", ('<PARAS><JGBM>+86</JGBM></PARAS>',))

#     EXEC USP_BI_BBSJ_HZ'<PARAS><JGBM>+86</JGBM></PARAS>';
# EXEC USP_BI_BBSJ_SHJHZ'<PARAS><JGBM>+86</JGBM></PARAS>';


    print reslist

    # print ms.conn_info
