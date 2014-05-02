+ script: Use for titanium  build
+ imgMove.py: place all titanium image into corresponding directory
	* Place imgMove.py in Resource directory.
	* Place all images into "Resources\images\imgMove" with profer name.
	* Sample image folder is given at "Resources\images\imgMove\sample"
	* For naming
		- tmp10.png: normal size portrait and final name will be "tmp.png"
		- tmp15.png: 1.5X size portrait and final name will be "tmp.png"
		- tmp15L.png: 1.5X size landscape and final name will be "tmp.png"
		- tmp20.png: 2X size portrait and final name will be "tmp.png" ("tmp@2x.png" for iphone)
		- tmp20L.png: 2X size landscape and final name will be "tmp.png" ("tmp@2x.png" for iphone)
		- all image name with sample images name will be ignore
		- after coping images please delete all images from "Resources\images\imgMove" except sample folder  
	