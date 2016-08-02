++++++++++++++++++++++++++++++++++++++++++++++

服务名称：
    THDataUP(64位) (Windows Service Name : THDataUP)

功能：
    轮询表Ris_Interface_PatientInfo和Ris_Interface_TaskInfo_XD(心电报告)，将相应的病人卡信息、报告数据、相关联的影像数据按照一定格式要求上传到PACS+平台

描述：
    1.Ris_Interface_PatientInfo中的CardState和Ris_Interface_TaskInfo_XD中的ReportState、ImageState，
    记录数据上传的状态：0：未处理 1：上传成功 2：上传失败 3：重试上传失败(不再重试)

    2.卡信息上传条件是:CardState = (0,2)
    Report上传的条件是可以在病人卡记录中找到相应的病人信息，且ReportState = (0,2)
    胶片信息上传的条件是ReportState=0，且在Pacs_Study、Pacs_Series、Pacs_Image表中找到对应的UID信息，且最近的入库时间在1分钟以前(参考存储过程tsp_QueryFilmTask)

服务配置：
    #数据库配置
    [DBConnect]
    Server = IP[:PORT]    # 数据库连接地址，若使用默认端口1433，端口可不写
    DataBase = DBName     # 数据库名
    DBUser= UserName      # 
    DBPassword=           # 密文模式

    #服务配置
    [Service]
    #UploadURL =          # 平台地址，如无特别要求，默认不填
    #Proxy = http://<IP>:<PORT> # 如果需要使用代理，配置代理地址

安装启动:
    双击运行start.cmd,安装并启动服务

    (若提示拒绝访问，以管理员身份运行)
    (安装服务前，确保服务器已经安装vcredist_x64,否则安装报错)

    




