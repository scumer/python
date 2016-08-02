# coding=utf-8

from sqlalchemy import Column, DateTime, Float, Index, Integer, LargeBinary, Numeric, SmallInteger, String, Table, Text, Unicode, UnicodeText, text
from sqlalchemy.dialects.mssql.base import MONEY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


t_ACR_ILLNESS = Table(
    'ACR_ILLNESS', metadata,
    Column('PCODE', String(255, u'Chinese_PRC_CI_AS'), nullable=False, index=True),
    Column('ICODE', String(255, u'Chinese_PRC_CI_AS'), nullable=False, index=True),
    Column('NOTE', String(255, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('NOTE_EN', String(255, u'Chinese_PRC_CI_AS'), nullable=False)
)


t_ACR_PART = Table(
    'ACR_PART', metadata,
    Column('PCODE', String(255, u'Chinese_PRC_CI_AS'), nullable=False, index=True),
    Column('NOTE', String(255, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('NOTE_EN', String(255, u'Chinese_PRC_CI_AS'), nullable=False)
)


class ApplyInfoList(Base):
    __tablename__ = 'ApplyInfoList'

    ApplyNo = Column(Integer, primary_key=True)
    ApplyTime = Column(DateTime, nullable=False)
    FromDept = Column(String(12, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ToDept = Column(String(12, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ApplyDocCode = Column(String(12, u'Chinese_PRC_CI_AS'), nullable=False)
    ApplyDocName = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    ExecStatus = Column(Integer, nullable=False)
    OrgApplyNo = Column(Integer, index=True)
    ExeApplyNo = Column(Integer)
    TechNo = Column(String(20, u'Chinese_PRC_CI_AS'), index=True)
    LabelID = Column(String(32, u'Chinese_PRC_CI_AS'), index=True)
    TechPatID = Column(Integer, index=True)
    PatName = Column(String(40, u'Chinese_PRC_CI_AS'), index=True)
    PatNameSpell = Column(String(40, u'Chinese_PRC_CI_AS'))
    PatientID = Column(Integer, index=True)
    CureNo = Column(Integer, index=True)
    CardNo = Column(String(30, u'Chinese_PRC_CI_AS'), index=True)
    HospNo = Column(String(20, u'Chinese_PRC_CI_AS'), index=True)
    Sex = Column(String(1, u'Chinese_PRC_CI_AS'))
    Age = Column(Numeric(5, 2))
    AgeUnit = Column(String(6, u'Chinese_PRC_CI_AS'))
    Birthday = Column(DateTime)
    Career = Column(String(30, u'Chinese_PRC_CI_AS'))
    Phone = Column(String(20, u'Chinese_PRC_CI_AS'))
    Address = Column(String(100, u'Chinese_PRC_CI_AS'))
    Zip = Column(String(6, u'Chinese_PRC_CI_AS'))
    Nation = Column(String(20, u'Chinese_PRC_CI_AS'))
    IDNum = Column(String(20, u'Chinese_PRC_CI_AS'))
    ChargeType = Column(String(12, u'Chinese_PRC_CI_AS'))
    ChargeTypeName = Column(String(50, u'Chinese_PRC_CI_AS'))
    ApplyDept = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyDeptName = Column(String(50, u'Chinese_PRC_CI_AS'))
    Ward = Column(String(12, u'Chinese_PRC_CI_AS'))
    WardName = Column(String(50, u'Chinese_PRC_CI_AS'))
    BedNo = Column(String(10, u'Chinese_PRC_CI_AS'))
    WardOrReg = Column(String(12, u'Chinese_PRC_CI_AS'))
    BriefCase = Column(String(255, u'Chinese_PRC_CI_AS'))
    ClinicDesc = Column(String(255, u'Chinese_PRC_CI_AS'))


class ApplyInfoResult(Base):
    __tablename__ = 'ApplyInfoResult'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ApplyNo = Column(Integer, nullable=False, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemResult = Column(String(7000, u'Chinese_PRC_CI_AS'))


class ChargeItemDic(Base):
    __tablename__ = 'ChargeItemDic'

    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ItemCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ItemType = Column(Integer, primary_key=True, nullable=False)
    ItemName = Column(String(100, u'Chinese_PRC_CI_AS'))
    Price = Column(MONEY)
    Unit = Column(String(20, u'Chinese_PRC_CI_AS'))
    MemCode1 = Column(String(20, u'Chinese_PRC_CI_AS'))
    MemCode2 = Column(String(20, u'Chinese_PRC_CI_AS'))


class ChineseCode(Base):
    __tablename__ = 'ChineseCode'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    Character = Column(String(4, u'Chinese_PRC_CI_AS'), index=True)
    Spell = Column(String(6, u'Chinese_PRC_CI_AS'))
    TypeCode1 = Column(String(6, u'Chinese_PRC_CI_AS'))
    TypeCode2 = Column(String(6, u'Chinese_PRC_CI_AS'))
    TypeCode3 = Column(String(6, u'Chinese_PRC_CI_AS'))
    TypeCode4 = Column(String(30, u'Chinese_PRC_CI_AS'))
    TypeCode5 = Column(String(6, u'Chinese_PRC_CI_AS'))


t_CurComputer = Table(
    'CurComputer', metadata,
    Column('IP', String(20, u'Chinese_PRC_CI_AS')),
    Column('ComputerName', String(50, u'Chinese_PRC_CI_AS')),
    Column('UserID', Integer),
    Column('UserName', String(20, u'Chinese_PRC_CI_AS')),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS'))
)


class DBFILERECORD(Base):
    __tablename__ = 'DB_FILE_RECORD'

    ID = Column(Integer, primary_key=True)
    FILETABLENAME = Column(String(40, u'Chinese_PRC_CI_AS'))
    FILETABLEID = Column(Integer)
    LABDOC_ID = Column(Integer)
    SRCFILENAME = Column(String(250, u'Chinese_PRC_CI_AS'))
    HOSTNAME = Column(String(40, u'Chinese_PRC_CI_AS'))
    USERID = Column(String(20, u'Chinese_PRC_CI_AS'))
    USERNAME = Column(String(40, u'Chinese_PRC_CI_AS'))
    MODIFYTIME = Column(DateTime)


class DBFILESTORAGE(Base):
    __tablename__ = 'DB_FILE_STORAGE'

    LABDOC_ID = Column(Integer, primary_key=True)
    DIR_ID = Column(Integer)
    FILE_IMAGE = Column(LargeBinary)
    FILE_NAME = Column(String(250, u'Chinese_PRC_CI_AS'), nullable=False)
    STOREDTIME = Column(DateTime)


class Dept(Base):
    __tablename__ = 'Dept'

    DeptNo = Column(String(12, u'Chinese_PRC_CI_AS'), primary_key=True)
    DeptName = Column(String(50, u'Chinese_PRC_CI_AS'))
    ExternCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    DeptType = Column(String(1, u'Chinese_PRC_CI_AS'))
    DeptClass = Column(Integer)
    Parent = Column(String(12, u'Chinese_PRC_CI_AS'))
    MemCode1 = Column(String(8, u'Chinese_PRC_CI_AS'))
    MemCode2 = Column(String(8, u'Chinese_PRC_CI_AS'))
    ExHospFlag = Column(String(1, u'Chinese_PRC_CI_AS'))


t_EFilm_Handling_Task = Table(
    'EFilm_Handling_Task', metadata,
    Column('ApplyNo', Integer),
    Column('StudyUID', String(128, u'Chinese_PRC_CI_AS'), index=True),
    Column('PrintStat', Integer, server_default=text("((0))")),
    Column('ModifyTime', DateTime, nullable=False, server_default=text("(getdate())")),
    Column('NeedEFilm', Integer, nullable=False, server_default=text("((1))")),
    Column('HttpStat', Integer, nullable=False, server_default=text("((0))")),
    Column('HttpJson', String(4000, u'Chinese_PRC_CI_AS')),
    Column('InsertTime', DateTime, nullable=False, server_default=text("(getdate())"))
)


class EquipmentInfo(Base):
    __tablename__ = 'EquipmentInfo'

    EquipMentID = Column(Integer, primary_key=True)
    EquipmentName = Column(String(50, u'Chinese_PRC_CI_AS'))
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    DeptNo = Column(String(12, u'Chinese_PRC_CI_AS'))
    duplex_flag = Column(Numeric(5, 0))
    dilute_flag = Column(String(1, u'Chinese_PRC_CI_AS'))
    autoin_flag = Column(String(1, u'Chinese_PRC_CI_AS'))
    comm_port = Column(String(6, u'Chinese_PRC_CI_AS'))
    baud_rate = Column(Numeric(10, 0))
    byte_size = Column(Numeric(5, 0))
    parity = Column(Numeric(5, 0))
    stop_bits = Column(Numeric(5, 0))
    f_outx = Column(Numeric(5, 0))
    f_inx = Column(Numeric(5, 0))
    f_hardware = Column(Numeric(5, 0))
    tx_queuesize = Column(Numeric(10, 0))
    rx_queuesize = Column(Numeric(10, 0))
    xoff_lim = Column(Numeric(10, 0))
    xon_char = Column(String(1, u'Chinese_PRC_CI_AS'))
    xoff_char = Column(String(1, u'Chinese_PRC_CI_AS'))
    error_char = Column(String(1, u'Chinese_PRC_CI_AS'))
    event_char = Column(String(1, u'Chinese_PRC_CI_AS'))
    driver_prog = Column(String(128, u'Chinese_PRC_CI_AS'))
    serve_status = Column(String(1, u'Chinese_PRC_CI_AS'))
    item_type = Column(String(1, u'Chinese_PRC_CI_AS'))
    xon_lim = Column(Numeric(10, 0))
    priority = Column(Numeric(5, 0))
    description = Column(String(40, u'Chinese_PRC_CI_AS'))
    connect_date = Column(DateTime)
    auto_load = Column(Numeric(5, 0))
    qc1 = Column(Integer)
    qc2 = Column(Integer)
    qc3 = Column(Integer)
    fromname = Column(String(50, u'Chinese_PRC_CI_AS'))
    computername = Column(String(50, u'Chinese_PRC_CI_AS'))
    BuyTime = Column(DateTime)
    InstrPrice = Column(Numeric(12, 2))
    LimitTime = Column(Numeric(6, 2))
    BuyCompany = Column(String(100, u'Chinese_PRC_CI_AS'))
    RepairMethod = Column(String(100, u'Chinese_PRC_CI_AS'))
    factory = Column(String(40, u'Chinese_PRC_CI_AS'))
    ReportInstr = Column(Integer)
    SampleAdd = Column(Integer)
    TestSysID = Column(String(20, u'Chinese_PRC_CI_AS'))
    InDataType = Column(String(1, u'Chinese_PRC_CI_AS'))
    TestMethod = Column(String(50, u'Chinese_PRC_CI_AS'))
    Address = Column(String(50, u'Chinese_PRC_CI_AS'))
    QueueLength = Column(Integer)
    OnlineFlag = Column(String(1, u'Chinese_PRC_CI_AS'))
    AssignFlag = Column(String(1, u'Chinese_PRC_CI_AS'))
    WorkReport = Column(Integer)
    WorklistAgent = Column(String(50, u'Chinese_PRC_CI_AS'))
    Modality = Column(String(16, u'Chinese_PRC_CI_AS'))
    ATitle = Column(String(128, u'Chinese_PRC_CI_AS'))
    EquipmentPhoto = Column(LargeBinary)


class FILMFilmInfo(Base):
    __tablename__ = 'FILM_FilmInfo'

    FilmID = Column(Integer, primary_key=True)
    PatientID = Column(String(32, u'Chinese_PRC_CI_AS'))
    PatientName = Column(String(64, u'Chinese_PRC_CI_AS'))
    StudyDate = Column(String(8, u'Chinese_PRC_CI_AS'))
    StudyUID = Column(String(128, u'Chinese_PRC_CI_AS'), index=True)
    SeriesUID = Column(String(128, u'Chinese_PRC_CI_AS'), index=True)
    ImageUID = Column(String(128, u'Chinese_PRC_CI_AS'), index=True)
    ImageCount = Column(Integer)
    FilmRow = Column(Integer)
    FilmColumn = Column(Integer)
    FilmOrientation = Column(Integer)
    FilmSize = Column(String(32, u'Chinese_PRC_CI_AS'))
    FilmTrueWidth = Column(Integer)
    FilmTrueHeight = Column(Integer)
    FilmWidth = Column(Integer)
    FilmHeight = Column(Integer)
    MaxPrintWidth = Column(Integer)
    MaxPrintHeight = Column(Integer)
    RuleType = Column(Integer)
    ShowGrid = Column(Integer)
    PosOfImgInfo = Column(Integer)
    SizeOfImgInfo = Column(Integer)
    PageInfo = Column(String(2000, u'Chinese_PRC_CI_AS'))
    ShowPageInfo = Column(Integer)
    InvertPageInfo = Column(Integer)
    SizeOfPageInfo = Column(Integer)
    AddScout = Column(Integer)
    DoubleScout = Column(Integer)
    AddDrawAnn = Column(Integer)
    HasEFilm = Column(Integer, index=True)
    PrintTimes = Column(Integer, index=True)
    Source = Column(Integer, nullable=False)
    AccessionNO = Column(String(32, u'Chinese_PRC_CI_AS'), index=True)
    InsertDate = Column(DateTime, nullable=False)
    AddScoutSec = Column(Integer)
    ImageInter = Column(Integer)
    bEFilmDeleted = Column(Integer, server_default=text("(0)"))
    PrintedTime = Column(DateTime)
    FilmPlan = Column(String(50, u'Chinese_PRC_CI_AS'))
    RegularLayout = Column(Integer)
    UserID = Column(String(128, u'Chinese_PRC_CI_AS'))
    ApplyNO = Column(Integer)
    UpNum = Column(Integer)
    DownNum = Column(Integer)
    LeftNum = Column(Integer)
    RightNum = Column(Integer)
    FP_PlanName = Column(String(64, u'Chinese_PRC_CI_AS'))
    FP_FilmName = Column(String(64, u'Chinese_PRC_CI_AS'))
    FP_FilmType = Column(String(64, u'Chinese_PRC_CI_AS'))
    FP_Layout = Column(Integer)
    FP_Rows = Column(Integer)
    FP_Cols = Column(Integer)
    ModifyTime = Column(DateTime)
    copyname = Column(Integer)
    IsColorFilm = Column(Integer)


class FILMImagePrintedInfo(Base):
    __tablename__ = 'FILM_ImagePrintedInfo'
    __table_args__ = (
        Index('INDEX_FILM_IMAGEPRINTEDINFO_UIDS', 'StudyUID', 'SeriesUID', 'InstanceUID'),
    )

    ID_Num = Column(Integer, primary_key=True)
    FilmID = Column(Integer, nullable=False, index=True)
    InstanceUID = Column(String(128, u'Chinese_PRC_CI_AS'), nullable=False)
    SeriesUID = Column(String(128, u'Chinese_PRC_CI_AS'), nullable=False)
    StudyUID = Column(String(128, u'Chinese_PRC_CI_AS'), nullable=False)
    CurveType = Column(Integer, nullable=False)
    CurveGene = Column(Integer, nullable=False)
    WinLevel = Column(Integer, nullable=False)
    WinWidth = Column(Integer, nullable=False)
    IsRelativeZoom = Column(Integer)
    RelativeZoom = Column(Integer)
    ZoomPercent = Column(Integer)
    RelativeMoveX = Column(Integer)
    RelativeMoveY = Column(Integer)
    MoveX = Column(Integer, nullable=False)
    MoveY = Column(Integer, nullable=False)
    Intensity = Column(Integer, nullable=False)
    Contrast = Column(Integer, nullable=False)
    Gamma = Column(Integer, nullable=False)
    Inverse = Column(Integer)
    RotateAngle = Column(Integer, nullable=False)
    FlipStatus = Column(Integer, nullable=False)
    ClipRectX = Column(Integer)
    ClipRectY = Column(Integer)
    ClipRectWidth = Column(Integer)
    ClipRectHeight = Column(Integer)
    ImagePosition = Column(Integer, nullable=False)
    ImageSubPosition = Column(Integer, nullable=False)
    SubViewType = Column(Integer, nullable=False)
    Annotations = Column(String(6000, u'Chinese_PRC_CI_AS'))
    InsertDate = Column(DateTime, nullable=False)
    IsScoutImage = Column(Integer, nullable=False, server_default=text("(0)"))
    ShowScoutImage = Column(Integer)
    ScoutSeries = Column(String(128, u'Chinese_PRC_CI_AS'))
    ShowAnnotation = Column(Integer)
    LeftRightPos = Column(String(2, u'Chinese_PRC_CI_AS'))
    OffSetX = Column(Float(53))
    OffSetY = Column(Float(53))
    RoomID_Num = Column(Integer)


t_FILM_ImageUIDDeleted = Table(
    'FILM_ImageUIDDeleted', metadata,
    Column('ID_Num', Integer, nullable=False),
    Column('UserID', String(12, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ImageUID', String(128, u'Chinese_PRC_CI_AS'), nullable=False, index=True),
    Column('InsertTime', DateTime, nullable=False),
    Column('DealTime', DateTime),
    Column('DealID', Integer, nullable=False)
)


t_FILM_MakeNum = Table(
    'FILM_MakeNum', metadata,
    Column('UseName', String(20, u'Chinese_PRC_CI_AS')),
    Column('CurNum', Integer),
    Column('CurDate', DateTime)
)


class FILMStudyUIDSeriesUIDMapping(Base):
    __tablename__ = 'FILM_StudyUIDSeriesUIDMapping'

    StudyUID = Column(String(128, u'Chinese_PRC_CI_AS'), primary_key=True)
    SeriesUID = Column(String(128, u'Chinese_PRC_CI_AS'), nullable=False)
    ImageNo = Column(Integer)


t_FILM_UnRecogniseFilm = Table(
    'FILM_UnRecogniseFilm', metadata,
    Column('ID_NUM', Integer, nullable=False),
    Column('InsertTime', DateTime),
    Column('FullNetPath', String(512, u'Chinese_PRC_CI_AS')),
    Column('IpAddress', String(32, u'Chinese_PRC_CI_AS')),
    Column('Modality', String(32, u'Chinese_PRC_CI_AS')),
    Column('AETitle', String(64, u'Chinese_PRC_CI_AS')),
    Column('Status', String(64, u'Chinese_PRC_CI_AS'), index=True),
    Index('INDEX_FILM_UNRECOGNISEFILM', 'InsertTime', 'Modality', 'AETitle', 'Status')
)


t_FormatFilmInfoLog = Table(
    'FormatFilmInfoLog', metadata,
    Column('SerialNo', Numeric(18, 0), nullable=False),
    Column('LogTime', DateTime),
    Column('LogContent', String(2000, u'Chinese_PRC_CI_AS')),
    Column('LogUser', String(20, u'Chinese_PRC_CI_AS')),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS'))
)


class GroupRight(Base):
    __tablename__ = 'GroupRights'

    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    GroupName = Column(String(50, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    FuncCode = Column(String(50, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    Powers = Column(String(50, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)


class HOSPITALINFO(Base):
    __tablename__ = 'HOSPITALINFO'

    HOSPITALCODE = Column(String(50, u'Chinese_PRC_CI_AS'), primary_key=True)
    HOSPITALNAME = Column(String(100, u'Chinese_PRC_CI_AS'), nullable=False)
    HOSPITALURL = Column(String(200, u'Chinese_PRC_CI_AS'))
    HOSPITALTYPE = Column(String(100, u'Chinese_PRC_CI_AS'))
    HOSPITALLEVEL = Column(String(100, u'Chinese_PRC_CI_AS'))
    AREA = Column(String(100, u'Chinese_PRC_CI_AS'))
    PARENTCODE = Column(String(50, u'Chinese_PRC_CI_AS'))
    VISIBLE = Column(Integer, nullable=False)
    HOSPHISURL = Column(String(200, u'Chinese_PRC_CI_AS'))
    HOSPSHORTNAME = Column(String(20, u'Chinese_PRC_CI_AS'))
    HOSPSHORTCODE = Column(String(2, u'Chinese_PRC_CI_AS'))
    DEALFLAG = Column(Integer)


class Helper(Base):
    __tablename__ = 'Helper'

    SerialNo = Column(Integer, primary_key=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    PageCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    PageName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ParentID = Column(Integer)
    OrderNo = Column(Integer)
    RTFText = Column(LargeBinary)


class InstConfigDic(Base):
    __tablename__ = 'InstConfigDic'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    InstID = Column(Integer)
    ItemName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ItemValue = Column(String(500, u'Chinese_PRC_CI_AS'))
    ValueType = Column(String(1, u'Chinese_PRC_CI_AS'))
    Visible = Column(Integer, server_default=text("(1)"))


class InstRelateEquip(Base):
    __tablename__ = 'InstRelateEquip'

    InstID = Column(Integer, primary_key=True, nullable=False)
    EquipMentID = Column(Integer, primary_key=True, nullable=False)
    EnableAssign = Column(Integer, server_default=text("(0)"))


class InstRelateTemplate(Base):
    __tablename__ = 'InstRelateTemplate'

    InstID = Column(Integer, primary_key=True, nullable=False)
    LibraryID = Column(Integer, primary_key=True, nullable=False)


class Instrument(Base):
    __tablename__ = 'Instrument'

    InstID = Column(Integer, primary_key=True)
    InstCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    InstName = Column(String(40, u'Chinese_PRC_CI_AS'))
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    ExamCode = Column(Integer)
    GraphFlag = Column(String(1, u'Chinese_PRC_CI_AS'))
    ExecDept = Column(String(12, u'Chinese_PRC_CI_AS'))
    Modality = Column(String(100, u'Chinese_PRC_CI_AS'))
    hospitalcode = Column(String(50, u'Chinese_PRC_CI_AS'), server_default=text("('0000')"))
    hospcode = Column(String(50, u'Chinese_PRC_CI_AS'), server_default=text("('0000')"))


class LABMMCTreeViewConfig(Base):
    __tablename__ = 'LAB_MMCTreeViewConfig'

    TV_ID = Column(Integer, primary_key=True)
    TV_Name = Column(String(100, u'Chinese_PRC_CI_AS'))
    Parent = Column(Integer)
    InitTree = Column(Integer)
    DetailFlag = Column(Integer)
    DetailDLL = Column(String(100, u'Chinese_PRC_CI_AS'))
    MenuDLL = Column(String(100, u'Chinese_PRC_CI_AS'))
    OrderNo = Column(Integer)
    Icon = Column(String(255, u'Chinese_PRC_CI_AS'))


class LABSTAFF(Base):
    __tablename__ = 'LAB_STAFF'

    USERID = Column(String(12, u'Chinese_PRC_CI_AS'), primary_key=True)
    STAFFID = Column(String(12, u'Chinese_PRC_CI_AS'))
    ABO = Column(String(8, u'Chinese_PRC_CI_AS'))
    RH_D = Column(String(8, u'Chinese_PRC_CI_AS'))
    BIRTHDAY = Column(DateTime)
    NATIVEPLACE = Column(String(60, u'Chinese_PRC_CI_AS'))
    REGRESIDENCE = Column(String(20, u'Chinese_PRC_CI_AS'))
    GENDER = Column(String(4, u'Chinese_PRC_CI_AS'))
    NATIONALITY = Column(String(20, u'Chinese_PRC_CI_AS'))
    FAITH = Column(String(40, u'Chinese_PRC_CI_AS'))
    CLAN = Column(String(20, u'Chinese_PRC_CI_AS'))
    IDCARD = Column(String(20, u'Chinese_PRC_CI_AS'))
    MARITALSTATUS = Column(String(8, u'Chinese_PRC_CI_AS'))
    ALMAMATER = Column(String(40, u'Chinese_PRC_CI_AS'))
    CLASSDAY = Column(DateTime)
    DEGREE = Column(String(20, u'Chinese_PRC_CI_AS'))
    FOREIGNLANGUAGE = Column(String(20, u'Chinese_PRC_CI_AS'))
    PHOTO = Column(LargeBinary)
    SIGNATURE = Column(LargeBinary)
    RESIDENCE = Column(String(200, u'Chinese_PRC_CI_AS'))
    POSTCODE = Column(String(10, u'Chinese_PRC_CI_AS'))
    TEL = Column(String(20, u'Chinese_PRC_CI_AS'))
    MOBILE = Column(String(20, u'Chinese_PRC_CI_AS'))
    FAX = Column(String(20, u'Chinese_PRC_CI_AS'))
    EMAIL = Column(String(20, u'Chinese_PRC_CI_AS'))
    EMERGENCYPERSON = Column(String(20, u'Chinese_PRC_CI_AS'))
    EMERGENCYPHONE = Column(String(20, u'Chinese_PRC_CI_AS'))
    TITLE = Column(String(20, u'Chinese_PRC_CI_AS'))
    HEADSHIP = Column(String(20, u'Chinese_PRC_CI_AS'))
    JOINDATE = Column(DateTime)
    MEMO = Column(String(20, u'Chinese_PRC_CI_AS'))
    ACHROMAT = Column(String(20, u'Chinese_PRC_CI_AS'))


class LISInstOrder(Base):
    __tablename__ = 'LIS_InstOrder'

    InstID = Column(Integer, primary_key=True, nullable=False)
    HisOrderCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    HisOrderName = Column(String(50, u'Chinese_PRC_CI_AS'))
    ItemType = Column(String(1, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)


class LISOrderToItem(Base):
    __tablename__ = 'LIS_OrderToItem'

    HisOrderCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ItemCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    HisOrderName = Column(String(50, u'Chinese_PRC_CI_AS'))
    ChargeOrder = Column(Integer)


class LabList(Base):
    __tablename__ = 'Lab_List'

    Tv_Id = Column(Integer, primary_key=True)
    Tv_Name = Column(String(50, u'Chinese_PRC_CI_AS'))
    DocType = Column(String(100, u'Chinese_PRC_CI_AS'))


class LisInstGroupOrder(Base):
    __tablename__ = 'Lis_InstGroupOrder'

    InstID = Column(Integer, primary_key=True, nullable=False)
    GroupCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    GroupName = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    MemCode1 = Column(String(20, u'Chinese_PRC_CI_AS'))
    MemCode2 = Column(String(20, u'Chinese_PRC_CI_AS'))
    HisOrderCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ItemType = Column(String(1, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemQty = Column(Numeric(8, 2))


class Lock(Base):
    __tablename__ = 'Locks'

    SerialNo = Column(Integer, primary_key=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    HostName = Column(String(50, u'Chinese_PRC_CI_AS'))
    UserID = Column(String(12, u'Chinese_PRC_CI_AS'))
    FuncCode = Column(String(50, u'Chinese_PRC_CI_AS'))
    TableName = Column(String(50, u'Chinese_PRC_CI_AS'))
    KeyValue = Column(String(100, u'Chinese_PRC_CI_AS'))


class MailInfo(Base):
    __tablename__ = 'MailInfo'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    MailType = Column(String(1, u'Chinese_PRC_CI_AS'))
    MailTitle = Column(String(50, u'Chinese_PRC_CI_AS'))
    MailContent = Column(String(1000, u'Chinese_PRC_CI_AS'))
    ReceiverID = Column(String(20, u'Chinese_PRC_CI_AS'))
    ReceiverName = Column(String(20, u'Chinese_PRC_CI_AS'))
    SenderID = Column(String(20, u'Chinese_PRC_CI_AS'))
    SenderName = Column(String(20, u'Chinese_PRC_CI_AS'))
    MailStatus = Column(String(1, u'Chinese_PRC_CI_AS'))
    MailFlag = Column(String(1, u'Chinese_PRC_CI_AS'))
    SendTime = Column(DateTime)
    ReceiverDel = Column(String(1, u'Chinese_PRC_CI_AS'))
    SenderDel = Column(String(1, u'Chinese_PRC_CI_AS'))


t_MakeNum = Table(
    'MakeNum', metadata,
    Column('UseName', String(40, u'Chinese_PRC_CI_AS')),
    Column('CurNum', Integer),
    Column('CurDate', DateTime)
)


class MsgFlowDic(Base):
    __tablename__ = 'MsgFlowDic'

    PKey = Column(Integer, primary_key=True)
    FromType = Column(String(1, u'Chinese_PRC_CI_AS'))
    FromName = Column(String(40, u'Chinese_PRC_CI_AS'))
    ToType = Column(String(1, u'Chinese_PRC_CI_AS'))
    ToName = Column(String(40, u'Chinese_PRC_CI_AS'))
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))


t_MsgLog = Table(
    'MsgLog', metadata,
    Column('FUser', String(20, u'Chinese_PRC_CI_AS')),
    Column('FModule', String(30, u'Chinese_PRC_CI_AS')),
    Column('MID', Integer),
    Column('ToIP', String(20, u'Chinese_PRC_CI_AS')),
    Column('ToPort', Integer),
    Column('ToUser', String(20, u'Chinese_PRC_CI_AS')),
    Column('ToModule', String(30, u'Chinese_PRC_CI_AS')),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('FSubSysCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('MsgType', Integer),
    Column('MContent', String(2048, u'Chinese_PRC_CI_AS'))
)


t_PACS_ExamineInfo = Table(
    'PACS_ExamineInfo', metadata,
    Column('ID', Integer, nullable=False),
    Column('Host', String(64, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('IP', String(64, u'Chinese_PRC_CI_AS')),
    Column('CheckType', String(64, u'Chinese_PRC_CI_AS'), nullable=False, index=True),
    Column('CheckModule', String(64, u'Chinese_PRC_CI_AS'), nullable=False, index=True),
    Column('ServiceName', String(64, u'Chinese_PRC_CI_AS')),
    Column('ServerStatus', Integer),
    Column('SpaceTotal', Float(53)),
    Column('SpaceLeft', Float(53)),
    Column('ImageCountInCheckTime', Integer, index=True),
    Column('ImageSizeInCheckTime', Float(53), index=True),
    Column('TimesInCheckTime', Integer, index=True),
    Column('Reserve1', String(64, u'Chinese_PRC_CI_AS')),
    Column('Reserve2', String(64, u'Chinese_PRC_CI_AS')),
    Column('Reserve3', String(64, u'Chinese_PRC_CI_AS')),
    Column('Reserve4', String(64, u'Chinese_PRC_CI_AS')),
    Column('Reserve5', String(64, u'Chinese_PRC_CI_AS')),
    Column('CheckTime', DateTime, nullable=False, index=True)
)


class PACSIFRule(Base):
    __tablename__ = 'PACS_IFRule'

    RuleID = Column(Integer, primary_key=True)
    ConditionID = Column(Integer, nullable=False)
    RuleName = Column(String(128, u'Chinese_PRC_CI_AS'))
    RuleDesc = Column(String(128, u'Chinese_PRC_CI_AS'))
    computerID = Column(Integer, nullable=False)
    RuleStatus = Column(Integer)
    inserttime = Column(DateTime)
    Target = Column(String(128, u'Chinese_PRC_CI_AS'), nullable=False)
    modifytime = Column(DateTime)


t_PACS_TA6_Service = Table(
    'PACS_TA6_Service', metadata,
    Column('ID_Num', Integer, nullable=False, index=True),
    Column('service_name', String(128, u'Chinese_PRC_CI_AS')),
    Column('host', String(128, u'Chinese_PRC_CI_AS')),
    Column('module', String(128, u'Chinese_PRC_CI_AS')),
    Column('property_name', String(128, u'Chinese_PRC_CI_AS')),
    Column('property_value', String(128, u'Chinese_PRC_CI_AS')),
    Column('datatype', String(128, u'Chinese_PRC_CI_AS'))
)


class PacsAETitle(Base):
    __tablename__ = 'Pacs_AETitle'

    AEID = Column(Integer, primary_key=True)
    AEName = Column(String(64, u'Chinese_PRC_CI_AS'), nullable=False)
    AEType = Column(String(32, u'Chinese_PRC_CI_AS'))
    AETitle = Column(String(16, u'Chinese_PRC_CI_AS'), nullable=False)
    IP = Column(String(32, u'Chinese_PRC_CI_AS'), nullable=False)
    Port = Column(Integer, nullable=False)
    AEDesc = Column(String(512, u'Chinese_PRC_CI_AS'))
    AEType_StorageSCU = Column(String(128, u'Chinese_PRC_CI_AS'))
    AEType_StorageSCP = Column(String(128, u'Chinese_PRC_CI_AS'))
    AEType_QRSCU = Column(String(128, u'Chinese_PRC_CI_AS'))
    AEType_QRSCP = Column(String(128, u'Chinese_PRC_CI_AS'))
    AEType_StorageCommitSCP = Column(String(128, u'Chinese_PRC_CI_AS'))


class PacsAllService(Base):
    __tablename__ = 'Pacs_AllService'

    ServiceID = Column(Integer, primary_key=True)
    ServiceName = Column(String(32, u'Chinese_PRC_CI_AS'), nullable=False)
    ServiceDispName = Column(String(64, u'Chinese_PRC_CI_AS'), nullable=False)
    ServiceDesc = Column(String(128, u'Chinese_PRC_CI_AS'))
    InstallParam = Column(String(64, u'Chinese_PRC_CI_AS'))
    Enabled = Column(Integer)
    FileName = Column(String(32, u'Chinese_PRC_CI_AS'), nullable=False)
    LogPrefix = Column(String(32, u'Chinese_PRC_CI_AS'), nullable=False)


class PacsBackupDiscInfo(Base):
    __tablename__ = 'Pacs_BackupDiscInfo'

    DiscID = Column(String(16, u'Chinese_PRC_CI_AS'), primary_key=True)
    PlanID = Column(Integer)
    JobID = Column(Integer)
    ComputerID = Column(Integer)
    BackupDesc = Column(String(64, u'Chinese_PRC_CI_AS'))
    BackupType = Column(Integer, nullable=False)
    BackupTime = Column(DateTime, nullable=False)
    CurrentSize = Column(Float(53), nullable=False)
    TempPath = Column(String(256, u'Chinese_PRC_CI_AS'))
    DiscStatus = Column(Integer, nullable=False)
    DeviceSize = Column(Float(53), nullable=False)
    BackupReport = Column(String(5000, u'Chinese_PRC_CI_AS'))


class PacsBackupDownloadSery(Base):
    __tablename__ = 'Pacs_BackupDownloadSeries'

    DiscID = Column(String(16, u'Chinese_PRC_CI_AS'), nullable=False)
    SeriesID = Column(Integer, primary_key=True)
    DownloadImageCount = Column(Integer, server_default=text("('0')"))
    DownloadTime = Column(DateTime)
    CompressionID = Column(Integer)
    TotalFileSize = Column(Float(53))
    VerifyFailCount = Column(Integer, nullable=False, server_default=text("(0)"))


class PacsBackupJob(Base):
    __tablename__ = 'Pacs_BackupJob'

    JobID = Column(Integer, primary_key=True)
    PlanID = Column(Integer, nullable=False)
    ScheduleID = Column(Integer, nullable=False)
    Status = Column(Integer)
    DeviceSize = Column(Float(53))
    ComputerID = Column(Integer)
    CreateTime = Column(DateTime, server_default=text("(getdate())"))
    BeginRunTime = Column(DateTime, server_default=text("(getdate())"))
    EndRunTime = Column(DateTime)


class PacsBackupModality(Base):
    __tablename__ = 'Pacs_BackupModality'

    PlanID = Column(Integer, primary_key=True, nullable=False)
    ModalityID = Column(Integer, primary_key=True, nullable=False)


class PacsBackupPlan(Base):
    __tablename__ = 'Pacs_BackupPlan'

    PlanID = Column(Integer, primary_key=True)
    PlanName = Column(String(64, u'Chinese_PRC_CI_AS'))
    CompressionID = Column(Integer)
    EndTime = Column(Integer, nullable=False)
    Enabled = Column(Integer)
    MaxDownloadDisc = Column(Integer)
    DeviceSize = Column(Float(53))
    ComputerID = Column(Integer, nullable=False)


t_Pacs_CadResult = Table(
    'Pacs_CadResult', metadata,
    Column('ID', Integer, nullable=False),
    Column('PatName', String(64, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('NoduleCount', Integer, nullable=False),
    Column('ImageNo', Integer, nullable=False),
    Column('TemplateIndex', Integer, nullable=False),
    Column('PositionX', Integer, nullable=False),
    Column('PositionY', Integer, nullable=False),
    Column('StudyUID', String(128, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('SeriesUID', String(128, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ImageUID', String(128, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('Diam', Integer, server_default=text("((0))"))
)


class PacsCancelImageLog(Base):
    __tablename__ = 'Pacs_CancelImageLog'

    CancelID = Column(Integer, primary_key=True)
    ImageID = Column(Integer, index=True)
    CancelTime = Column(DateTime, index=True, server_default=text("(getdate())"))
    UserID = Column(String(12, u'Chinese_PRC_CI_AS'), nullable=False, index=True)


class PacsCompression(Base):
    __tablename__ = 'Pacs_Compression'

    CompressionID = Column(Integer, primary_key=True)
    Type = Column(String(16, u'Chinese_PRC_CI_AS'), nullable=False)
    Quality = Column(Integer)
    CompressDesc = Column(String(128, u'Chinese_PRC_CI_AS'))


class PacsComputer(Base):
    __tablename__ = 'Pacs_Computer'

    ComputerID = Column(Integer, primary_key=True)
    ComputerName = Column(String(64, u'Chinese_PRC_CI_AS'))
    DeptNo = Column(String(12, u'Chinese_PRC_CI_AS'))
    Type = Column(Integer, nullable=False)
    HostName = Column(String(64, u'Chinese_PRC_CI_AS'), unique=True)
    IP = Column(String(15, u'Chinese_PRC_CI_AS'))
    GroupID = Column(Integer)
    ComputerDesc = Column(String(1024, u'Chinese_PRC_CI_AS'))
    MonitorFlag = Column(Integer)
    InsertTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyUserID = Column(String(12, u'Chinese_PRC_CI_AS'))
    State = Column(Integer)
    HospCode = Column(String(50, u'Chinese_PRC_CI_AS'), server_default=text("('0000')"))
    HospName = Column(String(50, u'Chinese_PRC_CI_AS'))
    DeptName = Column(String(50, u'Chinese_PRC_CI_AS'))


class PacsDownloadMonitor(Base):
    __tablename__ = 'Pacs_DownloadMonitor'

    MonitorID = Column(Integer, primary_key=True)
    ComputerName = Column(String(50, u'Chinese_PRC_CI_AS'))
    DownloadTime = Column(DateTime, index=True)
    ImageNum = Column(Integer)
    Modality = Column(String(50, u'Chinese_PRC_CI_AS'))


class PacsErrorCode(Base):
    __tablename__ = 'Pacs_ErrorCode'

    ErrorCode = Column(Integer, primary_key=True)
    Error = Column(String(128, u'Chinese_PRC_CI_AS'), nullable=False)


class PacsEstimateImage(Base):
    __tablename__ = 'Pacs_EstimateImages'
    __table_args__ = (
        Index('Pacs_EstimateImages_ID', 'EstimateID', 'ApplyNo', unique=True),
    )

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ApplyNo = Column(Integer, nullable=False, index=True)
    EstimateID = Column(Integer, nullable=False)
    EstimateFlag = Column(Integer, nullable=False)
    Grade = Column(String(10, u'Chinese_PRC_CI_AS'))
    Reason = Column(String(1000, u'Chinese_PRC_CI_AS'))
    Estimator = Column(String(10, u'Chinese_PRC_CI_AS'))
    EstimatorName = Column(String(50, u'Chinese_PRC_CI_AS'))
    EstimateTime = Column(DateTime, server_default=text("(getdate())"))


class PacsFilmList(Base):
    __tablename__ = 'Pacs_FilmList'

    FilmID = Column(Integer, primary_key=True)
    PrintTime = Column(DateTime)
    Pages = Column(Integer)
    Images = Column(Integer)
    Type = Column(Integer)
    FilmSize = Column(String(16, u'Chinese_PRC_CI_AS'))
    Orientation = Column(Integer)
    Printer = Column(String(32, u'Chinese_PRC_CI_AS'))
    UserID = Column(String(64, u'Chinese_PRC_CI_AS'))
    FilmDesc = Column(String(512, u'Chinese_PRC_CI_AS'))
    PrintCount = Column(Integer)


class PacsGroup(Base):
    __tablename__ = 'Pacs_Group'

    GroupID = Column(Integer, primary_key=True)
    GroupName = Column(String(64, u'Chinese_PRC_CI_AS'))
    GroupDesc = Column(String(128, u'Chinese_PRC_CI_AS'))
    RouteID = Column(Integer, nullable=False)
    InsertTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyUserID = Column(String(12, u'Chinese_PRC_CI_AS'))
    State = Column(Integer)


t_Pacs_HPInstance = Table(
    'Pacs_HPInstance', metadata,
    Column('ID', Integer, nullable=False),
    Column('nProtocolID', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ProtocolName', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ProtocolDateTime', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('DisplayMode', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('RelationToStu', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('RelationToSer', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('StudyDec', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('StudyCount', Integer, nullable=False),
    Column('SeriesCount', Integer, nullable=False),
    Column('ModalityInStudy', String(50, u'Chinese_PRC_CI_AS')),
    Column('DisplayScreen', Integer, nullable=False),
    Column('RoomMode', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('RoomOrder', Integer, nullable=False),
    Column('BodyPart', String(50, u'Chinese_PRC_CI_AS')),
    Column('ModalityInSeries', String(50, u'Chinese_PRC_CI_AS')),
    Column('ImageType', String(50, u'Chinese_PRC_CI_AS')),
    Column('PatientPosition', String(50, u'Chinese_PRC_CI_AS')),
    Column('SeriesDescription', String(50, u'Chinese_PRC_CI_AS')),
    Column('SeriesInstanceUID', String(50, u'Chinese_PRC_CI_AS')),
    Column('SeriesNumber', Integer),
    Column('StudyDescription', String(50, u'Chinese_PRC_CI_AS')),
    Column('StudyInstanceUID', String(50, u'Chinese_PRC_CI_AS')),
    Column('ViewPosition', String(50, u'Chinese_PRC_CI_AS')),
    Column('PriorImagesValue', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('WindowCenter', Integer, nullable=False),
    Column('WindowWidth', Integer, nullable=False),
    Column('Factor', Integer, nullable=False),
    Column('Annotatation', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('PatientOrientationR', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('PatientOrientationF', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ImageRow', Integer, nullable=False),
    Column('ImageColumn', Integer, nullable=False),
    Column('SortCriteria', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('SetWindowMode', String(50, u'Chinese_PRC_CI_AS')),
    Column('ZoomMode', String(50, u'Chinese_PRC_CI_AS'))
)


t_Pacs_HPInstanceEx = Table(
    'Pacs_HPInstanceEx', metadata,
    Column('ID', Integer, nullable=False),
    Column('nProtocolID', Integer, nullable=False),
    Column('ProtocolName', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ProtocolDateTime', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('DisplayMode', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('RelationToStu', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('RelationToSer', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('StudyDec', String(200, u'Chinese_PRC_CI_AS')),
    Column('StudyCount', Integer, nullable=False),
    Column('SeriesCount', Integer, nullable=False),
    Column('ModalityInStudy', String(50, u'Chinese_PRC_CI_AS')),
    Column('DisplayScreen', Integer, nullable=False),
    Column('RoomMode', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('RoomOrder', Integer, nullable=False),
    Column('ImageFilter', String(7000, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('WindowCenter', Integer, nullable=False),
    Column('WindowWidth', Integer, nullable=False),
    Column('Factor', Integer, nullable=False),
    Column('Annotatation', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('PatientOrientationR', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('PatientOrientationF', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ImageRow', Integer, nullable=False),
    Column('ImageColumn', Integer, nullable=False),
    Column('SortCriteria', Integer, nullable=False),
    Column('SetWindowMode', String(50, u'Chinese_PRC_CI_AS')),
    Column('ZoomMode', String(50, u'Chinese_PRC_CI_AS')),
    Column('OrderNo', Integer, nullable=False),
    Column('UserID', String(50, u'Chinese_PRC_CI_AS'))
)


class PacsImage(Base):
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


class PacsImageCondition(Base):
    __tablename__ = 'Pacs_ImageCondition'

    ConditionID = Column(Integer, primary_key=True)
    Name = Column(String(64, u'Chinese_PRC_CI_AS'))
    Condition = Column(String(5000, u'Chinese_PRC_CI_AS'), nullable=False)
    ConditionDesc = Column(String(1000, u'Chinese_PRC_CI_AS'))
    Type = Column(Integer)
    Enabled = Column(Integer, nullable=False)
    ModifyTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyUserID = Column(String(12, u'Chinese_PRC_CI_AS'))
    SqlType = Column(Integer, nullable=False)


t_Pacs_ImageDataflowIDs = Table(
    'Pacs_ImageDataflowIDs', metadata,
    Column('RunningID', Integer, nullable=False),
    Column('RuleID', Integer, nullable=False),
    Column('TaskSeriesID', Integer, nullable=False),
    Column('TaskSeriesCount', Integer, nullable=False),
    Column('CreateTime', DateTime, nullable=False),
    Column('ExecTime', DateTime, nullable=False)
)


class PacsImageJudgeInfo(Base):
    __tablename__ = 'Pacs_ImageJudgeInfo'

    ImageID = Column(Integer, primary_key=True)
    Quality = Column(Integer, server_default=text("(1)"))
    Context = Column(String(1000, u'Chinese_PRC_CI_AS'))


class PacsImagePrinted(Base):
    __tablename__ = 'Pacs_ImagePrinted'

    FilmID = Column(Integer, nullable=False, index=True)
    ImageID = Column(Integer, nullable=False, index=True)
    SeriesID = Column(Integer)
    StudyID = Column(Integer)
    ImageStatusID = Column(Integer)
    ImagePrintID = Column(Integer, primary_key=True)


class PacsInstance(Base):
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


class PacsLogin(Base):
    __tablename__ = 'Pacs_Login'

    LoginID = Column(Integer, primary_key=True)
    HostName = Column(String(64, u'Chinese_PRC_CI_AS'), index=True)
    IP = Column(String(15, u'Chinese_PRC_CI_AS'))
    SubSysCode = Column(String(8, u'Chinese_PRC_CI_AS'))
    LoginTime = Column(DateTime)
    LoginUser = Column(String(12, u'Chinese_PRC_CI_AS'))
    LogoutTime = Column(DateTime)
    Reserved1 = Column(String(256, u'Chinese_PRC_CI_AS'))
    Reserved2 = Column(String(256, u'Chinese_PRC_CI_AS'))


t_Pacs_MMCTreeViewConfig = Table(
    'Pacs_MMCTreeViewConfig', metadata,
    Column('TV_ID', Integer, nullable=False),
    Column('TV_Name', String(100, u'Chinese_PRC_CI_AS')),
    Column('Parent', Integer),
    Column('InitTree', Integer),
    Column('DetailFlag', Integer),
    Column('DetailDLL', String(100, u'Chinese_PRC_CI_AS')),
    Column('MenuDLL', String(100, u'Chinese_PRC_CI_AS')),
    Column('OrderNo', Integer),
    Column('Icon', String(255, u'Chinese_PRC_CI_AS')),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS'), nullable=False, server_default=text("('RadSuitePACS')"))
)


class PacsMakeNum(Base):
    __tablename__ = 'Pacs_MakeNum'

    NoName = Column(String(40, u'Chinese_PRC_CI_AS'), primary_key=True)
    CurrNo = Column(Integer)
    CurrDate = Column(DateTime)


class PacsModality(Base):
    __tablename__ = 'Pacs_Modality'

    ModalityID = Column(Integer, primary_key=True)
    ModalityName = Column(String(16, u'Chinese_PRC_CI_AS'), nullable=False)
    ModalityDesc = Column(String(64, u'Chinese_PRC_CI_AS'))
    ReportID = Column(Integer, nullable=False)


class PacsMonitor(Base):
    __tablename__ = 'Pacs_Monitor'

    MonitorID = Column(Integer, primary_key=True)
    Type = Column(Integer, nullable=False)
    ComputerID = Column(Integer)
    ImageID = Column(Integer, nullable=False)
    ImageFileSize = Column(Float(53), nullable=False)
    TimeBegin = Column(DateTime, nullable=False)
    TimeEnd = Column(DateTime)
    TotalTime = Column(Integer, nullable=False)
    ErrorFlag = Column(Integer, nullable=False)
    ErrorReason = Column(String(256, u'Chinese_PRC_CI_AS'))


class PacsMonitorInfo(Base):
    __tablename__ = 'Pacs_MonitorInfo'

    ID = Column(Integer, primary_key=True)
    Host = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    IP = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    HostType = Column(Integer, nullable=False)
    DicomSvrType = Column(String(50, u'Chinese_PRC_CI_AS'))
    DicomServiceStatus = Column(Integer, nullable=False, server_default=text("((-1))"))
    SpaceTotal = Column(Integer, nullable=False, server_default=text("((-1))"))
    SpaceLeft = Column(Integer, nullable=False, server_default=text("((-1))"))
    StoragePort = Column(Integer, nullable=False, server_default=text("((-1))"))
    IsStorageSvrAlive = Column(Integer, nullable=False, server_default=text("((-1))"))
    HttpPort = Column(Integer, nullable=False)
    MTime = Column(String(50, u'Chinese_PRC_CI_AS'), server_default=text("(CONVERT([varchar](30),getdate(),(20)))"))


t_Pacs_Operation = Table(
    'Pacs_Operation', metadata,
    Column('OpID', Integer, nullable=False),
    Column('GrpID', Integer, nullable=False, index=True),
    Column('ImageID', Integer, nullable=False),
    Column('WinLevel', Integer),
    Column('WinWidth', Integer),
    Column('Bright', Integer),
    Column('Contrast', Integer),
    Column('Inverse', Integer),
    Column('Zoom', Integer),
    Column('State', Integer),
    Column('Annotations', String(6000, u'Chinese_PRC_CI_AS')),
    Column('IsKey', Integer),
    Column('CreateTime', DateTime),
    Column('ModifyTime', DateTime),
    Column('IsPrinted', Integer)
)


class PacsPatIDPrefix(Base):
    __tablename__ = 'Pacs_PatID_Prefix'

    Modality = Column(String(16, u'Chinese_PRC_CI_AS'), primary_key=True)
    PatID_Prefix = Column(String(6, u'Chinese_PRC_CI_AS'))
    Prefix_Desc = Column(String(128, u'Chinese_PRC_CI_AS'))
    ModifyTime = Column(DateTime)


class PacsRoute(Base):
    __tablename__ = 'Pacs_Route'

    RouteID = Column(Integer, primary_key=True)
    RouteName = Column(String(64, u'Chinese_PRC_CI_AS'))
    IsDefault = Column(Integer)
    RouteDesc = Column(String(128, u'Chinese_PRC_CI_AS'))
    InsertTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyUserID = Column(String(12, u'Chinese_PRC_CI_AS'))
    State = Column(Integer)


class PacsRouteOrder(Base):
    __tablename__ = 'Pacs_RouteOrder'

    OrderID = Column(Integer, primary_key=True)
    OrderNo = Column(Integer, nullable=False)
    RouteID = Column(Integer, nullable=False)
    AccessID = Column(Integer, nullable=False)


class PacsRule(Base):
    __tablename__ = 'Pacs_Rule'

    RuleID = Column(Integer, primary_key=True)
    ConditionID = Column(Integer)
    RuleName = Column(String(64, u'Chinese_PRC_CI_AS'))
    RuleType = Column(Integer, nullable=False)
    VolumeID = Column(Integer, nullable=False)
    AccessID = Column(Integer, nullable=False)
    DefaultPriority = Column(Integer)
    CompressionID = Column(Integer)
    DeleteSource = Column(Integer)
    ComputerID = Column(Integer, nullable=False)
    EnableRunStart = Column(Integer)
    EnableRunEnd = Column(Integer)
    RuleStatus = Column(Integer, nullable=False)
    RuleDesc = Column(String(128, u'Chinese_PRC_CI_AS'))
    InsertTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyUserID = Column(String(12, u'Chinese_PRC_CI_AS'))
    State = Column(Integer)
    module = Column(String(128, u'Chinese_PRC_CI_AS'))


class PacsRuleDestVolume(Base):
    __tablename__ = 'Pacs_RuleDestVolume'

    RuleID = Column(Integer, primary_key=True, nullable=False)
    VolumeID = Column(Integer, primary_key=True, nullable=False)
    AccessID = Column(Integer, nullable=False)


class PacsSchedule(Base):
    __tablename__ = 'Pacs_Schedule'

    ScheduleID = Column(Integer, primary_key=True)
    RuleID = Column(Integer, nullable=False)
    ScheduleType = Column(Integer, nullable=False)
    ScheduleName = Column(String(128, u'Chinese_PRC_CI_AS'))
    Enabled = Column(Integer)
    Freq_Type = Column(Integer)
    Freq_Interval = Column(Integer)
    Freq_Subday_Type = Column(Integer)
    Freq_Subday_Interval = Column(Integer)
    Freq_Relative_Interval = Column(Integer)
    Freq_Recurrence_Factor = Column(Integer)
    Active_Start_Date = Column(Integer)
    Active_End_Date = Column(Integer)
    Active_Start_Time = Column(Integer)
    Active_End_Time = Column(Integer)
    Next_Run_Date = Column(Integer)
    Next_Run_Time = Column(Integer)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))


class PacsSery(Base):
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


class PacsService(Base):
    __tablename__ = 'Pacs_Service'

    ServiceID = Column(Integer, primary_key=True)
    ServiceName = Column(String(64, u'Chinese_PRC_CI_AS'), nullable=False)
    ComputerID = Column(Integer, nullable=False)
    ServiceStatus = Column(Integer)
    ServiceDesc = Column(String(128, u'Chinese_PRC_CI_AS'))
    ServiceIP = Column(String(15, u'Chinese_PRC_CI_AS'))
    ServicePort = Column(Integer)
    AETitle = Column(String(64, u'Chinese_PRC_CI_AS'))
    ActiveTime = Column(DateTime)


class PacsStudy(Base):
    __tablename__ = 'Pacs_Study'
    __table_args__ = (
        Index('IX_Pacs_Study_Hosp_AccessNo', 'AccessionNo', 'HospCode'),
        Index('IX_Pacs_Study_Hosp_Patid', 'PatID', 'HospCode'),
        Index('IX_Pacs_Study_Hosp_PatName', 'PatName', 'HospCode'),
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


class PacsSubTask(Base):
    __tablename__ = 'Pacs_SubTask'

    SubTaskID = Column(Integer, primary_key=True)
    TaskID = Column(Integer, nullable=False, index=True)
    InstanceID = Column(Integer, nullable=False, index=True)
    BeginTime = Column(DateTime)
    EndTime = Column(DateTime)
    ErrorReason = Column(String(256, u'Chinese_PRC_CI_AS'))
    ExecStatus = Column(Integer, nullable=False)


class PacsSwapPatIDAndName(Base):
    __tablename__ = 'Pacs_SwapPatIDAndName'

    Modality = Column(String(16, u'Chinese_PRC_CI_AS'), primary_key=True)
    IsSwap = Column(Integer)
    Note = Column(String(256, u'Chinese_PRC_CI_AS'))


class PacsSysDict(Base):
    __tablename__ = 'Pacs_SysDict'

    TableName = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    FieldName = Column(String(64, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    nValue = Column(Integer, primary_key=True, nullable=False)
    cValue = Column(String(256, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    Note = Column(String(256, u'Chinese_PRC_CI_AS'))


class PacsTask(Base):
    __tablename__ = 'Pacs_Task'

    TaskID = Column(Integer, primary_key=True)
    RuleID = Column(Integer, nullable=False)
    ConditionID = Column(Integer, nullable=False)
    TaskName = Column(String(64, u'Chinese_PRC_CI_AS'))
    TaskType = Column(Integer, nullable=False)
    VolumeID = Column(Integer, nullable=False)
    AccessID = Column(Integer, nullable=False)
    Priority = Column(Integer)
    CompressionID = Column(Integer)
    DeleteSource = Column(Integer)
    ComputerID = Column(Integer, nullable=False)
    EnableRunStart = Column(Integer)
    EnableRunEnd = Column(Integer)
    ExecStatus = Column(Integer, nullable=False)
    BeginTime = Column(DateTime)
    EndTime = Column(DateTime)
    ExecDesc = Column(String(512, u'Chinese_PRC_CI_AS'))
    SubTaskCount = Column(Integer, server_default=text("(0)"))
    ScheduleID = Column(Integer)


class PacsTaskDestVolume(Base):
    __tablename__ = 'Pacs_TaskDestVolume'

    TaskID = Column(Integer, primary_key=True, nullable=False)
    VolumeID = Column(Integer, primary_key=True, nullable=False)
    AccessID = Column(Integer, nullable=False)


class PacsViewSetting(Base):
    __tablename__ = 'Pacs_ViewSettings'
    __table_args__ = (
        Index('idx_PACS_ViewSettings_MuliInd', 'SubSysCode', 'Domain', 'DomainName', 'Section', 'GroupName', 'Entry', 'HospCode', unique=True),
    )

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    Domain = Column(Integer, nullable=False)
    DomainName = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    Section = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    GroupName = Column(String(20, u'Chinese_PRC_CI_AS'))
    Entry = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    DataType = Column(String(20, u'Chinese_PRC_CI_AS'))
    Value = Column(String(7000, u'Chinese_PRC_CI_AS'))
    Visible = Column(Integer, nullable=False)
    Comment = Column(String(250, u'Chinese_PRC_CI_AS'))
    HospCode = Column(String(50, u'Chinese_PRC_CI_AS'), server_default=text("('0000')"))


class PacsViewTag(Base):
    __tablename__ = 'Pacs_ViewTag'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    Modality = Column(String(16, u'Chinese_PRC_CI_AS'), nullable=False)
    GroupNum = Column(String(4, u'Chinese_PRC_CI_AS'), nullable=False)
    ElementNum = Column(String(4, u'Chinese_PRC_CI_AS'), nullable=False)
    TagDesc = Column(String(64, u'Chinese_PRC_CI_AS'), nullable=False, server_default=text("('')"))


class PacsVolume(Base):
    __tablename__ = 'Pacs_Volume'

    VolumeID = Column(Integer, primary_key=True)
    Label = Column(String(64, u'Chinese_PRC_CI_AS'))
    LocalPath = Column(String(256, u'Chinese_PRC_CI_AS'))
    DefaultAccessID = Column(Integer)
    VolumeDesc = Column(String(128, u'Chinese_PRC_CI_AS'))
    DeptNo = Column(String(12, u'Chinese_PRC_CI_AS'))
    ComputerID = Column(Integer)
    SpaceLimit = Column(Integer)
    SpaceUsed = Column(Float(53), server_default=text("(0.0)"))
    SpaceTotal = Column(Float(53))
    VolumeType = Column(Integer)
    MonitorFlag = Column(Integer, server_default=text("(0)"))
    Online = Column(Integer, server_default=text("(1)"))
    VolumeStatus = Column(Integer, server_default=text("(1)"))
    InsertTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyUserID = Column(String(12, u'Chinese_PRC_CI_AS'))
    State = Column(Integer)
    SubNode = Column(String(20, u'Chinese_PRC_CI_AS'))


class PacsVolumeAcces(Base):
    __tablename__ = 'Pacs_VolumeAccess'

    AccessID = Column(Integer, primary_key=True)
    VolumeID = Column(Integer, nullable=False)
    AccessType = Column(Integer, nullable=False)
    RemotePath = Column(String(256, u'Chinese_PRC_CI_AS'))
    Host = Column(String(64, u'Chinese_PRC_CI_AS'))
    IP = Column(String(80, u'Chinese_PRC_CI_AS'))
    Port = Column(Integer)
    UserName = Column(String(64, u'Chinese_PRC_CI_AS'))
    UserPassword = Column(String(64, u'Chinese_PRC_CI_AS'))
    AccessDesc = Column(String(128, u'Chinese_PRC_CI_AS'))
    InsertTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyTime = Column(DateTime, server_default=text("(getdate())"))
    ModifyUserID = Column(String(12, u'Chinese_PRC_CI_AS'))


class PacsWithRI(Base):
    __tablename__ = 'Pacs_WithRIS'

    TAG = Column(String(64, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    Value = Column(String(64, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    PacsField = Column(String(64, u'Chinese_PRC_CI_AS'))
    RisField = Column(String(64, u'Chinese_PRC_CI_AS'))
    Note = Column(String(64, u'Chinese_PRC_CI_AS'))


t_Pacs_t_Schedule = Table(
    'Pacs_t_Schedule', metadata,
    Column('ScheduleID', Integer),
    Column('RuleID', Integer),
    Column('ScheduleType', Integer),
    Column('SubSysCode', Integer),
    Column('ComputerID', Integer, index=True)
)


class PatTechNo(Base):
    __tablename__ = 'PatTechNo'
    __table_args__ = (
        Index('idx_PatTechNo_TechNo', 'ReportID', 'TechNo'),
        Index('idx_PatTechNo_TechPatID', 'ReportID', 'TechNo')
    )

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    TechPatID = Column(Integer, nullable=False)
    ReportID = Column(Integer, nullable=False)
    TechNo = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    LastUseDate = Column(DateTime)


class PatientInfo(Base):
    __tablename__ = 'PatientInfo'

    TechPatID = Column(Integer, primary_key=True)
    PatName = Column(String(40, u'Chinese_PRC_CI_AS'), index=True)
    PatNameSpell = Column(String(40, u'Chinese_PRC_CI_AS'))
    PatientID = Column(Integer, index=True)
    CureNo = Column(Integer, index=True)
    CardNo = Column(String(30, u'Chinese_PRC_CI_AS'), index=True)
    DiagNo = Column(String(16, u'Chinese_PRC_CI_AS'), index=True)
    HospNo = Column(String(20, u'Chinese_PRC_CI_AS'), index=True)
    Sex = Column(String(16, u'Chinese_PRC_CI_AS'))
    Age = Column(Numeric(5, 2))
    AgeUnit = Column(String(6, u'Chinese_PRC_CI_AS'))
    BirthDay = Column(DateTime)
    Career = Column(String(30, u'Chinese_PRC_CI_AS'))
    Phone = Column(String(20, u'Chinese_PRC_CI_AS'))
    Address = Column(String(100, u'Chinese_PRC_CI_AS'))
    ZIP = Column(String(6, u'Chinese_PRC_CI_AS'))
    Nation = Column(String(20, u'Chinese_PRC_CI_AS'))
    IDNum = Column(String(20, u'Chinese_PRC_CI_AS'))
    EngName = Column(String(100, u'Chinese_PRC_CI_AS'))


class PinYinCode(Base):
    __tablename__ = 'PinYinCode'

    UnicodeID = Column(Integer, primary_key=True)
    ChineseChar = Column(String(2, u'Chinese_PRC_CI_AS'), nullable=False)
    PinYin = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)


class PrintBarCode(Base):
    __tablename__ = 'PrintBarCode'

    SerialNo = Column(Integer, primary_key=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    PrintDate = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    PrePart = Column(String(20, u'Chinese_PRC_CI_AS'))
    BackPart = Column(String(20, u'Chinese_PRC_CI_AS'))
    BegNum = Column(Integer, nullable=False)
    EndNum = Column(Integer, nullable=False)
    ZeroLen = Column(Integer)
    PrintDocCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    PrintDocName = Column(String(20, u'Chinese_PRC_CI_AS'))


t_QrStudyUid = Table(
    'QrStudyUid', metadata,
    Column('sNo', Integer, nullable=False),
    Column('StudyUid', String(128, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('Status', String(10, u'Chinese_PRC_CI_AS'))
)


class QueryCondition(Base):
    __tablename__ = 'QueryCondition'

    TableDesc = Column(String(30, u'Chinese_PRC_CI_AS'), nullable=False)
    TableName = Column(String(30, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    TableType = Column(String(1, u'Chinese_PRC_CI_AS'), nullable=False)
    FieldDesc = Column(String(30, u'Chinese_PRC_CI_AS'), nullable=False)
    FieldName = Column(String(30, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ConField1 = Column(String(30, u'Chinese_PRC_CI_AS'))
    ConName1 = Column(String(30, u'Chinese_PRC_CI_AS'))
    ConField2 = Column(String(30, u'Chinese_PRC_CI_AS'))
    ConName2 = Column(String(30, u'Chinese_PRC_CI_AS'))
    InputType = Column(String(20, u'Chinese_PRC_CI_AS'))
    DefaultValue = Column(String(20, u'Chinese_PRC_CI_AS'))
    DefaultRela = Column(String(20, u'Chinese_PRC_CI_AS'))
    UseRelation = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    InputSQL = Column(String(1000, u'Chinese_PRC_CI_AS'))
    DispOrder = Column(Integer)
    IsText = Column(Integer, server_default=text("(0)"))


class RISAcceptItem(Base):
    __tablename__ = 'RIS_AcceptItems'
    __table_args__ = (
        Index('idx_Ris_AcceptItems_ReceiveTime', 'ApplyNo', 'ReceiveTime'),
        Index('idx_Ris_AcceptItems_ItemCode', 'ApplyNo', 'ItemCode')
    )

    SerialNo = Column(Integer, primary_key=True)
    ApplyNo = Column(Integer, nullable=False, index=True)
    HISApplyNo = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'))
    Price = Column(MONEY)
    Price2 = Column(MONEY)
    ItemQty = Column(Numeric(8, 2))
    ReceiveTime = Column(DateTime)
    OperatorCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    OperatorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    Status = Column(String(1, u'Chinese_PRC_CI_AS'))
    GroupNo = Column(String(20, u'Chinese_PRC_CI_AS'))
    LogNo = Column(String(20, u'Chinese_PRC_CI_AS'))
    ApplyDocCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    ApplyDept = Column(String(20, u'Chinese_PRC_CI_AS'))
    ExecDept = Column(String(20, u'Chinese_PRC_CI_AS'))
    ApplyTime = Column(DateTime)
    ItemUnit = Column(String(20, u'Chinese_PRC_CI_AS'))
    AddType = Column(String(1, u'Chinese_PRC_CI_AS'))
    ItemType = Column(String(1, u'Chinese_PRC_CI_AS'))
    ChargeFlag = Column(String(1, u'Chinese_PRC_CI_AS'))
    Content = Column(String(200, u'Chinese_PRC_CI_AS'))
    ghxh = Column(String(30, u'Chinese_PRC_CI_AS'))
    ChargeType = Column(String(50, u'Chinese_PRC_CI_AS'))
    ChargeTypeDesc = Column(String(50, u'Chinese_PRC_CI_AS'))


class RISAcceptItemsHistory(Base):
    __tablename__ = 'RIS_AcceptItems_History'
    __table_args__ = (
        Index('idx_Ris_AcceptItems_History_ItemCode', 'ApplyNo', 'ItemCode'),
        Index('idx_Ris_AcceptItems_History_ReceiveTime', 'ApplyNo', 'ReceiveTime')
    )

    SerialNo = Column(Integer, primary_key=True)
    ApplyNo = Column(Integer, nullable=False)
    HISApplyNo = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'))
    Price = Column(MONEY)
    Price2 = Column(MONEY)
    ItemQty = Column(Numeric(8, 2))
    ReceiveTime = Column(DateTime)
    OperatorCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    OperatorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    Status = Column(String(1, u'Chinese_PRC_CI_AS'))
    GroupNo = Column(String(20, u'Chinese_PRC_CI_AS'))
    LogNo = Column(String(20, u'Chinese_PRC_CI_AS'))
    ApplyDocCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    ApplyDept = Column(String(20, u'Chinese_PRC_CI_AS'))
    ExecDept = Column(String(20, u'Chinese_PRC_CI_AS'))
    ApplyTime = Column(DateTime)
    ItemUnit = Column(String(20, u'Chinese_PRC_CI_AS'))
    AddType = Column(String(1, u'Chinese_PRC_CI_AS'))
    ItemType = Column(String(1, u'Chinese_PRC_CI_AS'))
    ChargeFlag = Column(String(1, u'Chinese_PRC_CI_AS'))
    Content = Column(String(200, u'Chinese_PRC_CI_AS'))
    ghxh = Column(String(30, u'Chinese_PRC_CI_AS'))
    ChargeType = Column(String(50, u'Chinese_PRC_CI_AS'))
    ChargeTypeDesc = Column(String(50, u'Chinese_PRC_CI_AS'))


class RISAttention(Base):
    __tablename__ = 'RIS_Attention'

    ReportID = Column(Integer, primary_key=True, nullable=False)
    AttentionCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ATitle = Column(String(50, u'Chinese_PRC_CI_AS'))
    AContent = Column(String(2000, u'Chinese_PRC_CI_AS'))


class RISBookingInfo(Base):
    __tablename__ = 'RIS_BookingInfo'

    ApplyNo = Column(Integer, primary_key=True, index=True)
    RegisterCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    RegisterName = Column(String(20, u'Chinese_PRC_CI_AS'))
    AttentionCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    BookNo = Column(Integer)
    DSID = Column(Integer)


class RISBookingInfoHistory(Base):
    __tablename__ = 'RIS_BookingInfo_History'

    ApplyNo = Column(Integer, primary_key=True, index=True)
    RegisterCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    RegisterName = Column(String(20, u'Chinese_PRC_CI_AS'))
    AttentionCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    BookNo = Column(Integer)
    DSID = Column(Integer)


t_RIS_Components = Table(
    'RIS_Components', metadata,
    Column('ModelCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('CompCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('ClassName', String(50, u'Chinese_PRC_CI_AS')),
    Column('ParentControl', String(20, u'Chinese_PRC_CI_AS')),
    Column('CompContent', LargeBinary),
    Column('isFix', String(1, u'Chinese_PRC_CI_AS')),
    Column('CreateIndex', Integer),
    Column('TabOrder', Integer)
)


class RISCurUseTechNo(Base):
    __tablename__ = 'RIS_CurUseTechNo'

    NumMakeID = Column(Integer, primary_key=True, nullable=False)
    TechNo = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    Status = Column(String(1, u'Chinese_PRC_CI_AS'))
    ComputerName = Column(String(50, u'Chinese_PRC_CI_AS'))
    UseDate = Column(DateTime)


class RISDOC(Base):
    __tablename__ = 'RIS_DOC'

    ID = Column(Integer, primary_key=True)
    USERID = Column(String(12, u'Chinese_PRC_CI_AS'))
    LabDoc_ID = Column(Integer)
    DocType = Column(String(50, u'Chinese_PRC_CI_AS'))
    DESCS = Column(String(250, u'Chinese_PRC_CI_AS'))


class RISExamItemConfig(Base):
    __tablename__ = 'RIS_ExamItemConfig'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ItemCode = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    Parent = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ItemType = Column(Integer, nullable=False, index=True)


class RISExamItemConfigDic(Base):
    __tablename__ = 'RIS_ExamItemConfigDic'

    SeriesNo = Column(Integer, primary_key=True)
    ItemCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemName = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemType = Column(Integer, nullable=False)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    UpdateFlag = Column(Integer, nullable=False)


class RISExamItemInfo(Base):
    __tablename__ = 'RIS_ExamItemInfo'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ExamItem = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    Price = Column(MONEY)
    Sample = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ReportID = Column(Integer, nullable=False, index=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    SampleOrder = Column(Integer)
    ExamitemOrder = Column(Integer, server_default=text("(1)"))
    Times = Column(Integer)


class RISExamSample(Base):
    __tablename__ = 'RIS_ExamSample'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    Sample = Column(String(100, u'Chinese_PRC_CI_AS'), nullable=False)
    SecSample = Column(String(100, u'Chinese_PRC_CI_AS'), nullable=False)
    FOrderNo = Column(String(20, u'Chinese_PRC_CI_AS'))
    SubSample = Column(String(100, u'Chinese_PRC_CI_AS'))
    SOrderNo = Column(String(20, u'Chinese_PRC_CI_AS'))
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))


t_RIS_FilmNum = Table(
    'RIS_FilmNum', metadata,
    Column('Printer', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('FilmNum', Integer, nullable=False),
    Column('FilmSumNum', Integer, nullable=False),
    Column('PaperNum', Integer, nullable=False),
    Column('MsgFlag', String(1, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('PrinterName', String(50, u'Chinese_PRC_CI_AS'), nullable=False)
)


class RISFormModel(Base):
    __tablename__ = 'RIS_FormModel'

    SerialNo = Column(Integer, primary_key=True)
    ModelCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    ModelName = Column(String(50, u'Chinese_PRC_CI_AS'))
    DLLPath = Column(String(200, u'Chinese_PRC_CI_AS'))
    ModelContent = Column(LargeBinary)


class RISForm(Base):
    __tablename__ = 'RIS_Forms'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    FuncCode = Column(String(50, u'Chinese_PRC_CI_AS'))
    FuncName = Column(String(100, u'Chinese_PRC_CI_AS'))
    ReportID = Column(Integer)
    ModelCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    FormContent = Column(LargeBinary)


class RISGetPart(Base):
    __tablename__ = 'RIS_GetPart'

    GetPartNo = Column(Integer, primary_key=True)
    ApplyNo = Column(Integer, nullable=False)
    LabelId = Column(String(32, u'Chinese_PRC_CI_AS'))
    TaskType = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    TissueCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    TissueName = Column(String(50, u'Chinese_PRC_CI_AS'))
    PartCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    PartName = Column(String(50, u'Chinese_PRC_CI_AS'))
    Quantity = Column(Integer, nullable=False)
    TechnicianCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    TechnicianName = Column(String(50, u'Chinese_PRC_CI_AS'))
    GetPartDate = Column(DateTime)
    OperatorCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    OperatorName = Column(String(50, u'Chinese_PRC_CI_AS'))
    OperatorDate = Column(DateTime)
    Description = Column(String(500, u'Chinese_PRC_CI_AS'))
    Remark = Column(String(500, u'Chinese_PRC_CI_AS'))


class RISGetPartProces(Base):
    __tablename__ = 'RIS_GetPartProcess'

    GetPartNo = Column(Integer, nullable=False)
    ProcessId = Column(Integer, primary_key=True)
    ProcessCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    ProcessName = Column(String(50, u'Chinese_PRC_CI_AS'))
    ProcessDate = Column(DateTime)
    Quantity = Column(Integer)
    Remark = Column(String(500, u'Chinese_PRC_CI_AS'))
    Status = Column(Integer, nullable=False)
    ProcessStartDate = Column(DateTime)


class RISGridHeadDic(Base):
    __tablename__ = 'RIS_GridHeadDic'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ReportID = Column(Integer)
    GridName = Column(String(50, u'Chinese_PRC_CI_AS'))
    RowColFlag = Column(String(1, u'Chinese_PRC_CI_AS'))
    RowColCaption = Column(String(50, u'Chinese_PRC_CI_AS'))
    RowColType = Column(String(1, u'Chinese_PRC_CI_AS'))
    RowColIndex = Column(Integer)
    Data = Column(String(200, u'Chinese_PRC_CI_AS'))
    Parent = Column(Integer)


class RISHasGetReport(Base):
    __tablename__ = 'RIS_HasGetReport'

    ApplyNo = Column(Integer, primary_key=True)
    Status = Column(Integer, server_default=text("(0)"))
    Voice = Column(Integer, server_default=text("(0)"))
    AppendTime = Column(DateTime, server_default=text("(getdate())"))
    AppendUserID = Column(String(20, u'Chinese_PRC_CI_AS'))
    AppendUserName = Column(String(50, u'Chinese_PRC_CI_AS'))
    TempRptStatus = Column(String(20, u'Chinese_PRC_CI_AS'))


class RISImageProcessArrowInfo(Base):
    __tablename__ = 'RIS_ImageProcessArrowInfo'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ImageID = Column(Integer, nullable=False)
    EditTime = Column(DateTime, nullable=False)
    BeginPosX = Column(Integer)
    BeginPosY = Column(Integer)
    EndPosX = Column(Integer)
    EndPosY = Column(Integer)
    LineSize = Column(Integer)
    LineColor = Column(Integer)


class RISImageProcessInfo(Base):
    __tablename__ = 'RIS_ImageProcessInfo'

    ImageID = Column(Integer, primary_key=True)
    EditTime = Column(DateTime, nullable=False)
    KeepWH = Column(Integer)
    ClipFlag = Column(Integer, nullable=False)
    ClipTop = Column(Integer)
    ClipLeft = Column(Integer)
    ClipWidth = Column(Integer)
    ClipHeight = Column(Integer)
    QualityFlag = Column(Integer, nullable=False)
    Brightness = Column(Integer)
    Contrast = Column(Integer)
    Saturation = Column(Integer)
    Hue = Column(Integer)
    LineFlag = Column(Integer, nullable=False, server_default=text("(0)"))
    MeasureFlag = Column(Integer)


class RISItemDic(Base):
    __tablename__ = 'RIS_ItemDic'

    SerialNo = Column(Integer, primary_key=True)
    ReportID = Column(Integer, nullable=False)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'))
    DataType = Column(String(1, u'Chinese_PRC_CI_AS'))
    ItemUnit = Column(String(10, u'Chinese_PRC_CI_AS'))
    Comment = Column(String(100, u'Chinese_PRC_CI_AS'))
    UpperLimit = Column(Numeric(14, 4))
    LowerLimit = Column(Numeric(14, 4))
    DefaultValue = Column(String(40, u'Chinese_PRC_CI_AS'))
    PrintFlag = Column(Integer)
    FieldName = Column(String(20, u'Chinese_PRC_CI_AS'))
    TemplateFlag = Column(Integer)
    AnalyzeFlag = Column(Integer)


class RISItemMapping(Base):
    __tablename__ = 'RIS_ItemMapping'

    SerialNo = Column(Integer, primary_key=True)
    ReportID = Column(Integer, nullable=False)
    SrcCode = Column(String(40, u'Chinese_PRC_CI_AS'))
    DesCode = Column(String(40, u'Chinese_PRC_CI_AS'))


class RISList(Base):
    __tablename__ = 'RIS_List'

    ApplyNo = Column(Integer, primary_key=True)
    TechNo = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ExecTime = Column(DateTime, index=True)
    LabelID = Column(String(32, u'Chinese_PRC_CI_AS'), index=True)
    TechPatID = Column(Integer, index=True)
    PatName = Column(String(40, u'Chinese_PRC_CI_AS'), index=True)
    PatNameSpell = Column(String(40, u'Chinese_PRC_CI_AS'), index=True)
    PatientID = Column(Integer, index=True)
    CureNo = Column(Integer, index=True)
    CardNo = Column(String(30, u'Chinese_PRC_CI_AS'), index=True)
    HospNo = Column(String(20, u'Chinese_PRC_CI_AS'), index=True)
    Sex = Column(String(1, u'Chinese_PRC_CI_AS'))
    Age = Column(Numeric(5, 2))
    AgeUnit = Column(String(6, u'Chinese_PRC_CI_AS'))
    Birthday = Column(DateTime)
    Career = Column(String(30, u'Chinese_PRC_CI_AS'))
    Phone = Column(String(20, u'Chinese_PRC_CI_AS'))
    Address = Column(String(100, u'Chinese_PRC_CI_AS'))
    Zip = Column(String(6, u'Chinese_PRC_CI_AS'))
    Nation = Column(String(20, u'Chinese_PRC_CI_AS'))
    IDNum = Column(String(20, u'Chinese_PRC_CI_AS'))
    ChargeType = Column(String(12, u'Chinese_PRC_CI_AS'))
    ChargeTypeName = Column(String(50, u'Chinese_PRC_CI_AS'))
    ApplyDept = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyDeptName = Column(String(50, u'Chinese_PRC_CI_AS'))
    Ward = Column(String(12, u'Chinese_PRC_CI_AS'))
    WardName = Column(String(50, u'Chinese_PRC_CI_AS'))
    BedNo = Column(String(10, u'Chinese_PRC_CI_AS'))
    WardOrReg = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyTime = Column(DateTime)
    BriefCase = Column(String(255, u'Chinese_PRC_CI_AS'))
    ClinicDesc = Column(String(255, u'Chinese_PRC_CI_AS'))
    AcceptTime = Column(DateTime, index=True)
    ApplyDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    Accepter = Column(String(12, u'Chinese_PRC_CI_AS'))
    AccepterName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ExecDoctor1 = Column(String(12, u'Chinese_PRC_CI_AS'))
    ExecDoctor1Name = Column(String(20, u'Chinese_PRC_CI_AS'))
    ExecDoctor2 = Column(String(12, u'Chinese_PRC_CI_AS'))
    ExecDoctor2Name = Column(String(20, u'Chinese_PRC_CI_AS'))
    QualityDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    QualityDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    VerifyDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    VerifyDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ReportDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    ReportDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ReportWriter = Column(String(12, u'Chinese_PRC_CI_AS'))
    ReportWriterName = Column(String(20, u'Chinese_PRC_CI_AS'))
    FinallyEditDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    FinallyEditDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    FinallyEditTime = Column(DateTime)
    AuditingTime = Column(DateTime)
    PublicTime = Column(DateTime)
    ReportID = Column(Integer, index=True)
    ReportTime = Column(DateTime, server_default=text("(getdate())"))
    Instrument = Column(String(50, u'Chinese_PRC_CI_AS'))
    OrgApplyNo = Column(String(12, u'Chinese_PRC_CI_AS'))
    Status = Column(Integer, nullable=False)
    LockFlag = Column(Integer)
    Locker = Column(String(30, u'Chinese_PRC_CI_AS'))
    PrintFlag = Column(Integer, server_default=text("(0)"))
    DeleteFlag = Column(Integer, server_default=text("(0)"))
    ChargeFlag = Column(Integer, server_default=text("(0)"))
    HavingImages = Column(SmallInteger, server_default=text("(0)"))
    EngName = Column(String(100, u'Chinese_PRC_CI_AS'))
    EquipmentID = Column(String(10, u'Chinese_PRC_CI_AS'))
    Invoice = Column(String(20, u'Chinese_PRC_CI_AS'), index=True)
    ImageTime = Column(DateTime)
    DpSign = Column(Integer, server_default=text("(0)"))
    dpsuggest = Column(String(50, u'Chinese_PRC_CI_AS'))
    ExamTime = Column(DateTime)
    BookCenterSID = Column(Integer)
    CrisisFlag = Column(Integer, server_default=text("(0)"))
    SurveySign = Column(Integer, server_default=text("(0)"))
    SurveySuggest = Column(String(50, u'Chinese_PRC_CI_AS'))
    JCBZ = Column(Integer, server_default=text("(0)"))
    ExamFlag = Column(Integer, server_default=text("(0)"))
    RegionDpSign = Column(Integer)
    RegionDpSuggest = Column(String(20, u'Chinese_PRC_CI_AS'))
    CrisisEnt = Column(Integer, server_default=text("(0)"))
    LockUser = Column(String(20, u'Chinese_PRC_CI_AS'))
    DeleteUser = Column(String(50, u'Chinese_PRC_CI_AS'))
    DeleteTime = Column(DateTime)


class RISListHistory(Base):
    __tablename__ = 'RIS_List_History'

    ApplyNo = Column(Integer, primary_key=True)
    TechNo = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ExecTime = Column(DateTime, index=True)
    LabelID = Column(String(32, u'Chinese_PRC_CI_AS'), index=True)
    TechPatID = Column(Integer, index=True)
    PatName = Column(String(40, u'Chinese_PRC_CI_AS'), index=True)
    PatNameSpell = Column(String(40, u'Chinese_PRC_CI_AS'))
    PatientID = Column(Integer, index=True)
    CureNo = Column(Integer, index=True)
    CardNo = Column(String(30, u'Chinese_PRC_CI_AS'), index=True)
    HospNo = Column(String(20, u'Chinese_PRC_CI_AS'), index=True)
    Sex = Column(String(1, u'Chinese_PRC_CI_AS'))
    Age = Column(Numeric(5, 2))
    AgeUnit = Column(String(6, u'Chinese_PRC_CI_AS'))
    Birthday = Column(DateTime)
    Career = Column(String(30, u'Chinese_PRC_CI_AS'))
    Phone = Column(String(20, u'Chinese_PRC_CI_AS'))
    Address = Column(String(100, u'Chinese_PRC_CI_AS'))
    Zip = Column(String(6, u'Chinese_PRC_CI_AS'))
    Nation = Column(String(20, u'Chinese_PRC_CI_AS'))
    IDNum = Column(String(20, u'Chinese_PRC_CI_AS'))
    ChargeType = Column(String(12, u'Chinese_PRC_CI_AS'))
    ChargeTypeName = Column(String(50, u'Chinese_PRC_CI_AS'))
    ApplyDept = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyDeptName = Column(String(50, u'Chinese_PRC_CI_AS'))
    Ward = Column(String(12, u'Chinese_PRC_CI_AS'))
    WardName = Column(String(50, u'Chinese_PRC_CI_AS'))
    BedNo = Column(String(10, u'Chinese_PRC_CI_AS'))
    WardOrReg = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyTime = Column(DateTime)
    BriefCase = Column(String(255, u'Chinese_PRC_CI_AS'))
    ClinicDesc = Column(String(255, u'Chinese_PRC_CI_AS'))
    AcceptTime = Column(DateTime)
    ApplyDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    Accepter = Column(String(12, u'Chinese_PRC_CI_AS'))
    AccepterName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ExecDoctor1 = Column(String(12, u'Chinese_PRC_CI_AS'))
    ExecDoctor1Name = Column(String(20, u'Chinese_PRC_CI_AS'))
    ExecDoctor2 = Column(String(12, u'Chinese_PRC_CI_AS'))
    ExecDoctor2Name = Column(String(20, u'Chinese_PRC_CI_AS'))
    QualityDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    QualityDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    VerifyDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    VerifyDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ReportDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    ReportDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ReportWriter = Column(String(12, u'Chinese_PRC_CI_AS'))
    ReportWriterName = Column(String(20, u'Chinese_PRC_CI_AS'))
    FinallyEditDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    FinallyEditDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    FinallyEditTime = Column(DateTime)
    AuditingTime = Column(DateTime)
    PublicTime = Column(DateTime)
    ReportID = Column(Integer, index=True)
    ReportTime = Column(DateTime, server_default=text("(getdate())"))
    Instrument = Column(String(50, u'Chinese_PRC_CI_AS'))
    OrgApplyNo = Column(String(12, u'Chinese_PRC_CI_AS'))
    Status = Column(Integer, nullable=False)
    LockFlag = Column(Integer)
    Locker = Column(String(30, u'Chinese_PRC_CI_AS'))
    PrintFlag = Column(Integer, server_default=text("(0)"))
    DeleteFlag = Column(Integer, server_default=text("(0)"))
    ChargeFlag = Column(Integer, server_default=text("(0)"))
    HavingImages = Column(SmallInteger, server_default=text("(0)"))
    EngName = Column(String(100, u'Chinese_PRC_CI_AS'))
    EquipmentID = Column(String(10, u'Chinese_PRC_CI_AS'))
    Invoice = Column(String(20, u'Chinese_PRC_CI_AS'), index=True)
    ImageTime = Column(DateTime)
    DpSign = Column(Integer, server_default=text("(0)"))
    dpsuggest = Column(String(50, u'Chinese_PRC_CI_AS'))
    ExamTime = Column(DateTime)
    BookCenterSID = Column(Integer)
    CrisisFlag = Column(Integer, server_default=text("(0)"))
    SurveySign = Column(Integer, server_default=text("(0)"))
    SurveySuggest = Column(String(50, u'Chinese_PRC_CI_AS'))
    JCBZ = Column(Integer, server_default=text("(0)"))
    ExamFlag = Column(Integer, server_default=text("(0)"))
    RegionDpSign = Column(Integer)
    RegionDpSuggest = Column(String(20, u'Chinese_PRC_CI_AS'))
    CrisisEnt = Column(Integer, server_default=text("(0)"))
    LockUser = Column(String(20, u'Chinese_PRC_CI_AS'))
    DeleteUser = Column(String(50, u'Chinese_PRC_CI_AS'))
    DeleteTime = Column(DateTime)


class RISListModify(Base):
    __tablename__ = 'RIS_List_Modify'

    ModID = Column(Integer, primary_key=True)
    ModDateTime = Column(DateTime, nullable=False, server_default=text("(getdate())"))
    ModDocCode = Column(String(12, u'Chinese_PRC_CI_AS'), nullable=False)
    ModDocName = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    ApplyNo = Column(Integer, nullable=False, index=True)
    TechNo = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ExecTime = Column(DateTime, index=True)
    LabelID = Column(String(32, u'Chinese_PRC_CI_AS'), index=True)
    TechPatID = Column(Integer, index=True)
    PatName = Column(String(40, u'Chinese_PRC_CI_AS'), index=True)
    PatNameSpell = Column(String(40, u'Chinese_PRC_CI_AS'))
    PatientID = Column(Integer, index=True)
    CureNo = Column(Integer, index=True)
    CardNo = Column(String(30, u'Chinese_PRC_CI_AS'), index=True)
    HospNo = Column(String(20, u'Chinese_PRC_CI_AS'), index=True)
    Sex = Column(String(1, u'Chinese_PRC_CI_AS'))
    Age = Column(Numeric(5, 2))
    AgeUnit = Column(String(6, u'Chinese_PRC_CI_AS'))
    Birthday = Column(DateTime)
    Career = Column(String(30, u'Chinese_PRC_CI_AS'))
    Phone = Column(String(20, u'Chinese_PRC_CI_AS'))
    Address = Column(String(100, u'Chinese_PRC_CI_AS'))
    Zip = Column(String(6, u'Chinese_PRC_CI_AS'))
    Nation = Column(String(20, u'Chinese_PRC_CI_AS'))
    IDNum = Column(String(20, u'Chinese_PRC_CI_AS'))
    ChargeType = Column(String(12, u'Chinese_PRC_CI_AS'))
    ChargeTypeName = Column(String(50, u'Chinese_PRC_CI_AS'))
    ApplyDept = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyDeptName = Column(String(50, u'Chinese_PRC_CI_AS'))
    Ward = Column(String(12, u'Chinese_PRC_CI_AS'))
    WardName = Column(String(50, u'Chinese_PRC_CI_AS'))
    BedNo = Column(String(10, u'Chinese_PRC_CI_AS'))
    WardOrReg = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyTime = Column(DateTime)
    BriefCase = Column(String(255, u'Chinese_PRC_CI_AS'))
    ClinicDesc = Column(String(255, u'Chinese_PRC_CI_AS'))
    AcceptTime = Column(DateTime)
    ApplyDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    Accepter = Column(String(12, u'Chinese_PRC_CI_AS'))
    AccepterName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ExecDoctor1 = Column(String(12, u'Chinese_PRC_CI_AS'))
    ExecDoctor1Name = Column(String(20, u'Chinese_PRC_CI_AS'))
    ExecDoctor2 = Column(String(12, u'Chinese_PRC_CI_AS'))
    ExecDoctor2Name = Column(String(20, u'Chinese_PRC_CI_AS'))
    QualityDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    QualityDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    VerifyDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    VerifyDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ReportDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    ReportDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    ReportWriter = Column(String(12, u'Chinese_PRC_CI_AS'))
    ReportWriterName = Column(String(20, u'Chinese_PRC_CI_AS'))
    FinallyEditDoctor = Column(String(12, u'Chinese_PRC_CI_AS'))
    FinallyEditDoctorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    FinallyEditTime = Column(DateTime)
    AuditingTime = Column(DateTime)
    PublicTime = Column(DateTime)
    ReportID = Column(Integer, index=True)
    ReportTime = Column(DateTime, server_default=text("(getdate())"))
    Instrument = Column(String(50, u'Chinese_PRC_CI_AS'))
    OrgApplyNo = Column(String(12, u'Chinese_PRC_CI_AS'))
    Status = Column(Integer, nullable=False)
    LockFlag = Column(Integer)
    Locker = Column(String(30, u'Chinese_PRC_CI_AS'))
    PrintFlag = Column(Integer, server_default=text("(0)"))
    DeleteFlag = Column(Integer, server_default=text("(0)"))
    ChargeFlag = Column(Integer, server_default=text("(0)"))
    HavingImages = Column(SmallInteger, server_default=text("(0)"))
    EngName = Column(String(100, u'Chinese_PRC_CI_AS'))
    EquipmentID = Column(String(10, u'Chinese_PRC_CI_AS'))
    Invoice = Column(String(20, u'Chinese_PRC_CI_AS'), index=True)
    ImageTime = Column(DateTime)
    ExamTime = Column(DateTime)
    CrisisFlag = Column(Integer, server_default=text("(0)"))
    SurveySign = Column(Integer, server_default=text("(0)"))
    SurveySuggest = Column(String(50, u'Chinese_PRC_CI_AS'))
    JCBZ = Column(Integer, server_default=text("(0)"))
    ExamFlag = Column(Integer, server_default=text("(0)"))
    RegionDpSign = Column(Integer)
    RegionDpSuggest = Column(String(20, u'Chinese_PRC_CI_AS'))
    CrisisEnt = Column(Integer, server_default=text("(0)"))
    LockUser = Column(String(20, u'Chinese_PRC_CI_AS'))
    DeleteUser = Column(String(50, u'Chinese_PRC_CI_AS'))
    DeleteTime = Column(DateTime)


class RISMakeTechNo(Base):
    __tablename__ = 'RIS_MakeTechNo'

    NumMakeID = Column(Integer, primary_key=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    UserName = Column(String(50, u'Chinese_PRC_CI_AS'))
    CurNum = Column(Integer)
    PrePart = Column(String(10, u'Chinese_PRC_CI_AS'))
    BackPart = Column(String(10, u'Chinese_PRC_CI_AS'))
    MakeMethod = Column(String(1, u'Chinese_PRC_CI_AS'))
    Period = Column(String(1, u'Chinese_PRC_CI_AS'))
    LastUseDate = Column(DateTime)
    Recycle = Column(String(1, u'Chinese_PRC_CI_AS'))
    OpStyle = Column(String(1, u'Chinese_PRC_CI_AS'))
    AddZero = Column(String(1, u'Chinese_PRC_CI_AS'))
    ZeroLen = Column(Integer)


class RISOrigApply(Base):
    __tablename__ = 'RIS_OrigApply'

    ApplyNo = Column(Integer, primary_key=True)
    OpCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    OpName = Column(String(20, u'Chinese_PRC_CI_AS'))
    OpTime = Column(DateTime)
    Content = Column(LargeBinary)


class RISOrigApplyHistory(Base):
    __tablename__ = 'RIS_OrigApply_History'

    ApplyNo = Column(Integer, primary_key=True)
    OpCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    OpName = Column(String(20, u'Chinese_PRC_CI_AS'))
    OpTime = Column(DateTime)
    Content = Column(LargeBinary)


class RISQueue(Base):
    __tablename__ = 'RIS_Queue'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    ReportID = Column(Integer)
    ApplyNo = Column(Integer)
    EquipmentID = Column(Integer)
    QueueDate = Column(DateTime)
    PatName = Column(String(40, u'Chinese_PRC_CI_AS'))
    Address = Column(String(50, u'Chinese_PRC_CI_AS'))
    QueueNo = Column(Integer)
    Status = Column(Integer)
    ClassNo = Column(Integer)
    BookTime = Column(Float(53))
    TimeType = Column(Integer)
    WaitNo = Column(Integer)
    Pause = Column(Integer)


class RISQueueRoom(Base):
    __tablename__ = 'RIS_QueueRoom'
    __table_args__ = (
        Index('idx_RIS_QueueRoom_SysCodeRoom', 'SubSysCode', 'RoomName'),
    )

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    RoomName = Column(String(30, u'Chinese_PRC_CI_AS'), nullable=False)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    GroupPre = Column(String(2, u'Chinese_PRC_CI_AS'))


t_RIS_QyerityDocs = Table(
    'RIS_QyerityDocs', metadata,
    Column('Id', Integer, nullable=False),
    Column('DocType', Integer, nullable=False),
    Column('DocCode', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('DocName', String(50, u'Chinese_PRC_CI_AS')),
    Column('DocContent', UnicodeText(1073741823)),
    Column('WriteDate', DateTime),
    Column('Writer', String(50, u'Chinese_PRC_CI_AS')),
    Column('MEMO', String(256, u'Chinese_PRC_CI_AS'))
)


class RISReportTechNo(Base):
    __tablename__ = 'RIS_ReportTechNo'

    ReportID = Column(Integer, primary_key=True, nullable=False)
    NumMakeID = Column(Integer, primary_key=True, nullable=False)


class RISResult(Base):
    __tablename__ = 'RIS_Result'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ApplyNo = Column(Integer, nullable=False, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemResult = Column(String(7000, u'Chinese_PRC_CI_AS'))


class RISResultGridDetail(Base):
    __tablename__ = 'RIS_ResultGridDetail'
    __table_args__ = (
        Index('idx_Ris_ResultGridDetail_SeqNo', 'ColName', 'RowName', 'SeqNo'),
    )

    SeqNo = Column(Integer, primary_key=True, nullable=False)
    RowName = Column(String(100, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ColName = Column(String(100, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ResultData = Column(String(200, u'Chinese_PRC_CI_AS'))


class RISResultGridDetailHistory(Base):
    __tablename__ = 'RIS_ResultGridDetail_History'
    __table_args__ = (
        Index('idx_Ris_ResultGridDetail_History_SeqNo', 'ColName', 'RowName', 'SeqNo'),
    )

    SeqNo = Column(Integer, primary_key=True, nullable=False)
    RowName = Column(String(100, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ColName = Column(String(100, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ResultData = Column(String(200, u'Chinese_PRC_CI_AS'))


class RISResultGridMaster(Base):
    __tablename__ = 'RIS_ResultGridMaster'
    __table_args__ = (
        Index('idx_Ris_ResultGridMaster_ItemCode', 'ItemCode', 'ItemResult'),
    )

    SeqNo = Column(Integer, primary_key=True)
    ApplyNo = Column(Integer, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'))
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'))
    ItemResult = Column(String(80, u'Chinese_PRC_CI_AS'))
    Parent = Column(Integer)


class RISResultGridMasterHistory(Base):
    __tablename__ = 'RIS_ResultGridMaster_History'
    __table_args__ = (
        Index('idx_Ris_ResultGridMaster_History_ItemCode', 'ItemCode', 'ItemResult'),
    )

    SeqNo = Column(Integer, primary_key=True, index=True)
    ApplyNo = Column(Integer, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'))
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'))
    ItemResult = Column(String(80, u'Chinese_PRC_CI_AS'))
    Parent = Column(Integer)


class RISResultIndex(Base):
    __tablename__ = 'RIS_ResultIndex'
    __table_args__ = (
        Index('idx_Ris_ResultIndex_ItemCode', 'ItemCode', 'ItemResult'),
    )

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ApplyNo = Column(Integer, nullable=False, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemResult = Column(String(60, u'Chinese_PRC_CI_AS'))


class RISResultIndexHistory(Base):
    __tablename__ = 'RIS_ResultIndex_History'
    __table_args__ = (
        Index('idx_Ris_ReportIndex_History_ItemCode', 'ItemCode', 'ItemResult'),
    )

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ApplyNo = Column(Integer, nullable=False, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemResult = Column(String(60, u'Chinese_PRC_CI_AS'))


class RISResultHistory(Base):
    __tablename__ = 'RIS_Result_History'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ApplyNo = Column(Integer, nullable=False, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemResult = Column(String(7000, u'Chinese_PRC_CI_AS'))


class RISResultModify(Base):
    __tablename__ = 'RIS_Result_Modify'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ModID = Column(Integer, nullable=False, index=True)
    ApplyNo = Column(Integer, nullable=False, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemResult = Column(String(7000, u'Chinese_PRC_CI_AS'))


t_RIS_SPS = Table(
    'RIS_SPS', metadata,
    Column('SPS_ID', Integer, nullable=False),
    Column('SPS_AETitle', String(64, u'Chinese_PRC_CI_AS')),
    Column('SPS_StartDateTime', DateTime, nullable=False, index=True),
    Column('SPS_PhysiciansName', String(64, u'Chinese_PRC_CI_AS')),
    Column('SPS_Modality', String(64, u'Chinese_PRC_CI_AS')),
    Column('SPS_Description', String(128, u'Chinese_PRC_CI_AS')),
    Column('SPS_CodeValue', String(128, u'Chinese_PRC_CI_AS')),
    Column('SPS_CodingSchemeVersion', String(128, u'Chinese_PRC_CI_AS')),
    Column('SPS_CodingSchemeDesignator', String(128, u'Chinese_PRC_CI_AS')),
    Column('SPS_CodeMeaning', String(128, u'Chinese_PRC_CI_AS')),
    Column('RP_ID', Integer, nullable=False),
    Column('RP_StudyUID', String(128, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('RP_Description', String(128, u'Chinese_PRC_CI_AS')),
    Column('ApplyNo', Integer, nullable=False),
    Column('AccessionNo', String(16, u'Chinese_PRC_CI_AS')),
    Column('PatientID', String(64, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('PatientEnglishName', String(64, u'Chinese_PRC_CI_AS')),
    Column('PPS_ID', String(20, u'Chinese_PRC_CI_AS')),
    Column('PPS_StudyUID', String(128, u'Chinese_PRC_CI_AS')),
    Column('PPS_StartDateTime', DateTime),
    Column('PPS_EndDateTime', DateTime),
    Column('PPS_Description', String(128, u'Chinese_PRC_CI_AS')),
    Column('PPS_ProtocolName', String(128, u'Chinese_PRC_CI_AS')),
    Column('PPS_IsPGP', Integer),
    Column('PPS_Status', Integer, nullable=False),
    Column('PPS_SopInstanceUID', String(128, u'Chinese_PRC_CI_AS')),
    Column('PPS_ImageCount', Integer),
    Column('IMG_Modality', String(20, u'Chinese_PRC_CI_AS')),
    Column('IMG_BodyPart', String(100, u'Chinese_PRC_CI_AS')),
    Column('IMG_StudyDateTime', DateTime),
    Column('PatientName', String(64, u'Chinese_PRC_CI_AS')),
    Column('StudyDescription', String(100, u'Chinese_PRC_CI_AS')),
    Column('StationName', String(50, u'Chinese_PRC_CI_AS')),
    Column('RefPhysiciansName', String(50, u'Chinese_PRC_CI_AS')),
    Column('InstitutionName', String(50, u'Chinese_PRC_CI_AS')),
    Column('PerformingPhysiciansName', String(50, u'Chinese_PRC_CI_AS'))
)


class RISScheduleDic(Base):
    __tablename__ = 'RIS_ScheduleDic'

    SerialNo = Column(Integer, primary_key=True)
    ReportID = Column(Integer, nullable=False)
    BookPlace = Column(String(30, u'Chinese_PRC_CI_AS'), nullable=False)
    TimeDesc = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    BookNum = Column(Integer, nullable=False, server_default=text("(0)"))
    ScheType = Column(String(1, u'Chinese_PRC_CI_AS'), nullable=False)
    BeginDate = Column(DateTime)
    EndDate = Column(DateTime)
    BeginTime = Column(String(5, u'Chinese_PRC_CI_AS'), nullable=False)
    EndTime = Column(String(5, u'Chinese_PRC_CI_AS'), nullable=False)
    TimeType = Column(Integer)
    WeekType = Column(String(20, u'Chinese_PRC_CI_AS'))


class RISSpecialItemDic(Base):
    __tablename__ = 'RIS_SpecialItemDic'

    ItemID = Column(Integer, primary_key=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ItemName = Column(String(60, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    NodeCode = Column(String(50, u'Chinese_PRC_CI_AS'), index=True)
    Parent = Column(Integer)
    MemCode1 = Column(String(8, u'Chinese_PRC_CI_AS'))
    MemCode2 = Column(String(8, u'Chinese_PRC_CI_AS'))
    Data = Column(String(40, u'Chinese_PRC_CI_AS'))
    TemplateID = Column(Integer)
    Type = Column(Integer, nullable=False)
    UserId = Column(String(20, u'Chinese_PRC_CI_AS'))
    UserName = Column(String(50, u'Chinese_PRC_CI_AS'))


class RISTask(Base):
    __tablename__ = 'RIS_Tasks'

    SerialNo = Column(Integer, primary_key=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    TaskType = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    TaskName = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    Priority = Column(Integer, nullable=False)
    Status = Column(Integer, nullable=False)
    Suspend = Column(Integer, nullable=False)
    AppendTime = Column(DateTime, nullable=False)
    SchemingTime = Column(DateTime, nullable=False)
    Deadline = Column(DateTime, nullable=False)
    StartingTime = Column(DateTime)
    AccomplishedTime = Column(DateTime)
    Executor = Column(String(50, u'Chinese_PRC_CI_AS'))
    Description = Column(String(256, u'Chinese_PRC_CI_AS'))
    WaitingTime = Column(DateTime)
    QueueEquipID = Column(String(50, u'Chinese_PRC_CI_AS'))


class RISTemplateDetail(Base):
    __tablename__ = 'RIS_TemplateDetail'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    TemplateID = Column(Integer, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'))
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'))
    Data = Column(String(7000, u'Chinese_PRC_CI_AS'))
    DefaultFlag = Column(Integer)
    MimeFlag = Column(Integer)


class RISTemplateDic(Base):
    __tablename__ = 'RIS_TemplateDic'

    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    TemplateID = Column(Integer, primary_key=True)
    TemplateCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    TemplateName = Column(String(100, u'Chinese_PRC_CI_AS'), nullable=False)


t_RegList = Table(
    'RegList', metadata,
    Column('IPAdd', String(15, u'Chinese_PRC_CI_AS')),
    Column('Port', Integer),
    Column('UserName', String(40, u'Chinese_PRC_CI_AS')),
    Column('ModuleName', String(40, u'Chinese_PRC_CI_AS')),
    Column('ComputeName', String(40, u'Chinese_PRC_CI_AS')),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('AppID', Integer)
)


class RisAccessionNo(Base):
    __tablename__ = 'Ris_AccessionNo'

    SERIALNO = Column(Numeric(18, 0), primary_key=True)
    AccessionNo = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    JSGZZ_HZD = Column(Integer)


class RisApplySheet(Base):
    __tablename__ = 'Ris_ApplySheet'

    SerialNo = Column(Integer, primary_key=True)
    SheetId = Column(Integer, index=True)
    SheetDesc = Column(String(7000, u'Chinese_PRC_CI_AS'))
    PatType = Column(Integer)


class RisBodyPartCodeMapping(Base):
    __tablename__ = 'Ris_BodyPartCodeMapping'

    CodeID = Column(Integer, primary_key=True)
    ReportID = Column(Integer, nullable=False, index=True)
    SrcCode = Column(String(64, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    DestCode1 = Column(String(64, u'Chinese_PRC_CI_AS'), nullable=False)
    DestCode2 = Column(String(64, u'Chinese_PRC_CI_AS'))


class RisDaySchedule(Base):
    __tablename__ = 'Ris_DaySchedule'

    DSID = Column(Integer, primary_key=True)
    ReportID = Column(Integer, nullable=False)
    BookPlace = Column(String(30, u'Chinese_PRC_CI_AS'), nullable=False)
    BookDate = Column(DateTime, nullable=False)
    BeginTime = Column(String(5, u'Chinese_PRC_CI_AS'))
    EndTime = Column(String(5, u'Chinese_PRC_CI_AS'))
    BookedNum = Column(Integer, nullable=False)
    CanBookNum = Column(Integer, nullable=False)
    TimeDesc = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    TimeType = Column(Integer)
    DSIDMemo = Column(String(50, u'Chinese_PRC_CI_AS'))
    Status = Column(String(1, u'Chinese_PRC_CI_AS'), server_default=text("('0')"))
    VaryBookNum = Column(Integer, server_default=text("(0)"))


class RisDpRecord(Base):
    __tablename__ = 'Ris_DpRecord'

    SerialNo = Column(Integer, primary_key=True)
    ApplyNo = Column(Integer, nullable=False)
    DpDate = Column(DateTime)
    DpEmceeCode = Column(String(50, u'Chinese_PRC_CI_AS'))
    DPEmceeName = Column(String(50, u'Chinese_PRC_CI_AS'))
    DpAttenders = Column(String(200, u'Chinese_PRC_CI_AS'))
    DpComment = Column(String(4000, u'Chinese_PRC_CI_AS'))
    EmceeSummary = Column(String(1500, u'Chinese_PRC_CI_AS'))
    DpSummary = Column(String(1500, u'Chinese_PRC_CI_AS'))
    DpSuggest = Column(String(20, u'Chinese_PRC_CI_AS'))
    BLSummary = Column(String(1000, u'Chinese_PRC_CI_AS'))


class RisEMFile(Base):
    __tablename__ = 'Ris_EM_File'

    EM_ID = Column(Integer, primary_key=True)
    LABDOC_ID = Column(Integer, server_default=text("(0)"))
    Doc_Desc = Column(String(500, u'Chinese_PRC_CI_AS'))
    CreateDate = Column(DateTime)
    Equipment_MaintenanceID = Column(Integer)


class RisEquipmentRunLog(Base):
    __tablename__ = 'Ris_EquipmentRunLog'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    LogTime = Column(DateTime)
    LogContent = Column(String(2000, u'Chinese_PRC_CI_AS'), nullable=False)
    LogUser = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    EquipMentID = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    Status = Column(Integer)


class RisEquipmentMaintenance(Base):
    __tablename__ = 'Ris_Equipment_Maintenance'

    Equipment_MaintenanceID = Column(Integer, primary_key=True)
    FaultDate = Column(DateTime, nullable=False)
    FaultUserId = Column(String(20, u'Chinese_PRC_CI_AS'))
    FaultMemo = Column(String(500, u'Chinese_PRC_CI_AS'))
    CallFaultDate = Column(DateTime, nullable=False)
    CallFaultUserId = Column(String(20, u'Chinese_PRC_CI_AS'))
    RepairDate = Column(DateTime)
    ReceiveUserId = Column(String(20, u'Chinese_PRC_CI_AS'))
    RepairUserId = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    Contact = Column(String(30, u'Chinese_PRC_CI_AS'), nullable=False)
    RepairMemo = Column(String(2000, u'Chinese_PRC_CI_AS'))
    EquipMentID = Column(Integer)


class RisExamLexicon(Base):
    __tablename__ = 'Ris_ExamLexicon'

    Id = Column(Integer, primary_key=True)
    LexiconName = Column(String(50, u'Chinese_PRC_CI_AS'), nullable=False)
    ReportID = Column(Integer, nullable=False)
    LexiconMemo = Column(String(500, u'Chinese_PRC_CI_AS'))
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    StopUse = Column(Integer, nullable=False, server_default=text("(0)"))


class RisExamMethod(Base):
    __tablename__ = 'Ris_ExamMethod'

    SerialNo = Column(Integer, primary_key=True)
    ReportID = Column(Integer, index=True)
    ExamType = Column(String(50, u'Chinese_PRC_CI_AS'))
    MethodDesc = Column(String(100, u'Chinese_PRC_CI_AS'))
    Remark = Column(String(100, u'Chinese_PRC_CI_AS'))
    OrderNo = Column(String(20, u'Chinese_PRC_CI_AS'))


class RisHisInterFace(Base):
    __tablename__ = 'Ris_HisInterFace'

    SerialNo = Column(Integer, primary_key=True)
    LogContent = Column(String(7000, u'Chinese_PRC_CI_AS'))
    LogTime = Column(DateTime)
    HostName = Column(String(100, u'Chinese_PRC_CI_AS'))


t_Ris_ImageMeasureInfo = Table(
    'Ris_ImageMeasureInfo', metadata,
    Column('SERIALNO', Integer, nullable=False),
    Column('ImageId', Integer),
    Column('EditTime', DateTime, server_default=text("(getdate())")),
    Column('BeginPosX', Integer),
    Column('BeginPosY', Integer),
    Column('EndPosX', Integer),
    Column('EndPosY', Integer),
    Column('MeasureValue', Float(53)),
    Column('iType', Integer),
    Column('Memo', String(400, u'Chinese_PRC_CI_AS')),
    Column('LineColor', Integer)
)


t_Ris_JSYPB = Table(
    'Ris_JSYPB', metadata,
    Column('SerialNo', Integer, nullable=False),
    Column('EquipMentID', String(50, u'Chinese_PRC_CI_AS')),
    Column('EquipmentName', String(50, u'Chinese_PRC_CI_AS')),
    Column('Operator', String(50, u'Chinese_PRC_CI_AS')),
    Column('ModifyDate', DateTime)
)


t_Ris_KQInfo = Table(
    'Ris_KQInfo', metadata,
    Column('SerialNo', Integer, nullable=False),
    Column('kqDate', DateTime, nullable=False),
    Column('userid', String(20, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('userName', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('WorkInfo', String(100, u'Chinese_PRC_CI_AS')),
    Column('Status', Integer),
    Column('ActionByCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('ActionByName', String(50, u'Chinese_PRC_CI_AS')),
    Column('ActionTime', DateTime),
    Column('VerifyCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('VerifyName', String(50, u'Chinese_PRC_CI_AS')),
    Column('VerifyTime', DateTime)
)


t_Ris_KQUserGroup = Table(
    'Ris_KQUserGroup', metadata,
    Column('SerialNo', Integer, nullable=False),
    Column('userid', String(20, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('GroupCode', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('GroupName', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS'), nullable=False)
)


t_Ris_OrderToItem = Table(
    'Ris_OrderToItem', metadata,
    Column('SerialNo', Integer, nullable=False),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('InstID', Integer),
    Column('HisOrderCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('HisOrderName', String(100, u'Chinese_PRC_CI_AS')),
    Column('ItemId', String(10, u'Chinese_PRC_CI_AS')),
    Column('ItemName', String(100, u'Chinese_PRC_CI_AS')),
    Column('ExamName', String(50, u'Chinese_PRC_CI_AS')),
    Column('OrderNo', String(20, u'Chinese_PRC_CI_AS')),
    Index('IX_Ris_OrderToItem', 'SubSysCode', 'InstID', 'HisOrderCode', 'ItemId', unique=True)
)


t_Ris_QC_List = Table(
    'Ris_QC_List', metadata,
    Column('SERIALNO', Integer, nullable=False),
    Column('Applyno', Integer, nullable=False),
    Column('Qc_Date', DateTime, server_default=text("(getdate())"))
)


t_Ris_QC_Result = Table(
    'Ris_QC_Result', metadata,
    Column('SERIALNO', Integer, nullable=False),
    Column('Applyno', Integer, nullable=False),
    Column('ItemCode', String(10, u'Chinese_PRC_CI_AS')),
    Column('ItemName', String(40, u'Chinese_PRC_CI_AS')),
    Column('ItemResult', String(7000, u'Chinese_PRC_CI_AS'))
)


t_Ris_QuerityResult = Table(
    'Ris_QuerityResult', metadata,
    Column('ID', Integer, nullable=False),
    Column('ReportType', String(20, u'Chinese_PRC_CI_AS')),
    Column('ExamItemField', String(50, u'Chinese_PRC_CI_AS'), server_default=text("('')")),
    Column('ExamItemResult', String(2000, u'Chinese_PRC_CI_AS')),
    Column('ExamYear', String(4, u'Chinese_PRC_CI_AS')),
    Column('ExamMonth', String(4, u'Chinese_PRC_CI_AS')),
    Column('PrintDate', DateTime)
)


class RisResultFormat(Base):
    __tablename__ = 'Ris_ResultFormat'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ApplyNo = Column(Integer, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'), index=True)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'))
    ItemResult = Column(String(7000, u'Chinese_PRC_CI_AS'))


t_Ris_SPS_Protocolcodemapping = Table(
    'Ris_SPS_Protocolcodemapping', metadata,
    Column('CodeID', Integer, nullable=False),
    Column('AETitle', String(20, u'Chinese_PRC_CI_AS')),
    Column('SrcCode', String(50, u'Chinese_PRC_CI_AS')),
    Column('CodeValue', String(50, u'Chinese_PRC_CI_AS')),
    Column('CodeMeaning', String(50, u'Chinese_PRC_CI_AS')),
    Column('CodingSchemeDesignator', String(50, u'Chinese_PRC_CI_AS')),
    Column('CodingSchemeVersion', String(50, u'Chinese_PRC_CI_AS')),
    Column('SpecificCharacterSet', String(50, u'Chinese_PRC_CI_AS'))
)


t_Ris_SetQueryConditions = Table(
    'Ris_SetQueryConditions', metadata,
    Column('SERIALNO', Integer, nullable=False),
    Column('TabName', String(20, u'Chinese_PRC_CI_AS')),
    Column('TableName', String(30, u'Chinese_PRC_CI_AS')),
    Column('TableDesc', String(30, u'Chinese_PRC_CI_AS')),
    Column('FieldName', String(30, u'Chinese_PRC_CI_AS')),
    Column('FieldDesc', String(30, u'Chinese_PRC_CI_AS')),
    Column('InputType', String(30, u'Chinese_PRC_CI_AS')),
    Column('cFirstValue', String(512, u'Chinese_PRC_CI_AS')),
    Column('cLastValue', String(512, u'Chinese_PRC_CI_AS')),
    Column('UseRelation', String(1024, u'Chinese_PRC_CI_AS')),
    Column('InputSQL', String(1000, u'Chinese_PRC_CI_AS')),
    Column('Relation', String(40, u'Chinese_PRC_CI_AS')),
    Column('DispRelation', String(100, u'Chinese_PRC_CI_AS')),
    Column('Locking', Integer),
    Column('UserCode', String(40, u'Chinese_PRC_CI_AS')),
    Column('UserName', String(40, u'Chinese_PRC_CI_AS')),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('DispOrder', Integer),
    Column('AddDate', DateTime, server_default=text("(getdate())"))
)


t_Ris_SketchPoints = Table(
    'Ris_SketchPoints', metadata,
    Column('SerialNo', Integer, nullable=False),
    Column('ApplyNo', Integer),
    Column('TypeCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('TypeName', String(50, u'Chinese_PRC_CI_AS')),
    Column('CheckItemCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('CheckItemName', String(50, u'Chinese_PRC_CI_AS')),
    Column('PosX', Integer),
    Column('PosY', Integer),
    Column('iSketchColorCode', Integer)
)


t_Ris_TeachTemplate = Table(
    'Ris_TeachTemplate', metadata,
    Column('TeachID', Integer, nullable=False, unique=True),
    Column('TeachName', String(100, u'Chinese_PRC_CI_AS')),
    Column('Parent', Integer, index=True),
    Column('OrderNo', Integer),
    Column('Type', Integer),
    Column('UserId', String(10, u'Chinese_PRC_CI_AS')),
    Column('UserName', String(20, u'Chinese_PRC_CI_AS')),
    Column('Data', String(2500, u'Chinese_PRC_CI_AS')),
    Column('DataType', String(50, u'Chinese_PRC_CI_AS')),
    Column('MemCode1', String(50, u'Chinese_PRC_CI_AS')),
    Column('MemCode2', String(50, u'Chinese_PRC_CI_AS')),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('ImageData', LargeBinary)
)


class RisVerifyUser(Base):
    __tablename__ = 'Ris_VerifyUsers'

    UserID = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    VerifiedUserID = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)


class RisWorkListRule(Base):
    __tablename__ = 'Ris_WorkListRule'

    WorkListRuleID = Column(Integer, primary_key=True, index=True)
    AETitleValue = Column(String(64, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    NeedInstanceUID = Column(Integer, nullable=False)
    ConvertFlag = Column(Integer, nullable=False)
    SplitName = Column(Integer, nullable=False)
    NeedBodyPart = Column(Integer, nullable=False)
    PrimaryBodyPartTag = Column(String(8, u'Chinese_PRC_CI_AS'))
    SubBodyPartTag = Column(String(8, u'Chinese_PRC_CI_AS'))
    ReportCondition = Column(String(512, u'Chinese_PRC_CI_AS'), nullable=False)
    Note = Column(String(255, u'Chinese_PRC_CI_AS'))
    ResultBodyPartCode = Column(String(10, u'Chinese_PRC_CI_AS'))


t_Ris_WorkListRule_SPS = Table(
    'Ris_WorkListRule_SPS', metadata,
    Column('WorkListRuleID', Integer, nullable=False),
    Column('AETitle', String(20, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('NeedInstanceUID', Integer, nullable=False),
    Column('SpecialCharacterSet', Integer, nullable=False),
    Column('BothChineseAndEnglish', Integer, nullable=False),
    Column('SplitName', Integer, nullable=False),
    Column('NeedStudyItem', Integer, nullable=False),
    Column('ReportCondition', String(512, u'Chinese_PRC_CI_AS'), nullable=False)
)


t_SF_YS_REPORT = Table(
    'SF_YS_REPORT', metadata,
    Column('xh', Integer, nullable=False),
    Column('repno', Integer, nullable=False),
    Column('reqno', String(12, u'Chinese_PRC_CI_AS')),
    Column('syxh', Integer),
    Column('patid', Integer),
    Column('blh', Integer),
    Column('CardNo', String(30, u'Chinese_PRC_CI_AS')),
    Column('hzxm', String(40, u'Chinese_PRC_CI_AS')),
    Column('sex', String(4, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('Age', Numeric(5, 2)),
    Column('sjksdm', String(12, u'Chinese_PRC_CI_AS')),
    Column('sjksmc', String(50, u'Chinese_PRC_CI_AS')),
    Column('bqdm', String(12, u'Chinese_PRC_CI_AS')),
    Column('bqmc', String(50, u'Chinese_PRC_CI_AS')),
    Column('cwdm', String(10, u'Chinese_PRC_CI_AS')),
    Column('sjysdm', String(12, u'Chinese_PRC_CI_AS')),
    Column('sjysxm', String(20, u'Chinese_PRC_CI_AS')),
    Column('sjrq', DateTime),
    Column('replb', String(20, u'Chinese_PRC_CI_AS')),
    Column('replbmc', String(40, u'Chinese_PRC_CI_AS')),
    Column('reprq', DateTime),
    Column('xtbz', String(12, u'Chinese_PRC_CI_AS')),
    Column('jcbw', String(1, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('jcysdm', String(12, u'Chinese_PRC_CI_AS')),
    Column('jcysxm', String(20, u'Chinese_PRC_CI_AS')),
    Column('jcksdm', String(12, u'Chinese_PRC_CI_AS')),
    Column('jcksmc', String(50, u'Chinese_PRC_CI_AS')),
    Column('isly', String(1, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('pubtime', DateTime),
    Column('fph', String(1, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('WardorReg', String(4, u'Chinese_PRC_CI_AS')),
    Column('Exectime', DateTime),
    Column('LogNo', String(20, u'Chinese_PRC_CI_AS')),
    Column('GroupNo', String(20, u'Chinese_PRC_CI_AS')),
    Column('LabelId', String(32, u'Chinese_PRC_CI_AS'))
)


t_Serials = Table(
    'Serials', metadata,
    Column('SerialName', String(40, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('SerialNo', Integer)
)


class SetWorkingDay(Base):
    __tablename__ = 'SetWorkingDay'

    Days = Column(DateTime, primary_key=True)
    Type = Column(String(1, u'Chinese_PRC_CI_AS'), nullable=False)


t_Settings = Table(
    'Settings', metadata,
    Column('SerialNo', Numeric(18, 0), nullable=False),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('Domain', Integer, nullable=False),
    Column('DomainName', String(20, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('Section', String(60, u'Chinese_PRC_CI_AS')),
    Column('Entry', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('DataType', String(40, u'Chinese_PRC_CI_AS')),
    Column('Value', String(250, u'Chinese_PRC_CI_AS')),
    Column('Visible', Integer, nullable=False),
    Column('Comment', String(250, u'Chinese_PRC_CI_AS')),
    Column('OrderNo', Integer),
    Index('idx_Settings_MuliInd', 'SubSysCode', 'Domain', 'DomainName', 'Section', 'Entry', unique=True)
)


t_SettingsDic = Table(
    'SettingsDic', metadata,
    Column('SerialNo', Numeric(18, 0), nullable=False),
    Column('SubSysCode', String(20, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('Domain', Integer, nullable=False),
    Column('Section', String(60, u'Chinese_PRC_CI_AS')),
    Column('Entry', String(50, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('DataType', String(40, u'Chinese_PRC_CI_AS')),
    Column('Value', String(250, u'Chinese_PRC_CI_AS')),
    Column('Visible', Integer, nullable=False),
    Column('Comment', String(250, u'Chinese_PRC_CI_AS')),
    Column('OrderNo', Integer),
    Index('idx_SettingsDic_MuliInd', 'SubSysCode', 'Domain', 'Section', 'Entry', unique=True)
)


class Slave(Base):
    __tablename__ = 'Slave'

    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    ClassCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    SlaveNo = Column(String(50, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    SlaveName = Column(String(50, u'Chinese_PRC_CI_AS'))
    ExternCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    MemCode1 = Column(String(8, u'Chinese_PRC_CI_AS'))
    MemCode2 = Column(String(8, u'Chinese_PRC_CI_AS'))
    Visible = Column(String(1, u'Chinese_PRC_CI_AS'))


class StaffAssessment(Base):
    __tablename__ = 'Staff_Assessment'

    SERIALNO = Column(Integer, primary_key=True)
    UserID = Column(String(12, u'Chinese_PRC_CI_AS'), nullable=False)
    UserName = Column(String(10, u'Chinese_PRC_CI_AS'))
    StartDate = Column(DateTime)
    EndDate = Column(DateTime)
    DeptNo = Column(String(12, u'Chinese_PRC_CI_AS'))
    DeptName = Column(String(50, u'Chinese_PRC_CI_AS'))
    AssessmentType = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    UserPosition = Column(String(20, u'Chinese_PRC_CI_AS'))
    subsyscode = Column(String(20, u'Chinese_PRC_CI_AS'))


t_StfA_FileList = Table(
    'StfA_FileList', metadata,
    Column('SERIALNO', Integer, nullable=False),
    Column('STFNO', Integer, nullable=False),
    Column('CREATEDATE', DateTime),
    Column('CreateUser', String(30, u'Chinese_PRC_CI_AS')),
    Column('VFILENAME', String(200, u'Chinese_PRC_CI_AS')),
    Column('VFILESIZE', String(20, u'Chinese_PRC_CI_AS')),
    Column('VFILETYPE', String(100, u'Chinese_PRC_CI_AS')),
    Column('VFILEMODIFYTIME', DateTime),
    Column('VFILEMEMO', String(2000, u'Chinese_PRC_CI_AS')),
    Column('LABDOC_ID', Integer)
)


class SubSysFunc(Base):
    __tablename__ = 'SubSysFunc'

    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    FuncCode = Column(String(50, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    FuncName = Column(String(100, u'Chinese_PRC_CI_AS'))
    ModuleName = Column(String(200, u'Chinese_PRC_CI_AS'))
    COMClass = Column(String(100, u'Chinese_PRC_CI_AS'))
    Params = Column(String(200, u'Chinese_PRC_CI_AS'))
    PageCode = Column(String(100, u'Chinese_PRC_CI_AS'))
    Powers = Column(String(1000, u'Chinese_PRC_CI_AS'))
    Menu = Column(String(50, u'Chinese_PRC_CI_AS'))
    MenuOrder = Column(String(20, u'Chinese_PRC_CI_AS'))
    Order1 = Column(Integer, server_default=text("(0)"))
    Order2 = Column(Integer, server_default=text("(0)"))
    AutoRun = Column(String(1, u'Chinese_PRC_CI_AS'))
    ReportID = Column(Integer)
    IsVisible = Column(Integer, server_default=text("(1)"))


class SubSysInfo(Base):
    __tablename__ = 'SubSysInfo'

    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True)
    SystemGroup = Column(String(20, u'Chinese_PRC_CI_AS'))
    SubSysName = Column(String(100, u'Chinese_PRC_CI_AS'))
    OrderNo = Column(Integer, nullable=False, server_default=text("('9')"))


class TechLog(Base):
    __tablename__ = 'TechLog'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    LogTime = Column(DateTime)
    LogContent = Column(String(2000, u'Chinese_PRC_CI_AS'))
    LogUser = Column(String(20, u'Chinese_PRC_CI_AS'))
    LogType = Column(String(20, u'Chinese_PRC_CI_AS'))
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'))


class ToolBarInfo(Base):
    __tablename__ = 'ToolBarInfo'

    SubsysCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    FuncCode = Column(String(50, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    LargeIcon = Column(LargeBinary)
    SmallIcon = Column(LargeBinary)
    SortIndex = Column(Integer)


class Tpldict(Base):
    __tablename__ = 'Tpldict'

    NodeID = Column(Integer, primary_key=True)
    Name = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False)
    ParentNodeID = Column(Integer, nullable=False)
    TplNo = Column(Integer)


class Tpl(Base):
    __tablename__ = 'Tpls'

    SerialNo = Column(Integer, nullable=False)
    TplNo = Column(Integer, primary_key=True, nullable=False)
    Entry = Column(String(80, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    DataType = Column(SmallInteger)
    Data = Column(String(1000, u'Chinese_PRC_CI_AS'))


class UserPlan(Base):
    __tablename__ = 'UserPlan'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    InputTime = Column(DateTime)
    HintTitle = Column(String(50, u'Chinese_PRC_CI_AS'))
    HintContent = Column(String(500, u'Chinese_PRC_CI_AS'))
    AlertTime = Column(DateTime)
    UserID = Column(String(20, u'Chinese_PRC_CI_AS'))


class UserRight(Base):
    __tablename__ = 'UserRight'

    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    GroupName = Column(String(50, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    UserID = Column(String(12, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False, index=True)
    InstID = Column(Integer, primary_key=True, nullable=False)


class User(Base):
    __tablename__ = 'Users'

    UserID = Column(String(12, u'Chinese_PRC_CI_AS'), primary_key=True)
    UserName = Column(String(20, u'Chinese_PRC_CI_AS'))
    Password = Column(String(64, u'Chinese_PRC_CI_AS'))
    DeptNo = Column(String(12, u'Chinese_PRC_CI_AS'))
    UserIME = Column(String(50, u'Chinese_PRC_CI_AS'))
    MemCode1 = Column(String(8, u'Chinese_PRC_CI_AS'))
    MemCode2 = Column(String(8, u'Chinese_PRC_CI_AS'))
    ExternCode = Column(String(20, u'Chinese_PRC_CI_AS'))
    UserType = Column(String(1000, u'Chinese_PRC_CI_AS'))
    StopUse = Column(String(1, u'Chinese_PRC_CI_AS'), server_default=text("('0')"))
    Phone = Column(String(20, u'Chinese_PRC_CI_AS'))
    Address = Column(String(80, u'Chinese_PRC_CI_AS'))
    AddressPhone = Column(String(20, u'Chinese_PRC_CI_AS'))
    eMail = Column(String(50, u'Chinese_PRC_CI_AS'))
    SignImage = Column(LargeBinary)
    OtherFlag = Column(Integer)
    LogNo = Column(String(50, u'Chinese_PRC_CI_AS'), server_default=text("('')"))


t_V_ImageDesc_2005 = Table(
    'V_ImageDesc_2005', metadata,
    Column('ApplyNo', Integer),
    Column('ImageDesc', String(92, u'Chinese_PRC_CI_AS'))
)


t_Version = Table(
    'Version', metadata,
    Column('SystemName', String(512, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ReleaseTime', DateTime, nullable=False),
    Column('InsertTime', DateTime, nullable=False)
)


class YYNEW(Base):
    __tablename__ = 'YY_NEWS'

    xh = Column(Integer, primary_key=True)
    czyh = Column(String(100, u'Chinese_PRC_CI_AS'), nullable=False)
    lrrq = Column(String(20, u'Chinese_PRC_CI_AS'))
    title = Column(String(100, u'Chinese_PRC_CI_AS'))
    news = Column(String(255, u'Chinese_PRC_CI_AS'), nullable=False)
    newsblob = Column(Text(2147483647, u'Chinese_PRC_CI_AS'))
    deadline = Column(String(20, u'Chinese_PRC_CI_AS'))
    tsxt = Column(Integer, nullable=False)
    tzks = Column(String(255, u'Chinese_PRC_CI_AS'))


t_com_WinningQQ_LeaveWord = Table(
    'com_WinningQQ_LeaveWord', metadata,
    Column('SeqNo', Integer, nullable=False),
    Column('UserID', String(20, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('LeaveWord', String(100, u'Chinese_PRC_CI_AS')),
    Column('FromUserID', String(20, u'Chinese_PRC_CI_AS')),
    Column('LeaveTime', DateTime),
    Column('ReadTime', DateTime)
)


t_com_WinningQQ_User = Table(
    'com_WinningQQ_User', metadata,
    Column('SeqNo', Integer, nullable=False),
    Column('UserID', String(20, u'Chinese_PRC_CI_AS')),
    Column('UserName', String(20, u'Chinese_PRC_CI_AS')),
    Column('QQPassword', String(500, u'Chinese_PRC_CI_AS')),
    Column('UserDesc', String(100, u'Chinese_PRC_CI_AS')),
    Column('ComputerName', String(200, u'Chinese_PRC_CI_AS')),
    Column('UserIcon', LargeBinary),
    Column('DeptName', String(50, u'Chinese_PRC_CI_AS')),
    Column('LastTime', DateTime)
)


class Dtproperty(Base):
    __tablename__ = 'dtproperties'

    id = Column(Integer, primary_key=True, nullable=False)
    objectid = Column(Integer)
    property = Column(String(64, u'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    value = Column(String(255, u'Chinese_PRC_CI_AS'))
    uvalue = Column(Unicode(255))
    lvalue = Column(LargeBinary)
    version = Column(Integer, nullable=False, server_default=text("(0)"))


t_pacs_IFResult = Table(
    'pacs_IFResult', metadata,
    Column('ID_Key', Integer, nullable=False, index=True),
    Column('IFHost', String(200, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('IFAETitle', String(200, u'Chinese_PRC_CI_AS')),
    Column('StudyID', Integer, nullable=False, index=True),
    Column('SeriesID', Integer, nullable=False, index=True),
    Column('ImageID', Integer, nullable=False, index=True),
    Column('Target', String(200, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('InsertTime', DateTime),
    Column('ReSend', Integer),
    Column('Status', String(50, u'Chinese_PRC_CI_AS')),
    Column('TryTimes', Integer),
    Index('index_pacs_IFResult_imageid_Target', 'ImageID', 'Target')
)


t_pacs_IF_task_list = Table(
    'pacs_IF_task_list', metadata,
    Column('ID_Key', Integer, nullable=False, index=True),
    Column('IFRuleid', Integer),
    Column('IFHost', String(200, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('IFAETitle', String(200, u'Chinese_PRC_CI_AS')),
    Column('IFID', Integer, nullable=False, index=True),
    Column('IDType', Integer, nullable=False),
    Column('Target', String(200, u'Chinese_PRC_CI_AS'), nullable=False)
)


t_pv_GetDate = Table(
    'pv_GetDate', metadata,
    Column('CurrentDateTime', DateTime, nullable=False)
)


t_ris_SR_Record = Table(
    'ris_SR_Record', metadata,
    Column('ApplyNo', Integer, nullable=False),
    Column('SR_StudyUID', String(128, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('SR_SeriesUID', String(128, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('SR_SopInstanceUID', String(128, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('Status', Integer, nullable=False)
)


t_ris_SR_Temp = Table(
    'ris_SR_Temp', metadata,
    Column('ApplyNo', Integer, nullable=False)
)


class RisSurveyDetail(Base):
    __tablename__ = 'ris_SurveyDetail'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    ApplyNo = Column(Integer, nullable=False, index=True)
    ItemCode = Column(String(10, u'Chinese_PRC_CI_AS'), nullable=False, index=True)
    ItemName = Column(String(40, u'Chinese_PRC_CI_AS'), nullable=False)
    ItemResult = Column(String(7000, u'Chinese_PRC_CI_AS'))


class RisSurveyRecord(Base):
    __tablename__ = 'ris_SurveyRecord'

    SurveyID = Column(Integer, primary_key=True)
    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    TechPatID = Column(Integer, nullable=False, index=True)
    ApplyNo = Column(Integer)
    PatName = Column(String(40, u'Chinese_PRC_CI_AS'), index=True)
    PatNameSpell = Column(String(40, u'Chinese_PRC_CI_AS'))
    PatientID = Column(Integer)
    CureNo = Column(Integer)
    CardNo = Column(String(30, u'Chinese_PRC_CI_AS'), index=True)
    InpatientNum = Column(String(16, u'Chinese_PRC_CI_AS'))
    OutpatientNum = Column(String(16, u'Chinese_PRC_CI_AS'))
    WardOrReg = Column(String(12, u'Chinese_PRC_CI_AS'))
    HospNo = Column(String(20, u'Chinese_PRC_CI_AS'))
    Sex = Column(String(1, u'Chinese_PRC_CI_AS'))
    Age = Column(Numeric(5, 2))
    AgeUnit = Column(String(6, u'Chinese_PRC_CI_AS'))
    Birthday = Column(DateTime)
    Occupation = Column(String(30, u'Chinese_PRC_CI_AS'))
    Phone = Column(String(20, u'Chinese_PRC_CI_AS'))
    Address = Column(String(100, u'Chinese_PRC_CI_AS'))
    Zip = Column(String(6, u'Chinese_PRC_CI_AS'))
    Nation = Column(String(20, u'Chinese_PRC_CI_AS'))
    IDNum = Column(String(20, u'Chinese_PRC_CI_AS'))
    ApplyDept = Column(String(12, u'Chinese_PRC_CI_AS'))
    ApplyDeptName = Column(String(50, u'Chinese_PRC_CI_AS'))
    AttendingPhysicianCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    AttendingPhysicianName = Column(String(20, u'Chinese_PRC_CI_AS'))
    BriefCase = Column(String(255, u'Chinese_PRC_CI_AS'))
    ClinicDesc = Column(String(255, u'Chinese_PRC_CI_AS'))
    SurveyDate = Column(DateTime, index=True)
    SurveyorCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    SurveyorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    VerifyDate = Column(DateTime)
    VerifierCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    VerifierName = Column(String(20, u'Chinese_PRC_CI_AS'))
    EditorCode = Column(String(12, u'Chinese_PRC_CI_AS'))
    EditorName = Column(String(20, u'Chinese_PRC_CI_AS'))
    CreateTime = Column(DateTime)
    SaveTime = Column(DateTime)
    PrintFlag = Column(Integer, server_default=text("(0)"))
    DeleteFlag = Column(Integer, server_default=text("(0)"))
    TechNo = Column(String(20, u'Chinese_PRC_CI_AS'))
    Reportid = Column(Integer)


class RisSurveyReportRelation(Base):
    __tablename__ = 'ris_SurveyReportRelation'

    SerialNo = Column(Numeric(18, 0), primary_key=True)
    SurveyID = Column(Integer, nullable=False, index=True)
    ApplyNo = Column(Integer, nullable=False)
    Region = Column(String(50, u'Chinese_PRC_CI_AS'))
    QualitativeAgreement = Column(Integer, server_default=text("(0)"))
    PositionalAgreement = Column(Integer, server_default=text("(0)"))


t_ris_TeachDicRecord = Table(
    'ris_TeachDicRecord', metadata,
    Column('TeachId', Integer, nullable=False, unique=True),
    Column('ApplyNo', Integer, nullable=False, index=True),
    Column('Reportid', Integer, nullable=False),
    Column('Type', Integer),
    Column('CollectTime', DateTime),
    Column('collectionDoctor', String(20, u'Chinese_PRC_CI_AS')),
    Column('collectionDoctorName', String(50, u'Chinese_PRC_CI_AS')),
    Column('CompeleteTime', DateTime),
    Column('CompeleteDoctor', String(50, u'Chinese_PRC_CI_AS')),
    Column('CompeleteDoctorName', String(50, u'Chinese_PRC_CI_AS')),
    Column('VerifyTime', DateTime),
    Column('VerifyDoctor', String(50, u'Chinese_PRC_CI_AS')),
    Column('VerifyDoctorName', String(50, u'Chinese_PRC_CI_AS')),
    Column('PurposeType', String(800, u'Chinese_PRC_CI_AS')),
    Column('DiseaseType', String(50, u'Chinese_PRC_CI_AS')),
    Column('DiseaseTypeName', String(500, u'Chinese_PRC_CI_AS')),
    Column('Status', Integer),
    Column('SubsysCode', String(50, u'Chinese_PRC_CI_AS')),
    Column('FindFlag', String(300, u'Chinese_PRC_CI_AS')),
    Column('HisToryAndExam', LargeBinary),
    Column('imagefeatures', LargeBinary),
    Column('review', LargeBinary),
    Column('ShareUserID', String(300, u'Chinese_PRC_CI_AS')),
    Column('ShareUserName', String(300, u'Chinese_PRC_CI_AS'))
)


class RisTemplateLibDic(Base):
    __tablename__ = 'ris_TemplateLibDic'

    SubSysCode = Column(String(20, u'Chinese_PRC_CI_AS'), nullable=False)
    LibraryID = Column(Integer, primary_key=True)
    LibraryName = Column(String(60, u'Chinese_PRC_CI_AS'), nullable=False)


t_vAllAcceptItemsData = Table(
    'vAllAcceptItemsData', metadata,
    Column('SerialNo', Integer, nullable=False),
    Column('ApplyNo', Integer, nullable=False),
    Column('HISApplyNo', String(20, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ItemCode', String(20, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ItemName', String(40, u'Chinese_PRC_CI_AS')),
    Column('Price', MONEY),
    Column('Price2', MONEY),
    Column('ItemQty', Numeric(8, 2)),
    Column('ReceiveTime', DateTime),
    Column('OperatorCode', String(12, u'Chinese_PRC_CI_AS')),
    Column('OperatorName', String(20, u'Chinese_PRC_CI_AS')),
    Column('Status', String(1, u'Chinese_PRC_CI_AS')),
    Column('GroupNo', String(20, u'Chinese_PRC_CI_AS')),
    Column('LogNo', String(20, u'Chinese_PRC_CI_AS')),
    Column('ApplyDocCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('ApplyDept', String(20, u'Chinese_PRC_CI_AS')),
    Column('ExecDept', String(20, u'Chinese_PRC_CI_AS')),
    Column('ApplyTime', DateTime),
    Column('ItemUnit', String(20, u'Chinese_PRC_CI_AS')),
    Column('AddType', String(1, u'Chinese_PRC_CI_AS')),
    Column('ItemType', String(1, u'Chinese_PRC_CI_AS')),
    Column('ChargeFlag', String(1, u'Chinese_PRC_CI_AS')),
    Column('Content', String(200, u'Chinese_PRC_CI_AS')),
    Column('ghxh', String(30, u'Chinese_PRC_CI_AS'))
)


t_vAllBookingInfo = Table(
    'vAllBookingInfo', metadata,
    Column('ApplyNo', Integer, nullable=False),
    Column('RegisterCode', String(12, u'Chinese_PRC_CI_AS')),
    Column('RegisterName', String(20, u'Chinese_PRC_CI_AS')),
    Column('AttentionCode', String(20, u'Chinese_PRC_CI_AS')),
    Column('BookNo', Integer),
    Column('DSID', Integer)
)


t_vAllListData = Table(
    'vAllListData', metadata,
    Column('ApplyNo', Integer, nullable=False),
    Column('TechNo', String(20, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ExecTime', DateTime),
    Column('LabelID', String(32, u'Chinese_PRC_CI_AS')),
    Column('TechPatID', Integer),
    Column('PatName', String(40, u'Chinese_PRC_CI_AS')),
    Column('PatNameSpell', String(40, u'Chinese_PRC_CI_AS')),
    Column('PatientID', Integer),
    Column('CureNo', Integer),
    Column('CardNo', String(30, u'Chinese_PRC_CI_AS')),
    Column('HospNo', String(20, u'Chinese_PRC_CI_AS')),
    Column('Sex', String(1, u'Chinese_PRC_CI_AS')),
    Column('Age', Numeric(5, 2)),
    Column('AgeUnit', String(6, u'Chinese_PRC_CI_AS')),
    Column('Birthday', DateTime),
    Column('Career', String(30, u'Chinese_PRC_CI_AS')),
    Column('Phone', String(20, u'Chinese_PRC_CI_AS')),
    Column('Address', String(100, u'Chinese_PRC_CI_AS')),
    Column('Zip', String(6, u'Chinese_PRC_CI_AS')),
    Column('Nation', String(20, u'Chinese_PRC_CI_AS')),
    Column('IDNum', String(20, u'Chinese_PRC_CI_AS')),
    Column('ChargeType', String(12, u'Chinese_PRC_CI_AS')),
    Column('ChargeTypeName', String(50, u'Chinese_PRC_CI_AS')),
    Column('ApplyDept', String(12, u'Chinese_PRC_CI_AS')),
    Column('ApplyDeptName', String(50, u'Chinese_PRC_CI_AS')),
    Column('Ward', String(12, u'Chinese_PRC_CI_AS')),
    Column('WardName', String(50, u'Chinese_PRC_CI_AS')),
    Column('BedNo', String(10, u'Chinese_PRC_CI_AS')),
    Column('WardOrReg', String(12, u'Chinese_PRC_CI_AS')),
    Column('ApplyTime', DateTime),
    Column('BriefCase', String(255, u'Chinese_PRC_CI_AS')),
    Column('ClinicDesc', String(255, u'Chinese_PRC_CI_AS')),
    Column('AcceptTime', DateTime),
    Column('ApplyDoctor', String(12, u'Chinese_PRC_CI_AS')),
    Column('ApplyDoctorName', String(20, u'Chinese_PRC_CI_AS')),
    Column('Accepter', String(12, u'Chinese_PRC_CI_AS')),
    Column('AccepterName', String(20, u'Chinese_PRC_CI_AS')),
    Column('ExecDoctor1', String(12, u'Chinese_PRC_CI_AS')),
    Column('ExecDoctor1Name', String(20, u'Chinese_PRC_CI_AS')),
    Column('ExecDoctor2', String(12, u'Chinese_PRC_CI_AS')),
    Column('ExecDoctor2Name', String(20, u'Chinese_PRC_CI_AS')),
    Column('QualityDoctor', String(12, u'Chinese_PRC_CI_AS')),
    Column('QualityDoctorName', String(20, u'Chinese_PRC_CI_AS')),
    Column('VerifyDoctor', String(12, u'Chinese_PRC_CI_AS')),
    Column('VerifyDoctorName', String(20, u'Chinese_PRC_CI_AS')),
    Column('ReportDoctor', String(12, u'Chinese_PRC_CI_AS')),
    Column('ReportDoctorName', String(20, u'Chinese_PRC_CI_AS')),
    Column('ReportWriter', String(12, u'Chinese_PRC_CI_AS')),
    Column('ReportWriterName', String(20, u'Chinese_PRC_CI_AS')),
    Column('FinallyEditDoctor', String(12, u'Chinese_PRC_CI_AS')),
    Column('FinallyEditDoctorName', String(20, u'Chinese_PRC_CI_AS')),
    Column('FinallyEditTime', DateTime),
    Column('AuditingTime', DateTime),
    Column('PublicTime', DateTime),
    Column('ReportID', Integer),
    Column('ReportTime', DateTime),
    Column('Instrument', String(50, u'Chinese_PRC_CI_AS')),
    Column('OrgApplyNo', String(12, u'Chinese_PRC_CI_AS')),
    Column('Status', Integer, nullable=False),
    Column('LockFlag', Integer),
    Column('Locker', String(30, u'Chinese_PRC_CI_AS')),
    Column('PrintFlag', Integer),
    Column('DeleteFlag', Integer),
    Column('ChargeFlag', Integer),
    Column('HavingImages', SmallInteger),
    Column('EngName', String(100, u'Chinese_PRC_CI_AS')),
    Column('EquipmentID', String(10, u'Chinese_PRC_CI_AS')),
    Column('Invoice', String(20, u'Chinese_PRC_CI_AS')),
    Column('ImageTime', DateTime),
    Column('DpSign', Integer),
    Column('dpsuggest', String(50, u'Chinese_PRC_CI_AS')),
    Column('ExamTime', DateTime),
    Column('BookCenterSID', Integer),
    Column('CrisisFlag', Integer),
    Column('SurveySign', Integer),
    Column('SurveySuggest', String(50, u'Chinese_PRC_CI_AS')),
    Column('JCBZ', Integer),
    Column('ExamFlag', Integer)
)


t_vAllResultData = Table(
    'vAllResultData', metadata,
    Column('SerialNo', Numeric(18, 0), nullable=False),
    Column('ApplyNo', Integer, nullable=False),
    Column('ItemCode', String(10, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ItemName', String(40, u'Chinese_PRC_CI_AS'), nullable=False),
    Column('ItemResult', String(7000, u'Chinese_PRC_CI_AS'))
)


class VRISResultRISBL(Base):
    __tablename__ = 'v_RIS_Result_RIS_BL'

    ApplyNo = Column(Integer, primary_key=True)
    BBZL = Column(String(100, u'Chinese_PRC_CI_AS'))
    BW = Column(String(100, u'Chinese_PRC_CI_AS'))
    JCSJ = Column(String(2000, u'Chinese_PRC_CI_AS'))
    JSSP = Column(String(100, u'Chinese_PRC_CI_AS'))


class VRISResultRISC(Base):
    __tablename__ = 'v_RIS_Result_RIS_CS'

    ApplyNo = Column(Integer, primary_key=True)
    BRSF = Column(String(100, u'Chinese_PRC_CI_AS'))
    BW = Column(String(100, u'Chinese_PRC_CI_AS'))
    DXBL = Column(String(100, u'Chinese_PRC_CI_AS'))
    JCJL = Column(String(2000, u'Chinese_PRC_CI_AS'))
    JCSJ = Column(String(2000, u'Chinese_PRC_CI_AS'))
    JLFS = Column(String(100, u'Chinese_PRC_CI_AS'))
    TTPL = Column(String(100, u'Chinese_PRC_CI_AS'))
    TX = Column(String(100, u'Chinese_PRC_CI_AS'))
    TXZL = Column(String(100, u'Chinese_PRC_CI_AS'))


class VRISResultRISF(Base):
    __tablename__ = 'v_RIS_Result_RIS_FS'

    ApplyNo = Column(Integer, primary_key=True)
    BW = Column(String(100, u'Chinese_PRC_CI_AS'))
    JCJL = Column(String(2000, u'Chinese_PRC_CI_AS'))
    JCSJ = Column(String(2000, u'Chinese_PRC_CI_AS'))


class VRISResultRISHY(Base):
    __tablename__ = 'v_RIS_Result_RIS_HY'

    ApplyNo = Column(Integer, primary_key=True)
    JCBW = Column(String(100, u'Chinese_PRC_CI_AS'))
    JCFS = Column(String(100, u'Chinese_PRC_CI_AS'))
    JCYW = Column(String(100, u'Chinese_PRC_CI_AS'))
    JCSJ = Column(String(2000, u'Chinese_PRC_CI_AS'))


class VRISResultRISND(Base):
    __tablename__ = 'v_RIS_Result_RIS_ND'

    ApplyNo = Column(Integer, primary_key=True)
    BW = Column(String(100, u'Chinese_PRC_CI_AS'))
    JCJL = Column(String(100, u'Chinese_PRC_CI_AS'))
    JCSJ = Column(String(100, u'Chinese_PRC_CI_AS'))


class VRISResultRISNJ(Base):
    __tablename__ = 'v_RIS_Result_RIS_NJ'

    ApplyNo = Column(Integer, primary_key=True)
    BLH = Column(String(100, u'Chinese_PRC_CI_AS'))
    BLZD = Column(String(100, u'Chinese_PRC_CI_AS'))
    JCJL = Column(String(100, u'Chinese_PRC_CI_AS'))
    JCSJ = Column(String(2000, u'Chinese_PRC_CI_AS'))
    XBS = Column(String(100, u'Chinese_PRC_CI_AS'))
    HJBW = Column(String(100, u'Chinese_PRC_CI_AS'))


class VRISResultRISXD(Base):
    __tablename__ = 'v_RIS_Result_RIS_XD'

    ApplyNo = Column(Integer, primary_key=True)
    JCJL = Column(String(2000, u'Chinese_PRC_CI_AS'))
    JCSJ = Column(String(2000, u'Chinese_PRC_CI_AS'))
    SJJL = Column(String(2000, u'Chinese_PRC_CI_AS'))
