from dicom._dicom_dict import DicomDictionary


sortkey =  sorted(DicomDictionary.keys())

for key in sortkey:
    s = '%08x'%(key)
    a,b,c,d,e = DicomDictionary[key]
    print s[:4],',',s[-4:],' ',e#,' ',c
    #DicomDictionary[key]

