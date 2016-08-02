







import os
if os.name == 'nt':
    import win32api


def Disk_Info(VolumeName):
    try:
        if os.name == 'nt':
            a = win32api.GetDiskFreeSpaceEx(VolumeName)
            return a[0]/1024/1024/1024, a[1]/1024/1024/1024
    except Exception as e:
        print e
        return None

print Disk_Info('D:')
