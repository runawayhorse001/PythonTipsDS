from __future__ import print_function
import sys
import os
import shutil
import inspect
import getopt
import glob
from collections import defaultdict

if __name__ == '__main__':

	if (len(sys.argv)>1):
		print('Hello, this is a test for %s.'%str(sys.argv[1]))
	else:
		print('Hello, you do not have input argument') 



	#throot = os.path.abspath(os.path.join(sys.path[0], os.pardir, os.pardir))
	throot = os.path.abspath(os.path.join(sys.path[0]))
	#print(throot)

	build_path = throot + '/build'
	if not os.path.exists(build_path):
		os.mkdir(build_path)

	files = glob.iglob(os.path.join(throot, "*.py"))
	
	for file in files:
		print(file)
		if os.path.isfile(file):
			shutil.copy2(file, build_path)

	# try:
	# 	src_files = os.listdir(src)
	# 	for file_name in src_files:
	# 		full_file_name = os.path.join(src, file_name)
	# 		if (os.path.isfile(full_file_name)):
	# 			shutil.copy(full_file_name, dest)
	# except OSError as e:
	# 	print('OSError:', e)
	# except IOError as e:
	# 	print('IOError:', e)      

