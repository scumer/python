# -*- coding: utf-8 -*-

"""
pymssql 测试
"""


import pymssql

class MSSQL:
    """
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启?
    """
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回： conn.cursor()
        """
        print (self.host, self.user, self.pwd, self.db)
        
        if not self.db:
            raise(NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        
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
        cur = sel.__GetConnect()
        cur.excute(sql)
        cur.conn.commit()
        self.conn.close()

 

def main():
    ms = MSSQL("192.168.33.189", "xuhui", "085517", "PACS_TEST")
    #ms = MSSQL('192.168.33.220','sa','winning','PACS6.0')
    resList = ms.ExecQuery("SELECT AEID,AEName,AEType,AETitle,IP,Port,AEDEsc FROM Pacs_AETitle WHERE AEType = 'X'")
    #print resList
    for res in resList:
        print res
    #for (id,weibocontent) in resList:
        #print str(weibocontent)

if __name__ == '__main__':
    main()


"""
使用pymssql进行中文操作时候可能会出现中文乱码，我解决的方案是：
文件头加上 #coding=utf8
sql语句中有中文的时候进行encode
insertSql = "insert into WeiBo([UserId],[WeiBoContent],[PublishDate]) values(1,'测试','2012/2/1')".encode("utf8")
连接的时候加入charset设置信息
pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
"""
