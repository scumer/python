
/****** Object: Table [dbo].[Ris_Interface_TaskInfo_XD] ******/
if not exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[Ris_Interface_TaskInfo_XD]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
begin
	CREATE TABLE [dbo].[Ris_Interface_TaskInfo_XD](
		[id] [int] IDENTITY(1,1) NOT NULL,
		[Studyuid] [varchar](128) NOT NULL,
		[ReportState] [int] NOT NULL,
		[ImageState] [int] NOT NULL,
		[CardNo] [varchar](50) NOT NULL,
		[PatName] [varchar](50) NOT NULL,
		[ApplyNo] [varchar](50) NOT NULL,
		[Sex] [varchar](8) NOT NULL,
		[Age] [varchar](20) NOT NULL,
		[BirthDay] [datetime] NULL,
		[HospNo] [varchar](50) NULL,
		[LabelID] [varchar](50) NULL,
		[InsertTime] [datetime] NOT NULL,
		[ModifyTimeR] [datetime] NOT NULL,
		[ModifyTimeI] [datetime] NOT NULL,
		[ApplyDeptName] [varchar](50) NULL,
		[WardName] [varchar](50) NULL,
		[BedNo] [varchar](50) NULL,
		[TechNo] [varchar](50) NOT NULL,
		[ExecTime] [datetime] NOT NULL,
		[InstName] [varchar](50) NOT NULL,
		[StudyItem] [varchar](50) NOT NULL,
		[StudyObservation] [varchar](256) NOT NULL,
		[StudyResult] [varchar](256) NOT NULL,
		[ReportDoctorName] [varchar](50) NOT NULL,
		[VerifyDoctorName] [varchar](50) NOT NULL,
		[ReportTime] [datetime] NOT NULL,
		[VerifyTime] [datetime] NOT NULL,
		[HR] [int] NULL,
		[PR] [float] NULL,
		[QT] [float] NULL,
		[QTC] [float] NULL,
		[P] [float] NULL,
		[T] [float] NULL,
		[QRS] [float] NULL,
		[QRSaxis] [float] NULL,
		[Paxis] [float] NULL,
		[Taxis] [float] NULL,
		[SV1] [float] NULL,
		[RV5] [float] NULL,
	 CONSTRAINT [PK_Ris_Interface_TaskInfo_XD] PRIMARY KEY CLUSTERED 
	(
		[id] ASC
	)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
	) ON [PRIMARY]


	ALTER TABLE [dbo].[Ris_Interface_TaskInfo_XD] ADD  
		CONSTRAINT [DF_Ris_Interface_TaskInfo_XD_ReportState]  DEFAULT ((0)) FOR [ReportState],
		CONSTRAINT [DF_Ris_Interface_TaskInfo_XD_ImageState]  DEFAULT ((0)) FOR [ImageState],
		CONSTRAINT [DF_Ris_Interface_TaskInfo_XD_InsertTime]  DEFAULT (getdate()) FOR [InsertTime],
		CONSTRAINT [DF_Ris_Interface_TaskInfo_XD_ModifyTimeR]  DEFAULT (getdate()) FOR [ModifyTimeR],
		CONSTRAINT [DF_Ris_Interface_TaskInfo_XD_ModifyTimeI]  DEFAULT (getdate()) FOR [ModifyTimeI]


	CREATE INDEX [IX_Ris_Interface_TaskInfo_XD_Card] ON [dbo].[Ris_Interface_TaskInfo_XD](CardNo,PatName)
	CREATE INDEX [IX_Ris_Interface_TaskInfo_XD_State] ON [dbo].[Ris_Interface_TaskInfo_XD](ReportState,ImageState)
	CREATE UNIQUE INDEX [IX_Ris_Interface_TaskInfo_XD_ApplyNO] ON [dbo].[Ris_Interface_TaskInfo_XD](ApplyNo)
end


/****** Object:  Table [dbo].[Ris_Interface_PatientInfo]    Script Date: 07/05/2016 17:23:13 ******/

if not exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[Ris_Interface_PatientInfo]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
begin
	CREATE TABLE [dbo].[Ris_Interface_PatientInfo](
		[id] [int] IDENTITY(1,1) NOT NULL,
		[CardNo] [varchar](50) NOT NULL,
		[PatName] [varchar](50) NOT NULL,
		[PatNameSpell] [varchar](50) NOT NULL,
		[Sex] [varchar](10) NOT NULL,
		[Phone] [varchar](20) NULL,
		[IDNum] [varchar](50) NULL,
		[HospitalCode] [varchar](20) NOT NULL,
		[CityCode] [varchar](10) NOT NULL,
		[CardState] [int] NOT NULL,
		[InsertTime] [datetime] NOT NULL,
		[ModifyTime] [datetime] NOT NULL,
	 CONSTRAINT [PK_Ris_Interface_PatientInfo] PRIMARY KEY CLUSTERED 
	(
		[id] ASC
	)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
	) ON [PRIMARY]

	ALTER TABLE [dbo].[Ris_Interface_PatientInfo] ADD 
		CONSTRAINT [DF_Ris_Interface_PatientInfo_CardState]  DEFAULT ((0)) FOR [CardState],
		CONSTRAINT [DF_Ris_Interface_PatientInfo_InsertTime]  DEFAULT (getdate()) FOR [InsertTime],
		CONSTRAINT [DF_Ris_Interface_PatientInfo_ModifyTime]  DEFAULT (getdate()) FOR [ModifyTime]

	CREATE NONCLUSTERED INDEX [IX_Ris_Interface_PatInfo] ON [dbo].[Ris_Interface_PatientInfo](CardNo,PatName)
	CREATE UNIQUE NONCLUSTERED INDEX [IX_Ris_Interface_PatCard] ON [dbo].[Ris_Interface_PatientInfo](CardNo,PatName,Sex,CityCode,HospitalCode)
end