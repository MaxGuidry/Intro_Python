import fileinput

def FindAndReplace(filename,old ,new):

	with open(filename,'r')as file:
		filedata = file.read()
	
	filedata=filedata.replace(old,new)

	with open(filename,'w') as file:
		file.write(filedata)