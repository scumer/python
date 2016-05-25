# coding=utf-8

import imp

hook_modname = 'PyInstaller_hooks_PyQt5_QtCore'
filename = 'D:\\Program Files\\Python27\\lib\\site-packages\\pyinstaller-3.0-py2.7.egg\\PyInstaller\\hooks\\' \
           'hook-PyQt5.QtCore.py'
module = imp.load_source(hook_modname, filename)

# print module
# print module.binaries

from PyInstaller.utils.hooks import qt5_plugins_binaries, qt5_plugins_dir, qt4_plugins_dir, eval_statement

print qt5_plugins_dir()

binaries = []
binaries.extend(qt5_plugins_binaries('accessible'))
binaries.extend(qt5_plugins_binaries('iconengines'))
binaries.extend(qt5_plugins_binaries('imageformats'))
binaries.extend(qt5_plugins_binaries('inputmethods'))
binaries.extend(qt5_plugins_binaries('graphicssystems'))
binaries.extend(qt5_plugins_binaries('platforms'))

# print binaries

import os
PACKAGEPATH = os.path.abspath(os.path.dirname(__file__))
HOMEPATH = os.path.dirname(PACKAGEPATH)
# print HOMEPATH
# print os.pathsep.join(['E:'] + [HOMEPATH])
print 'QT_PLUGIN_PATH' in os.environ

def qt5_plugins_dir_my():
    if 'QT_PLUGIN_PATH' in os.environ and os.path.isdir(os.environ['QT_PLUGIN_PATH']):
        return str(os.environ['QT_PLUGIN_PATH'])

    qt5_plugin_dirs = eval_statement(
        "from PyQt5.QtCore import QCoreApplication;"
        "app=QCoreApplication([]);"
        # For Python 2 print would give "<PyQt4.QtCore.QStringList
        # object at 0x....>", so we need to convert each element separately
        "str=getattr(__builtins__, 'unicode', str);" # for Python 2
        "print([str(p) for p in app.libraryPaths()])")
    if not qt5_plugin_dirs:
        print ("Cannot find PyQt5 plugin directories")
        return ""
    for d in qt5_plugin_dirs:
        if os.path.isdir(d):
            return str(d)  # must be 8-bit chars for one-file builds
    print("Cannot find existing PyQt5 plugin directory")
    return ""

#print qt5_plugins_dir_my()

# from PyQt4.QtCore import QCoreApplication
# app=QCoreApplication([])
# str=getattr(__builtins__, 'unicode', str)
# print([str(p) for p in app.libraryPaths()])
# [u'D:/Program Files/Python27/Lib/site-packages/PyQt4/plugins',
# u'D:/Program Files/Python27']

# from PyQt5.QtCore import QCoreApplication
# app=QCoreApplication([])
# str=getattr(__builtins__, 'unicode', str)
# print([str(p) for p in app.libraryPaths()])
# [u'D:/Program Files/Python27/Lib/site-packages/PyQt4/plugins',
# u'D:/Program Files/Python27',
# u'D:/Program Files/Python27/lib/site-packages/PyQt5/plugins']


def qt4_plugins_dir_my(ns='PyQt4'):
    qt4_plugin_dirs = eval_statement(
        "from %s.QtCore import QCoreApplication;"
        "app=QCoreApplication([]);"
        # For Python 2 print would give "<PyQt4.QtCore.QStringList
        # object at 0x....>", so we need to convert each element separately
        "str=getattr(__builtins__, 'unicode', str);" # for Python 2
        "print([str(p) for p in app.libraryPaths()])" % ns)
    if not qt4_plugin_dirs:
        print ('Cannot find %s plugin directories' % ns)
        return ""
    for d in qt4_plugin_dirs:
        if os.path.isdir(d):
            return str(d)  # must be 8-bit chars for one-file builds
    print ('Cannot find existing %s plugin directory' % ns)
    return ""
# print module.__dict__


# hook_modname_qt4 = 'PyInstaller_hooks_PyQt4_QtCore'
# filename_qt4 = 'D:\\Program Files\\Python27\\lib\\site-packages\\pyinstaller-3.0-py2.7.egg\\PyInstaller\\hooks\\' \
#            'hook-PyQt4.QtCore.py'
# module = imp.load_source(hook_modname_qt4, filename_qt4)
#
# print module
# print module.binaries
