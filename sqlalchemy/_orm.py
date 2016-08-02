# coding=utf-8

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker

from mssql_model import *


db = create_engine("mssql+pymssql://xuhui:@127.0.0.1/PACS_TEST?charset=utf8", convert_unicode=True) 
Session = sessionmaker(bind=db)
session = Session()

# result = db.execute('select * from users')

# ret = result.fetchone()

# print ret[0],ret[1] 

# our_user = session.query(User).filter_by(UserID='001').first()
# study = session.query(PacsVolumeAcces.VolumeID, PacsVolume.VolumeID).filter().all()
# # print study
# # print list(study)
# for row,row1,in study:
#     # print list(row)
#     print row,
#     print row1
    # print row[0],row[1]


# import script
from sqlalchemy import text
# our_user = session.query(t_EFilm_Handling_Task).filter_by(t_EFilm_Handling_Task.c.PrintStat==1).first()
our_user = session.query(t_EFilm_Handling_Task).filter(text("PrintStat=1")).first()
print our_user.HttpJson


session.execute()


