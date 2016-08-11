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
        self.host = Configure().get_default('DBConnect', 'Server', '.')
        self.user = Configure().get('DBConnect', 'DBUser')
        self.pwd = Configure().get_default('DBConnect', 'DBPassword', '')
        self.db = Configure().get('DBConnect', 'DBName')

        if self.pwd:
            self.pwd = b64decode(self.pwd)        

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8", login_timeout=2)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,u"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()    

    def ExecMany(self,*sql):
        cur = self.__GetConnect()
        cur.executemany(*sql)
        self.conn.commit()
        self.conn.close()  



if __name__ == '__main__':
    ms = MSSQL()
    resList = ms.ExecQuery("SELECT AEID,AEName,AEType,AETitle,IP,Port FROM Pacs_AETitle WHERE AEType = 'X'")
    #resList = ms.ExecQuery('SELECT * FROM Pacs_AETitle')
    for (res) in resList:
        for r in res:
            print "%-10s" %r,
        print ''