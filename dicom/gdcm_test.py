"""
Test Gdcm
"""

import gdcm
import sys

if __name__ == "__main__":

    #Get the file namefrom the command line
    #filename = sys.argv[1]
    filename = "E:/PACS_Program/DCM/16/277.dcm"

    #instanciate a gdcm.reader
    r = gdcm.Reader()
    r.SetFileName( filename )
    if not r.Read():
        print "Not a valid DICOM file"
        sys.exit(1)

    #Get file structure
    file = r.GetFile()

    #Get dataset part of file
    dataset = file.GetDataSet()

    #print it
    #print dataset

    #Use StringFilter to print a Tag:
    sf = gdcm.StringFilter()
    sf.SetFile(r.GetFile())

    #Check if Attribute exist
    #print dataset.FindDataElement(gdcm.Tag(0x0028, 0x0010))

    #Let's print it ad string pair
   # print sf.ToStringPair(gdcm.Tag(0x0010, 0x0010))


    #try C-Echo
    echoRq = gdcm.CompositeNetworkFunctions()
    if echoRq.CEcho('xuhui-pc', 1040):
        print "Echo Success!"
    else:
        print "Echo Failed!"
