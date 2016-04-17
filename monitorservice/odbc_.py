#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc

class MSSQL:
    """
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启
    """
    def __init__(self, dsn, user, pwd):
        self.dsn = dsn
        self.user = user
        self.pwd = pwd

    def __GetConnect(self):
        """
        得到连接信息
        返回： conn.cursor()
        """
        # print (self.host, self.user, self.pwd, self.db)
        
        # if not self.db:
        #     raise(NameError, "没有设置数据库信息")
    
    	login = 'DSN=%s;UID=%s;PWD=%s' % (self.dsn, self.user, self.pwd)
        self.conn = pyodbc.connect(login)

        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
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

        #查询完毕后关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
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

 

def main():
    ms = MSSQL('Techsvr_DSN', 'xuhui', '085517')
    #ms = MSSQL('192.168.33.220','sa','winning','PACS6.0')
    resList = ms.ExecQuery("SELECT AEID,AEName,AEType,AETitle,IP,Port FROM Pacs_AETitle WHERE AEType = 'X'")
    #resList = ms.ExecQuery('SELECT * FROM Pacs_AETitle')

    for (res) in resList:
        for r in res:
            print "%-10s" %r,
        print ''

if __name__ == '__main__':
    main()