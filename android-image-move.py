from datetime import datetime
import os, shutil

# valid file anme "icon1.0.png", "icon1.5.png", "icon2.0.png", "icon3.0.png"
VALID_FILE = ["1.0.png", "1.5.png", "2.0.png", "3.0.png"]
VALID_FILE_PATH = ["drawable-mdpi", "drawable-hdpi", "drawable-xhdpi", "drawable-xxhdpi"]
IS_DELETE_FILE_AFTER_MOVE = False


def deleteFile(name):
	try:
		os.remove(name)
		print "Deleted:", name
	except:
		pass


def copyFile(s, dest):
	print "COPY Src: ",s
	print "COPY Dst: ", dest
	deleteFile(dest)
	shutil.copyfile(s, dest)
	if IS_DELETE_FILE_AFTER_MOVE:
		deleteFile(s)	
		print "Deleted: ",s
	print "Done\n\n"

def isValidFile(name):
	i = 0
	for t in VALID_FILE:
		if name.endswith(t):
			return i
		i += 1
	return -1

def makeRealFIleName(index, name):
	return name.replace(VALID_FILE[index],".png")

def moveFile(src, dst):
	print "Mopving file "
	for n in os.listdir(src):
		index = isValidFile(n)
		if index == -1:
			continue
		realName = makeRealFIleName(index, n)
		print "[Process]",n,"[Path]",VALID_FILE_PATH[index],"[RealName]",realName
		copyFile(src+n, dst+VALID_FILE_PATH[index]+"/"+realName)



if __name__=='__main__':
	print "Start : ",datetime.now()

	ANDROID_PATH = '/Users/Jony/Developer/Android/SiSigmaAndroidAPP/res/';
	SRC_PATH = '/Users/Jony/Developer/Python/test/infile/'

	print "ANDROID",ANDROID_PATH
	print "SRC",SRC_PATH
	print 100*"*"

	moveFile(SRC_PATH, ANDROID_PATH)

	print "End : ",datetime.now()