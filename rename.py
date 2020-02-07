#!/usr/bin/python

import os,sys


path = './'+sys.argv[1]

#get all the files name in list contain by folder
files = os.listdir(path)

int_array=[]
str_array=[]

#seperate files(integer or string) with use its name 
for file in files:
	if os.path.splitext(file)[0].isdigit():
		int_array.append(os.path.splitext(file)[0])
	else :
		str_array.append(file)

#sort integer files which is already renamed
int_array.sort(key=int)

num=1

#rename all integer files first in ascending number order eg.1,2,3,4.....
for i in int_array:
	for j in files:
		if os.path.splitext(j)[0].isdigit():
			if int(i)==int(os.path.splitext(j)[0]):
				os.rename(os.path.join(path, j), os.path.join(path, str(num)+os.path.splitext(j)[1]))
				num=num+1
#now rename remaining files which is string and rename it to ascending number order
for j in str_array:
	os.rename(os.path.join(path, j), os.path.join(path, str(num)+os.path.splitext(j)[1]))
	num=num+1

###   How To Use
##    python rename.py /path/to/folder
