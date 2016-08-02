import accessdataTA as ta

studyUID = '1.3.6.1.4.1.19439.0.108707908.20101009113616.1737.1328696'
seriesUID = '1.3.12.2.1107.5.1.4.50632.30000010100902082148400004680'
sopUID = '1.3.12.2.1107.5.1.4.50632.30000010100902082148400004685'

print ta.initialize('WADO')

#imageinfos = ta.getStudyLocalFileList(studyUID)
#print imageinfos

imginf = ta.getImage(studyUID, seriesUID, sopUID)
print imginf.SrcFile