import os, shutil

p = os.getcwd()

# input images
inpFolder = '/images/imgMove/'

#ios image dir
iosDir = '/images/'

delete_after_move = False

def isIgnore(name):
	iList = ['tmp10.png', 'tmp15.png', 'tmp20.png', 'tmp25.png', 'tmp10L.png', 'tmp15L.png', 'tmp20L.png', 'tmp25L.png', '.DS_Store', 'sample']
	return name in iList
	

def isEndsWith(name, s):
	try:
		w = name.split(".")
		if w[len(w)-2].endswith(s):
			return True
	except:
		pass
	return False

def deleteFile(name):
	try:
		os.remove(name)
		print "Deleted:", name
	except:
		pass


def copyFile(fname, k, dest):
	s = p+inpFolder+fname
	print "Src: ",s
	print "Dst: ", dest
	deleteFile(dest)
	shutil.copyfile(s, dest)
	if delete_after_move:
		deleteFile(s)	
		print "Deleted: ",s


		
def readInputFile():
	sn = 1
	for n in os.listdir(p+inpFolder):
		print sn,"Moving:",n
		
		# if True:
		#	continue
		sn += 1
		if isIgnore(n):
			print "Ignored: ",n,"\n"
			continue
		
		# for mdpi
		k = "10"
		if (isEndsWith(n, k) ): 
			d = p + "/android/images/res-port-mdpi/"+n.replace(k+".", ".")
			copyFile(n, k, d)
			# iphone
			d = p + iosDir+n.replace(k+".", ".")
			copyFile(n, k, d)
			
		# for hdpi
		k = "15"
		if (isEndsWith(n, k) ): 
			d = p + "/android/images/res-port-hdpi/"+n.replace(k+".", ".")
			copyFile(n, k, d)
			
		# for xhdpi
		k = "20"
		if (isEndsWith(n, k) ): 
			d = p + "/android/images/res-port-xhdpi/"+n.replace(k+".", ".")
			copyFile(n, k, d)
			
			# iphone retina
			d = p + iosDir+n.replace(k+".", "@2x.")
			copyFile(n, k, d)
			
		# for xxhdpi
		k = "25"
		if (isEndsWith(n, k) ): 
			d = p + "/android/images/res-port-xxhdpi/"+n.replace(k+".", ".")
			copyFile(n, k, d)
			
		# for landscape
		# for mdpi
		k = "10L"
		if (isEndsWith(n, k) ): 
			d = p + "/android/images/res-land-mdpi/"+n.replace(k+".", ".")
			copyFile(n, k, d)
			
		# for hdpi
		k = "15L"
		if (isEndsWith(n, k) ): 
			d = p + "/android/images/res-land-hdpi/"+n.replace(k+".", ".")
			copyFile(n, k, d)
			
		# for xhdpi
		k = "20L"
		if (isEndsWith(n, k) ): 
			d = p + "/android/images/res-land-xhdpi/"+n.replace(k+".", ".")
			copyFile(n, k, d)
			
		# for xxhdpi
		k = "25L"
		if (isEndsWith(n, k) ): 
			d = p + "/android/images/res-land-xxhdpi/"+n.replace(k+".", ".")
			copyFile(n, k, d)

		print "Completed: ",n,"\n"
		
			
		
			
		

print "Resource parh: ",p;	
readInputFile()

# m = 10
# h = 15
# xh = 20
# xxh = 25
	
print "OK"