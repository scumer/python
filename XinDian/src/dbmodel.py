# coding=utf-8

from sqlalchemy import Column, DateTime, Float, Index, Integer, LargeBinary, Numeric, SmallInteger, String, Table, Text, Unicode, UnicodeText, text
from sqlalchemy.dialects.mssql.base import MONEY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class PatientInfo(Base):
    __tablename__ = 'Ris_Interface_PatientInfo'
    __table_args__ = (
        Index('IX_Ris_Interface_PatInfo', 'CardNo', 'PatName'),
    )

    id = Column(Integer, nullable=False)
    CardNo = Column(String(50, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    PatName = Column(String(50, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    PatNameSpell = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    Sex = Column(String(10, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    Phone = Column(String(20, u'Chinese_PRC_CI_AS'))
    IDNum = Column(String(50, u'Chinese_PRC_CI_AS'))
    HospitalCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    CityCode = Column(String(10, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    CardState = Column(Integer, nullable=False, server_default=text("((0))"))
    InsertTime = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    ModifyTime = Column(DateTime, nullable=False, server_default=text("(getdate())"))


class XDReport(Base):
    __tablename__ = 'Ris_Interface_TaskInfo_XD'
    __table_args__ = (
        Index('IX_Ris_Interface_TaskInfo_XD_State', 'ReportState', 'ImageState'),
        Index('IX_Ris_Interface_TaskInfo_XD_Card', 'CardNo', 'PatName')
    )

    id = Column(Integer, primary_key=True)
    Studyuid = Column(String(128, u'Chinese_PRC_CI_AS'), nullable=False)
    ReportState = Column(Integer, nullable=False, server_default=text("((0))"))
    ImageState = Column(Integer, nullable=False, server_default=text("((0))"))
    CardNo = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    PatName = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    ApplyNo = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    Sex = Column(String(8, u'Chinese_PRC_CI_AS'), nullable=False)
    Age = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    BirthDay = Column(DateTime)
    HospNo = Column(String(50, u'Chinese_PRC_CI_AS'))
    LabelID = Column(String(50, u'Chinese_PRC_CI_AS'))
    InsertTime = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    ModifyTimeR = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    ModifyTimeI = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    ApplyDeptName = Column(String(50, u'Chinese_PRC_CI_AS'))
    WardName = Column(String(50, u'Chinese_PRC_CI_AS'))
    BedNo = Column(String(50, u'Chinese_PRC_CI_AS'))
    TechNo = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    ExecTime = Column(DateTime, nullable=False)
    InstName = Column(DateTime, nullable=False)
    StudyItem = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    StudyObservation = Column(String(256, u'Chinese_PRC_CI_AS'), nullable=False)
    StudyResult = Column(String(256, u'Chinese_PRC_CI_AS'), nullable=False)
    ReportDoctorName = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    VerifyDoctorName = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    ReportTime = Column(DateTime, nullable=False)
    VerifyTime = Column(DateTime, nullable=False)
    HR = Column(Integer)
    PR = Column(Float(53))
    QT = Column(Float(53))
    QTC = Column(Float(53))
    P = Column(Float(53))
    T = Column(Float(53))
    QRS = Column(Float(53))
    QRSaxis = Column(Float(53))
    Paxis = Column(Float(53))
    Taxis = Column(Float(53))
    SV1 = Column(Float(53))
    RV5 = Column(Float(53))
    

class Image(Base):
    __tablename__ = 'Pacs_Image'

    ImageID = Column(Integer, primary_key=True)
    StudyID = Column(Integer, nullable=False, index=True)
    SeriesID = Column(Integer, nullable=False, index=True)
    ImageUID = Column(String(128, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    AcqNo = Column(Integer)
    ImageNo = Column(Integer)
    ImageTime = Column(DateTime)
    ImageFormat = Column(Integer, nullable=False, server_default=text("(0)"))
    ImageFile = Column(String(256, u'Chinese_PRC_CI_AS'), nullable=False)
    ImageFileSize = Column(Float(53))
    Caption = Column(String(30, u'Chinese_PRC_CI_AS'), server_default=text("('')"))
    TakeinTime = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    DataStatus = Column(Integer, nullable=False, server_default=text("(0)"))
    CancelFlag = Column(Integer, nullable=False, server_default=text("(0)"))
    InsertTime = Column(DateTime, server_default=text("(getdate())"))
    nReserved1 = Column(Integer, server_default=text("(0)"))
    cReserved1 = Column(String(128, u'Chinese_PRC_CI_AS'), server_default=text("('')"))
    cReserved2 = Column(String(128, u'Chinese_PRC_CI_AS'), server_default=text("('')"))
    ImageType = Column(String(128, u'Chinese_PRC_CI_AS'))
    ImageComments = Column(String(2048, u'Chinese_PRC_CI_AS'))
    AcquisitionTime = Column(DateTime)
    ContentDateTime = Column(DateTime)
    PatientOrientation = Column(String(50, u'Chinese_PRC_CI_AS'))
    ImageFileSizeInByte = Column(Integer)
    TransferSyntaxUID = Column(String(128, u'Chinese_PRC_CI_AS'))
    SopClassUID = Column(String(128, u'Chinese_PRC_CI_AS'))
    SpecificCharacterSet = Column(String(16, u'Chinese_PRC_CI_AS'))
    Rows = Column(Integer)
    Columns = Column(Integer)
    BitAllocated = Column(Integer)
    BitStored = Column(Integer)
    HighBit = Column(Integer)
    WinWidth = Column(String(64, u'Chinese_PRC_CI_AS'))
    WinCenter = Column(String(64, u'Chinese_PRC_CI_AS'))
    WindowLevelExplanation = Column(String(192, u'Chinese_PRC_CI_AS'))
    ValidWindowLevel = Column(Integer)
    VOI_LUT_Length = Column(Integer)
    VOI_LUT_FirstPixel = Column(Integer)
    VOI_LUT_Bits = Column(Integer)
    PhotoMetric = Column(String(64, u'Chinese_PRC_CI_AS'))
    PixelRepresentation = Column(Integer)
    PixelSpacing = Column(String(34, u'Chinese_PRC_CI_AS'))
    ImagePixelSpacing = Column(String(34, u'Chinese_PRC_CI_AS'))
    FieldOfView = Column(String(64, u'Chinese_PRC_CI_AS'))
    RefUID = Column(String(128, u'Chinese_PRC_CI_AS'))
    SliceLoction = Column(Float(53))
    SliceThick = Column(Float(53))
    ImgPos = Column(String(51, u'Chinese_PRC_CI_AS'))
    ImageOrientation = Column(String(102, u'Chinese_PRC_CI_AS'))
    NumberOfFrames = Column(Integer)
    FrameTime = Column(Integer)
    CineRate = Column(Integer)
    MaskNum = Column(Integer)
    PixelAspectRatio = Column(String(64, u'Chinese_PRC_CI_AS'))
    RescaleSlope = Column(Float(53))
    RescaleIntercept = Column(Float(53))
    RescaleType = Column(String(64, u'Chinese_PRC_CI_AS'))
    cReserved3 = Column(String(128, u'Chinese_PRC_CI_AS'))
    ClipID = Column(String(128, u'Chinese_PRC_CI_AS'))


class Instance(Base):
    __tablename__ = 'Pacs_Instance'
    __table_args__ = (
        Index('IX_Pacs_Instance_SeriesIDVolumeID', 'SeriesID', 'VolumeID', unique=True),
    )

    InstanceID = Column(Integer, primary_key=True)
    SeriesID = Column(Integer, nullable=False)
    VolumeID = Column(Integer, nullable=False)
    CompressionID = Column(Integer)
    CopySource = Column(Integer)
    ImageCount = Column(Integer, server_default=text("(0)"))
    TotalFileSize = Column(Float(53), server_default=text("(0)"))
    DeleteFlag = Column(Integer, server_default=text("(0)"))
    DiscID = Column(String(16, u'Chinese_PRC_CI_AS'))
    InsertTime = Column(DateTime, index=True, server_default=text("(getdate())"))
    ModifyTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyUserID = Column(String(12, u'Chinese_PRC_CI_AS'))
    State = Column(Integer)
    nReserved1 = Column(Integer, server_default=text("(0)"))
    cReserved1 = Column(String(64, u'Chinese_PRC_CI_AS'), server_default=text("('')"))
    cReserved2 = Column(String(64, u'Chinese_PRC_CI_AS'), server_default=text("('')"))


class Series(Base):
    __tablename__ = 'Pacs_Series'

    SeriesID = Column(Integer, primary_key=True)
    StudyID = Column(Integer, nullable=False, index=True)
    Modality = Column(String(16, u'Chinese_PRC_CI_AS'), nullable=False)
    SeriesUID = Column(String(128, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    SeriesNo = Column(Integer, nullable=False)
    SeriesTime = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    SeriesDesc = Column(String(64, u'Chinese_PRC_CI_AS'))
    OperatorDoctor = Column(String(64, u'Chinese_PRC_CI_AS'))
    BodyPart = Column(String(32, u'Chinese_PRC_CI_AS'))
    StationName = Column(String(16, u'Chinese_PRC_CI_AS'), server_default=text("('')"))
    ImageCount = Column(Integer, server_default=text("(0)"))
    ImagePath = Column(String(256, u'Chinese_PRC_CI_AS'), nullable=False)
    TakeinTime = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    BackupStatus = Column(Integer, nullable=False, index=True, server_default=text("('0')"))
    BackupFailCount = Column(Integer, index=True, server_default=text("(0)"))
    InsertTime = Column(DateTime, server_default=text("(getdate())"))
    nReserved1 = Column(Integer, server_default=text("(0)"))
    cReserved1 = Column(String(128, u'Chinese_PRC_CI_AS'), server_default=text("('')"))
    cReserved2 = Column(String(128, u'Chinese_PRC_CI_AS'), server_default=text("('')"))
    ProtocolName = Column(String(64, u'Chinese_PRC_CI_AS'))
    Laterality = Column(String(16, u'Chinese_PRC_CI_AS'))
    PatientPosition = Column(String(16, u'Chinese_PRC_CI_AS'))
    ViewPosition = Column(String(16, u'Chinese_PRC_CI_AS'))
    Manufacturer = Column(String(64, u'Chinese_PRC_CI_AS'))
    ManufacturerModelName = Column(String(64, u'Chinese_PRC_CI_AS'))
    InstitutionName = Column(String(64, u'Chinese_PRC_CI_AS'))
    InstitutionDepartmentName = Column(String(64, u'Chinese_PRC_CI_AS'))
    InstitutionAddress = Column(String(1024, u'Chinese_PRC_CI_AS'))
    DeviceSerialNumber = Column(String(64, u'Chinese_PRC_CI_AS'))
    cReserved3 = Column(String(128, u'Chinese_PRC_CI_AS'))


class Study(Base):
    __tablename__ = 'Pacs_Study'
    __table_args__ = (
        Index('IX_Pacs_Study_Hosp_PatName', 'PatName', 'HospCode'),
        Index('IX_Pacs_Study_Hosp_AccessNo', 'AccessionNo', 'HospCode'),
        Index('IX_Pacs_Study_Hosp_Patid', 'PatID', 'HospCode'),
        Index('IX_Pacs_Study_Hosp_StudyTime', 'StudyTime', 'HospCode')
    )

    StudyID = Column(Integer, primary_key=True)
    StudyNo = Column(String(64, u'Chinese_PRC_CI_AS'))
    StudyUID = Column(String(128, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    Modality = Column(String(16, u'Chinese_PRC_CI_AS'), nullable=False)
    StudyTime = Column(DateTime, nullable=False, index=True, server_default=text("(getdate())"))
    StudyDoctor = Column(String(64, u'Chinese_PRC_CI_AS'))
    StudyDesc = Column(String(64, u'Chinese_PRC_CI_AS'))
    ApplyNo = Column(Integer, index=True)
    PatID = Column(String(64, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    OthID = Column(String(64, u'Chinese_PRC_CI_AS'))
    AccessionNo = Column(String(16, u'Chinese_PRC_CI_AS'), index=True)
    PatName = Column(String(64, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    Name_Chn = Column(String(64, u'Chinese_PRC_CI_AS'))
    Sex = Column(String(1, u'Chinese_PRC_CI_AS'), nullable=False, server_default=text("('O')"))
    Birthday = Column(DateTime, server_default=text("(getdate())"))
    Age = Column(String(16, u'Chinese_PRC_CI_AS'))
    TakeinTime = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    StudyType = Column(Integer, nullable=False, server_default=text("(0)"))
    DataStatus = Column(Integer, nullable=False, server_default=text("(0)"))
    InsertTime = Column(DateTime, server_default=text("(getdate())"))
    nReserved1 = Column(Integer, server_default=text("(0)"))
    cReserved1 = Column(String(128, u'Chinese_PRC_CI_AS'), server_default=text("('')"))
    cReserved2 = Column(String(128, u'Chinese_PRC_CI_AS'), server_default=text("('')"))
    PatientComments = Column(String(2048, u'Chinese_PRC_CI_AS'))
    PatientSize = Column(String(16, u'Chinese_PRC_CI_AS'))
    PatientWeight = Column(String(16, u'Chinese_PRC_CI_AS'))
    SeriesCountInStudy = Column(Integer)
    ImageCountInStudy = Column(Integer)
    BackupStatus = Column(Integer)
    BackupFailCount = Column(Integer)
    cReserved3 = Column(String(128, u'Chinese_PRC_CI_AS'))
    HospCode = Column(String(50, u'Chinese_PRC_CI_AS'), server_default=text("('0000')"))
    HospName = Column(String(50, u'Chinese_PRC_CI_AS'))
    DeptNo = Column(String(12, u'Chinese_PRC_CI_AS'))
    DeptName = Column(String(50, u'Chinese_PRC_CI_AS'))


class ATEST(Base):
    __tablename__ = 'ATEST'

    id = Column(Integer, primary_key=True)
    time = Column(DateTime)    