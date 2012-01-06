# -*- encoding: utf-8 -*-
'''
por enquanto só no para segundos e millisegundos
'''

import datetime
from sys import argv
import os

script, fileName, timeStr=argv

if not os.path.isfile(fileName):
	print 'the path isn\'t a file'
	sys.exit()

isPositive=timeStr.find('-')==-1
timeStr=timeStr.replace('-','')

timeDatetime=datetime.datetime.strptime(timeStr,'%S,%f')
time=datetime.timedelta(seconds=timeDatetime.second,microseconds=timeDatetime.microsecond)

file=open(fileName,'r')
targetFileName=os.path.join(os.path.dirname(file.name),'alter-'+os.path.basename(file.name))
targetFile=open(targetFileName,'w')

file_content=file.readlines()
file.close()

for line in file_content:
	line=line.replace('\n','') #I'm sleepy, it's the best thing what I think
	if line.find('-->') != -1:
		times=line.split(' --> ')
		start=datetime.datetime.strptime(times[0],'%H:%M:%S,%f')
		end=datetime.datetime.strptime(times[1],'%H:%M:%S,%f')
		if isPositive:
			start=start+time
			end=end+time
		else:
			start=start-time
			end=end-time
		line=start.strftime('%H:%M:%S,%f')[:12]+' --> '+end.strftime('%H:%M:%S,%f')[:12]
		
	targetFile.write(line)
	targetFile.write('\n')

targetFile.close()
	
print 'Success!!!'