/****** Object:  StoredProcedure [dbo].[tsp_QueryFilmTask]    Script Date: 07/07/2016 10:28:32 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


/* ===============================================
tsp_QueryFilmTask

功能：获取第三方报告关联的影像信息。
作者：X.H.
创建日期：2016-07-07

输入参数：
@i_TaskName varchar(50) -- 任务队列名称
@i_Count int=3  -- 0:返回所有符合条件的记录，其它:返回3条记录(可以改成根据i_Count返回相应的数量)
================================================*/
create procedure [dbo].[tsp_QueryFilmTask]
@i_TaskName varchar(50)='',
@i_Count int = 3
as 
begin
	if ISNULL(@i_TaskName,'')=''
		set @i_TaskName = 'Ris_Interface_TaskInfo_XD'
		
	create table #task
	(
		id int,
		ImageState int,
		StudyUID varchar(128),
		SeriesUID varchar(128),
		ObjectUID varchar(128),
		PatName varchar(50),
		Age varchar(50),
		Sex varchar(50),
		LabelID varchar(256),
		TechNo varchar(256),
		HospitalCode varchar(50),
	)
	
	declare @exec_sql varchar(1000)
	set @exec_sql = 
		'
			insert into #task select * from
			(select A.id,A.ImageState,A.StudyUID,D.SeriesUID,E.ImageUID,A.PatName,A.Age,A.Sex,A.StudyUID as LabelID,A.StudyUID as TechNo,B.HospitalCode
			from ' +@i_TaskName+ ' as A, Ris_Interface_PatientInfo B, Pacs_Study C, Pacs_Series D, Pacs_Image E
			where A.ReportState=1
			and A.ImageState in (0,2)
			and A.Studyuid=C.StudyUID
			and A.PatName=B.PatName
			and A.CardNo = B.CardNo
			and C.StudyID = D.StudyID
			and C.StudyID = E.StudyID
			and C.TakeinTime < dateadd(mi, -1, getdate())
			and E.SeriesID = D.SeriesID 
			and E.DataStatus=1
			and E.CancelFlag = 0) as tasklist
		'
	print @exec_sql
	exec(@exec_sql)
	
	if @i_Count != 0
		select top 3 * from #task where id=(select distinct top 1 id from #task)
	else
		select * from #task where id=(select distinct top 1 id from #task)
		
	drop table #task
	return 0
end









