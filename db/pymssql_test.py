# -*- coding: utf-8 -*-

"""
pymssql ����
"""


import pymssql

class MSSQL:
    """
    ʹ�øÿ�ʱ����Ҫ��Sql Server Configuration Manager���潫TCP/IPЭ�鿪��?
    """
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        �õ�������Ϣ
        ���أ� conn.cursor()
        """
        print (self.host, self.user, self.pwd, self.db)
        
        if not self.db:
            raise(NameError, "û���������ݿ���Ϣ")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        
        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "�������ݿ�ʧ��")
        else:
            return cur

    def ExecQuery(self, sql):
        """
        ִ�в�ѯ���
        ���ص���һ������tuple��list��list��Ԫ���Ǽ�¼�У�tuple��Ԫ����ÿ�м�¼���ֶ�

        ����ʾ����
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #��ѯ��Ϻ�ر�����
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        """
        ִ�зǲ�ѯ���

        ����ʾ����
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
ʹ��pymssql�������Ĳ���ʱ����ܻ�����������룬�ҽ���ķ����ǣ�
�ļ�ͷ���� #coding=utf8
sql����������ĵ�ʱ�����encode
insertSql = "insert into WeiBo([UserId],[WeiBoContent],[PublishDate]) values(1,'����','2012/2/1')".encode("utf8")
���ӵ�ʱ�����charset������Ϣ
pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
"""
