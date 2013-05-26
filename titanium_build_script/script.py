import os, shutil

def deleteFile(name):
	try:
		os.remove(name)
	except:
		pass
		
def makeFile(source, target):
	# read file from source
	f = open(source, 'r')
	data = f.read()
	f.close()

	# write to target
	d  =  os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/" + target
	deleteFile(d)
	f = open(d, 'w')
	f.write(data)
	f.close()


def changeImage(isFree):
	b  =  os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/Resources/"
	d1  =  b + "iphone/Default.png"
	d2  =  b + "iphone/Default@2x.png"
	d3  =  b + "iphone/Default-568h@2x.png"
	
	deleteFile(d1)
	deleteFile(d2)	
	deleteFile(d3)
	# For android
	ad1  =  b + "android/Default.png"
	ad2  =  b + "android/Default@2x.png"
	deleteFile(ad1)
	deleteFile(ad2)
	
	if isFree:
		s1  =  b + "iphone/Default_free.png"
		s2  =  b + "iphone/Defaultl@2x_free.png"
		s3  =  b + "iphone/Default-568h@2x_free.png"
		
		shutil.copyfile(s1, d1)
		shutil.copyfile(s2, d2)
		shutil.copyfile(s3, d3)
		#android
		shutil.copyfile(s1, ad1)
		shutil.copyfile(s2, ad2)
	else:
		s1  =  b + "iphone/Default_paid.png"
		s2  =  b + "iphone/Default@2x_paid.png"
		s3  =  b + "iphone/Default-568h@2x_paid.png"
		shutil.copyfile(s1, d1)
		shutil.copyfile(s2, d2)
		shutil.copyfile(s3, d3)
		#android
		shutil.copyfile(s1, ad1)
		shutil.copyfile(s2, ad2)
		
	# android other
	if isFree:
		#res-notlong-port-mdpi
		ad  =  b + "android/images/res-notlong-port-mdpi/Default.png"
		deleteFile(ad)
		sa =  b + "iphone/Default_free.png"
		shutil.copyfile(sa, ad)
		#res-notlong-port-ldpi
		ad  =  b + "android/images/res-notlong-port-ldpi/Default.png"
		deleteFile(ad)
		sa =  b + "android/Default_trial_240x320.png"
		shutil.copyfile(sa, ad)
		# res-notlong-port-hdpi
		ad  =  b + "android/images/res-notlong-port-hdpi/Default.png"
		deleteFile(ad)
		sa =  b + "android/Default_trial_480x800.png"
		shutil.copyfile(sa, ad)
		# res-long-port-hdpi
		ad  =  b + "android/images/res-long-port-hdpi/Default.png"
		deleteFile(ad)
		sa =  b + "android/Default_trial_480x800.png"
		shutil.copyfile(sa, ad)
		
	else:
		#res-notlong-port-mdpi
		ad  =  b + "android/images/res-notlong-port-mdpi/Default.png"
		deleteFile(ad)
		sa =  b + "iphone/Default_paid.png"
		shutil.copyfile(sa, ad)
		#res-notlong-port-ldpi
		ad  =  b + "android/images/res-notlong-port-ldpi/Default.png"
		deleteFile(ad)
		sa =  b + "android/Default_paid_240x320.png"
		shutil.copyfile(sa, ad)
		# res-notlong-port-hdpi
		ad  =  b + "android/images/res-notlong-port-hdpi/Default.png"
		deleteFile(ad)
		sa =  b + "android/Default_paid_480x800.png"
		shutil.copyfile(sa, ad)
		# res-long-port-hdpi
		ad  =  b + "android/images/res-long-port-hdpi/Default.png"
		deleteFile(ad)
		sa =  b + "android/Default_paid_480x800.png"
		shutil.copyfile(sa, ad)
	
	
def moveAppIconToResourceImage(isFree):
	b  =  os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/Resources/"
	d1  =  b + "images/appicon.png"
	d2  =  b + "images/appicon@2x.png"
	if isFree:
		s1  =  b + "iphone/appicon_trial.png"
		s2  =  b + "iphone/appicon@2x_trial.png"
	else:
		s1  =  b + "iphone/appicon_paid.png"
		s2  =  b + "iphone/appicon@2x_paid.png"
	shutil.copyfile(s1, d1)
	shutil.copyfile(s2, d2)
	
		

def changeAppIcon(isFree):
	# For iphone
	if isFree:
		b  =  os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/Resources/"
		d1  =  b + "iphone/appicon.png"
		d2  =  b + "iphone/appicon@2x.png"
		deleteFile(d1)
		deleteFile(d2)
		
		s1  =  b + "iphone/appicon_trial.png"
		s2  =  b + "iphone/appicon@2x_trial.png"
		
		shutil.copyfile(s1, d1)
		shutil.copyfile(s2, d2)
		
		#android
		d1  =  b + "android/appicon.png"
		d2  =  b + "android/appicon@2x.png"
		shutil.copyfile(s1, d1)
		shutil.copyfile(s2, d2)
	else:
		b  =  os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/Resources/"
		d1  =  b + "iphone/appicon.png"
		d2  =  b + "iphone/appicon@2x.png"
		deleteFile(d1)
		deleteFile(d2)
		
		s1  =  b + "iphone/appicon_paid.png"
		s2  =  b + "iphone/appicon@2x_paid.png"
		shutil.copyfile(s1, d1)
		shutil.copyfile(s2, d2)
		
		#android
		d1  =  b + "android/appicon.png"
		d2  =  b + "android/appicon@2x.png"
		shutil.copyfile(s1, d1)
		shutil.copyfile(s2, d2)

# Free version
makeFile("freetiapp.xml", "tiapp.xml")
makeFile("freeinfo.plist", "info.plist")
changeImage(True)
changeAppIcon(True)
moveAppIconToResourceImage(True)

# Paid version
#makeFile("paidtiapp.xml", "tiapp.xml")
#makeFile("paidinfo.plist", "info.plist")
#changeImage(False)
#changeAppIcon(False)
#moveAppIconToResourceImage(False)

print "Success !!!"
