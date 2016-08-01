# codin=utf-8

import gdcm
import os

MOVE_CONFIG = { 
               'callingAE':'PY_QR_XH', 
               'callAE':'AE_QR_XH', 
               'retrievePort': 1060, 
               'port':1043, 
               'host':'192.168.33.189',
               # 'host':'127.0.0.1',
               'path':'./QR'
               }

STORE_CONFIG = { 
                'host':'127.0.0.1',
                'port':1045, 
                'callAE':'AE_Net',
                'callingAE':'PY_QR_XH', 
                'path':'./QR'
               }
 
studyUIDTag = gdcm.Tag(0x0020,0x000D)
seriesUIDTag = gdcm.Tag(0x0020,0x000E)
sopUIDTag = gdcm.Tag(0x0008,0x0018)

def _getQuery(kwargs):
    queryKeys = gdcm.DataSet()
    for key in kwargs:
        if key != studyUIDTag:
            continue
        de = gdcm.DataElement()
        de.SetTag(key)
        de.SetByteValue(kwargs[key],gdcm.VL(len(kwargs[key])))
        queryKeys.Insert(de)
    

    #ePatientRootType,eStudyRootType   # ePatient,eStudy,eSeries,eImage 
    query = gdcm.CompositeNetworkFunctions_ConstructQuery(gdcm.eStudyRootType,gdcm.eStudy,queryKeys,True) 
    # query = gdcm.CompositeNetworkFunctions_ConstructQuery(gdcm.eStudyRootType,gdcm.eStudy,queryKeys,True) 
    # print query.GetQueryDataSet()
    # print query.GetTagListByLevel(gdcm.eImage)
    # print query.ValidateQuery()
    return query


def findSCU(studyUID,seriesUID,sopUID):
    query = _getQuery(
        {
            studyUIDTag:studyUID,
            seriesUIDTag:seriesUID,
            sopUIDTag:sopUID
        })
    res = gdcm.DataSetArrayType()
    if gdcm.CompositeNetworkFunctions_CFind(MOVE_CONFIG['host'],MOVE_CONFIG['port'],query,res,MOVE_CONFIG['callingAE'],MOVE_CONFIG['callAE']):
        print 'result len:', res.size()
        for dataset in res:
            print dataset.GetDataElement(studyUIDTag)
            print dataset.GetDataElement(seriesUIDTag)
            print dataset.GetDataElement(sopUIDTag)

    return ''

def moveSCU(studyUID,seriesUID,sopUID):
    query = _getQuery(
        {
            studyUIDTag:studyUID,
            seriesUIDTag:seriesUID,
            sopUIDTag:sopUID
        })
    
    if not query.ValidateQuery(): return None
    if gdcm.CompositeNetworkFunctions_CMove(
                                            MOVE_CONFIG['host'],
                                            MOVE_CONFIG['port'],
                                            query,
                                            MOVE_CONFIG['retrievePort'],
                                            MOVE_CONFIG['callingAE'],
                                            MOVE_CONFIG['callAE'],
                                            MOVE_CONFIG['path']):
        filePath = MOVE_CONFIG['path'] + os.sep + sopUID + '.dcm'
        return os.path.abspath(filePath)
    else:
        return None


class SCUWatcher(gdcm.SimpleSubjectWatcher):
    def __init__(self, subject, comment=''):
        super(SCUWatcher, self).__init__(subject,comment)
        # print subject
        # self.subject = subject
        self.index = 0
    
    def ShowIteration(self):
        self.index += 1
        print self.index

    def ShowDataSet(self, caller, event):
        print caller
        print event
        
    def ShowAbort(self):
        print 'abort'

    def ShowFileName(self, caller, event):
        print caller
        print event

    def StartFilter(self):
        print 'StartFilter'

    def ShowProgress(self, caller, event):
        # print caller
        # print event
        # print event.this.GetProgress()
        # print gdcm.ProgressEvent_Cast(event).GetProgress()
        pass


