# Reading files from the network

import urllib2
import codeskulptor

FILENAME = "examples_files_dracula.txt"

url = codeskulptor.file2url(FILENAME)
netfile = urllib2.urlopen(url)

#data = netfile.read()
#print data
#print type(data)

#for line in netfile.readlines():
#    print line
    