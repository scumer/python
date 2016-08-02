'''
Created on 2014-7-8

@author: septem
'''
import pyPacscore
import json

cache = pyPacscore.LocalFileCache.GetCacheInstance()

PACSCORE_CONFIG = {
                   'DSN':'PacsDB',
                   'DBUser':'sa',
                   'DBPassword':'winning',
                   'WebServiceURL':''
                   }

def initialize(user):
    initp = pyPacscore.InitParam()
    initp.UserID = user
    initp.Debug = False
    initp.UseLocal = True
    initp.ForceToCache = True
    initp.GetReload = False
    initp.CopyToCache = False
    return pyPacscore.initPacscore(initp)
    # return pyPacscore.quickInitialize(ServiceName=user,DSN='LocalPacsDB',User='sa',Password='d2lubmluZw==')

def getImage(studyUID,seriesUID,sopUID):
    return pyPacscore.getImage(studyUID,seriesUID,sopUID)
        
def getSeries(seriesUID):
    return pyPacscore.getSeries(seriesUID)
    
def getStudyLocalFileList(studyUID):
	query = pyPacscore.ImageInfo()
	query.StudyUID = studyUID
	return pyPacscore.GetImageOnlyLocal(query)

def imageInfo2Json(imginf):
    def Unicode(val):
        for codec in ['gbk','utf-8','gb2312']:
        	try:
        		return unicode(val,codec)
        	except:
        		pass
        else:
            return u''
                
    tags = {}
    for attr in dir(imginf):
        if not attr.startswith('__'):
            val = getattr(imginf,attr)
            tags[attr] = Unicode(val) if isinstance(val,str) else val
    return json.dumps(tags)

def removeCacheFile(fl):
    cache.DeleteCacheFile(fl)
    