import os, shutil, time, sys

FILE_EXTENSION = ".png"
IMAGE_LOCATION = os.getcwd()+"/test"

def getDir(n):
    return IMAGE_LOCATION+"/"+n

def deleteFile(name):
    try:
        os.remove(getDir(name))
    except:
        pass

def verbose(n):
    if n<=1:
        return str(n)+" File"
    return str(n)+" Files"

def countOptimizeFile():
    c = 0
    files = os.listdir(IMAGE_LOCATION)
    for n in files:
        if n.endswith("-fs8"+FILE_EXTENSION):
            c +=1
    return c

def deleteOldFiles():
    c = 0
    files = os.listdir(IMAGE_LOCATION)
    for n in files:
        if not n.endswith("-fs8"+FILE_EXTENSION) and n.endswith(FILE_EXTENSION):
            c +=1
            deleteFile(n)
    print "Total "+verbose(c)+" deleted"
    return c
            

def renameNewFile():
    files = os.listdir(IMAGE_LOCATION)
    print files
    c = 0
    for n in files:
        if n.endswith("-fs8"+FILE_EXTENSION):
            tn = n.replace("-fs8","")
            try:
                print "Rename["+n+"] to ["+tn+"]"
                os.rename(os.path.join(IMAGE_LOCATION,n), os.path.join(IMAGE_LOCATION,tn) )
                c += 1
            except :
                print "Err ",str(sys.exc_info())
                print "Error", tn
                deleteFile(n)
                pass
    print "Total "+verbose(c)+" renamed"
  
    

y = countOptimizeFile()
print "Optimize file count ",y
if y>0:
    deleteOldFiles()
    time.sleep(1)
    renameNewFile()
time.sleep(2)
