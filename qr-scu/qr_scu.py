#!/usr/bin/python
# -*- coding: utf-8 -*-

import gdcm
import os

MOVE_CONFIG = {
               'callingAE':'AE_WYY',
               'callAE':'221_QR',
               'retrievePort': 1060,
               'port':1042,
               'host':'192.168.33.221',
               'path':'.'
               }

studyUIDTag = gdcm.Tag(0x0020,0x000D)
seriesUIDTag = gdcm.Tag(0x0020,0x000E)
sopUIDTag = gdcm.Tag(0x0008,0x0018)


def _getQuery(kwargs):
    queryKeys = gdcm.DataSet()
    for key in kwargs:
        de = gdcm.DataElement()
        de.SetTag(key)
        de.SetByteValue(kwargs[key],gdcm.VL(len(kwargs[key])))
        queryKeys.Insert(de)
    query = gdcm.CompositeNetworkFunctions_ConstructQuery(
        gdcm.eStudyRootType,gdcm.eImage,queryKeys,True)
    return query

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

