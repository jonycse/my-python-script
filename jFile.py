import os, shutil

# path = os.getcwd()

def deleteFileSafe(name):
	"""Delete a file from path, with no exception"""
	try:
		deleteFile(name)
	except:
		pass

def deleteFile(name):
	"""Delete a file from path, with exception"""
	os.remove(name)
	print "Deleted:", name

def deleteFolder(name):
	"""Delete a entire folder, with exception"""
	shutil.rmtree(name)
	print "Deleted Folder:", name

def deleteFolderSafe(name):
	"""Delete a entire folder, with no exception"""
	try:
		shutil.rmtree(name)
		print "Deleted Folder:", name
	except:
		pass

def copyFile(src, dest):
	"""Copy file from source to destination. Use raw string for path"""
	print "Src: ",src
	print "Dst: ", dest
	deleteFileSafe(dest)
	shutil.copyfile(src, dest)
	
def moveFile(src, dest):
	"""Move file from source to destination. Use raw string for path"""
	print "Src: ",src
	print "Dst: ", dest
	shutil.move(src, dest)

def readFile(name):
	"""Read a file"""
	f = open(name, 'r')
	data = f.read()
	f.close()
	return data


def readFileByLine(name):
	"""Read a file by line"""
	rt = []
	f = open(name, 'r')
	for line in f.readlines():
		rt.append( line.strip() )
	f.close()
	return rt

def writeFile(name, data):
	"""Write content to a file"""
	f=open(name,'w')
	f.write(data)
	f.close()

def allFileType(directory, fileType):
	"""Gel all specefic file type from a directory"""
	rt = []
	for name in os.listdir(directory):
		if name.endswith(fileType):
			rt.append(name)
	return rt