def myscu(studyUID,seriesUID,sopUID):
    scu = gdcm.ServiceClassUser()
    
    watcher = None
    # watcher = SCUWatcher(scu, 'myscu')
    # watcher = gdcm.SimpleSubjectWatcher(scu, 'myscu')

    scu.SetHostname(MOVE_CONFIG['host'])
    scu.SetPort(MOVE_CONFIG['port'])
    scu.SetTimeout(100)
    scu.SetCalledAETitle(MOVE_CONFIG['callAE'])
    scu.SetAETitle(MOVE_CONFIG['callingAE'])
    scu.SetPortSCP(MOVE_CONFIG['retrievePort'])

    filename = 'QR/1.3.46.670589.30.1.6.963335137819.1.612.1430783775437.dcm'
    files = gdcm.FilenamesType()
    files.push_back(filename)

    query = _getQuery(
        {
            studyUIDTag:studyUID,
            seriesUIDTag:seriesUID,
            sopUIDTag:sopUID
        })
    print 'query:', query.ValidateQuery()

    print 'InitializeConnection:', scu.InitializeConnection()
    generator = gdcm.PresentationContextGenerator()
    generator.GenerateFromUID(query.GetAbstractSyntaxUID())
    scu.SetPresentationContexts(generator.GetPresentationContexts())

    if scu.StartAssociation():
        # pass
        # print 'Echo:',scu.SendEcho()
        res = gdcm.DataSetArrayType()
        # if scu.SendFind(query, res):
        if scu.SendMove(query, MOVE_CONFIG['path']):
            pass
            # for dataset in res:
            #     print dataset.GetDataElement(studyUIDTag)
            #     print dataset.GetDataElement(seriesUIDTag)
            #     print dataset.GetDataElement(sopUIDTag)
        scu.StopAssociation()

    if watcher:
        watcher.__disown__()

def storeSCU():
    try:
        scu = gdcm.ServiceClassUser()
        # watcher = gdcm.SimpleSubjectWatcher(scu,'SimpleSubjectWatcher')
        watcher = SCUWatcher(scu,'SimpleSubjectWatcher')

        scu.SetHostname(STORE_CONFIG['host'])
        scu.SetPort(STORE_CONFIG['port'])
        scu.SetTimeout(1000);
        scu.SetCalledAETitle(STORE_CONFIG['callAE'])
        scu.SetAETitle(STORE_CONFIG['callingAE'])

        directory = gdcm.Directory()
        directory.Load('QR')

        filename = 'QR/1.3.46.670589.30.1.6.963335137819.1.612.1430783775437.dcm'
        files = gdcm.FilenamesType()
        files.push_back(filename)

        scu.InitializeConnection()
        generator = gdcm.PresentationContextGenerator()
        # generator.GenerateFromUID(gdcm.UIDs.VerificationSOPClass);
        generator.GenerateFromFilenames(files)
        # generator.GenerateFromFilenames(directory.GetFilenames())
        scu.SetPresentationContexts(generator.GetPresentationContexts())

        if scu.StartAssociation():
            scu.SendStore(filename)
            scu.SendStore(filename)
            scu.StopAssociation()

        watcher.__disown__()
    except Exception, e:
        print e


if __name__ == "__main__":
    # gdcm.Trace_DebugOn()
    # print moveSCU('1.2.840.1.4.1.194.0.100000000.20150505073430.140.10000.2424418','1.3.46.670589.30.1.6.1.963335137819.1430783771546.1','1.3.46.670589.30.1.6.963335137819.1.612.1430783775437')
    # print findSCU('1.2.840.1.4.1.194.0.100000000.20150505073430.140.10000.2424418','1.2.840.1.19439.1.100000000.20160307175758.1933','1.2.840.2.1000001.1000001.20160225152451.1000041')
    # print moveSCU('1.2.840.1.4.1.194.0.100000000.20150505073430.140.10000.2424418','1.3.46.670589.30.1.6.1.963335137819.1430783771546.1','1.3.46.670589.30.1.6.963335137819.1.612.1430783775437')

    # myscu('1.2.840.1.4.1.194.0.100000000.20150505073430.140.10000.2424418','1.2.840.1.19439.1.100000000.20160307175758.1933','1.2.840.2.1000001.1000001.20160225152451.1000041')
    storeSCU()

    # cmd = CMD()


"""
PatientRootQueryRetrieveInformationModelFIND = 198, 
PatientRootQueryRetrieveInformationModelMOVE = 199, 
PatientRootQueryRetrieveInformationModelGET = 200, 

PatientStudyOnlyQueryRetrieveInformationModelFINDRetired = 204, 
PatientStudyOnlyQueryRetrieveInformationModelMOVERetired = 205, 
PatientStudyOnlyQueryRetrieveInformationModelGETRetired = 206, 

StudyRootQueryRetrieveInformationModelFIND = 201, 
StudyRootQueryRetrieveInformationModelMOVE = 202, 
StudyRootQueryRetrieveInformationModelGET = 203, 
"""