# coding=utf-8

from base64 import b64decode

import pymssql, _mssql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker

from config import SingletonMeta, Configure


ECHO = False


class DBSession(object):

    __metaclass__ = SingletonMeta

    def __init__(self):

        server = Configure().get_default('DBConnect', 'Server', '.')
        username = Configure().get('DBConnect', 'DBUser')
        userpswd = Configure().get_default('DBConnect', 'DBPassword', '')
        dbname = Configure().get('DBConnect', 'DataBase')

        if userpswd:
            userpswd = b64decode(userpswd)

        self.conn_str = "mssql+pymssql://%s:%s@%s/%s?charset=utf8&login_timeout=2" % (username, userpswd, server, dbname)
        self.db_engine = create_engine(self.conn_str,convert_unicode=True, echo=ECHO) 
        # db = create_engine("mssql+pymssql://xuhui:@127.0.0.1/PACS_TEST?charset=utf8", convert_unicode=True, echo=True) 
        self.session_factory = sessionmaker(bind=self.db_engine)

    def get_session(self):
        return self.session_factory()

    def get_engine(self):
        return self.db_engine

    def get_connstr(self):
        return self.conn_str


if __name__ == '__main__':
    from dbmodel import *
    session = DBSession().get_session()
    # our_user = session.query(User.__table__).filter_by(UserID='001').all()
    # our_user = session.query(User).filter_by(UserID='001').all()
    # study = session.query(PacsVolumeAcces.VolumeID, PacsVolume.VolumeID).filter().first()
    # study = session.query(PacsVolumeAcces.VolumeID, PacsVolume.VolumeID).filter()
    # our_user = session.query(PatientInfo).filter(text("id=1"))
    # for row in our_user:
    #     print row.__dict__
    #     break
    ret = session.execute('tsp_QueryFilmTask :taskname,:count',{'taskname':'','count':3}).fetchall()
    print ret