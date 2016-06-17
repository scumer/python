# -*- coding: utf-8 -*-

"""
删除指定目录及目录下所有文件，递归单个文件删除
"""
import os
import stat
import sys

# os.remove(path)
# os.rmdir(path)
# os.path.dirname()

# filecnt = sum([len(files) for root, dirs, files in os.walk(pathname)]) # 获取目录文件总数
# dircnt = sum([len(dirs) for root, dirs, files in os.walk(pathname)]) # 获取目录文件总数
# print u'目录总数:', dircnt
# print u'文件总数:', filecnt

def main():
	try:
		failedfile = []
		pathname = ''
		"""获取目录名称"""
		if len(sys.argv) > 1:
			pathname = sys.argv[1]
			pathname = pathname.strip("\" \t\r\n")
		else:
			print u'输入需要删除的目录或文件名称:',
			pathname = raw_input()
			pathname = pathname.strip("\" \t\r\n")
		
		while True:
			if not os.path.exists(pathname):
				print u'目录或文件不存在！重新输入目录或文件名称:',
				pathname = raw_input()
				pathname = pathname.strip("\" \t\r\n")
			else:
				print u"确定要删除文件\"",pathname,"\"?  (y)es?:",
				sure = raw_input()
				sure = sure.lower()
				if sure == 'y' or sure=='yes':
					break
				else:
					return

		"""判断文件还是目录"""
		if os.path.isfile(pathname):
			try:
				os.chmod( pathname, stat.S_IWRITE ) # 去除只读属性
				os.remove(pathname)
			except Exception:
				failedfile.append(pathname)

			print '----------------------------------------------------'
			print u'目录总数:', 0, u'文件总数:', 1
			if failedfile:
				print u'删除失败文件：'
				print failedfile[0]
			return

		"""递归删除目录"""
		dircnt = 0
		filecnt = 0
		
		print '----------------------------------------------------'
		for path, subdirs, files in os.walk(pathname, topdown=False):
			dircnt = dircnt + 1
			try:
				for file in files:
					try:
						filename = os.path.join(path,file)
						filecnt = filecnt + 1
						print u'正在删除第%i个文件...%s'%(filecnt, '\r'),
						os.chmod( filename, stat.S_IWRITE ) # 去除只读属性
						os.remove(filename)
					except Exception, e:
						failedfile.append(filename)
						continue
				os.rmdir(path)
			except Exception, e:
				pass

		print u'目录总数:', dircnt, u'文件总数:', filecnt, u'删除失败总数：', len(failedfile)
		if failedfile:
			print u'删除失败文件：'
			for ret in failedfile:
				print ret
		
		print u'\n\n按回车按键退出.',
		raw_input()

	except KeyboardInterrupt:
		pass

if __name__ == '__main__':
	main()
