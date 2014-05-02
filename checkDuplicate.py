import hashlib
import os

'''
from checkDuplicate import CheckDuplicate

d = CheckDuplicate(p)
a, redundant = d.findDuplicate()
print redundant
print a
d.deleteAllRedundantFile(redundant)
'''

class CheckDuplicate:
	def __init__(self, path):
		self.path = path

	def deleteAllRedundantFile(self, redundantFile):
		for name in redundantFile:
			os.remove(name)
			print "Deleted:", name

	def hashfile(self, path, blocksize = 65536):
	    afile = open(path, 'rb')
	    hasher = hashlib.md5()
	    buf = afile.read(blocksize)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(blocksize)
	    afile.close()
	    return hasher.hexdigest()

	def findDuplicate(self):
	    # Dups in format {hash:[names]}
	    dups = {}
	    redundantFile = []
	    for dirName, subdirs, fileList in os.walk(self.path):
	        print('Scanning %s...' % dirName)
	        for filename in fileList:
	            # Get the path to the file
	            path = os.path.join(dirName, filename)
	            # Calculate hash
	            file_hash = self.hashfile(path)
	            # Add or append the file path
	            if file_hash in dups:
	            	# this is duplicate file
	            	redundantFile.append(path)
	                dups[file_hash].append(path)
	            else:
	                dups[file_hash] = [path]
	    return dups, redundantFile