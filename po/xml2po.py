#!/usr/bin/python
from __future__ import print_function
import sys
import os
import string
import re
import xml.dom.minidom
from xml.dom import minidom, Node
attrlist = set()

for arg in sys.argv[1:]:
	mqbfunctions = xml.dom.minidom.parse(arg)
	for mqbfunction in mqbfunctions.getElementsByTagName("content"):
		if mqbfunction.getElementsByTagName("name"):
			name = str(mqbfunction.getElementsByTagName("name")[0].childNodes[0].data)
		if mqbfunction.getElementsByTagName("trans"):
			name = str(mqbfunction.getElementsByTagName("translation")[0].childNodes[0].data)
		attrlist.add((name, None))
	for mqbfunction in mqbfunctions.getElementsByTagName("mqbfunction"):
		if mqbfunction.getElementsByTagName("name"):
			name = str(mqbfunction.getElementsByTagName("name")[0].childNodes[0].data)
		if mqbfunction.getElementsByTagName("trans"):
			name = str(mqbfunction.getElementsByTagName("translation")[0].childNodes[0].data)
		attrlist.add((name, None))

	attrlist = list(attrlist)
	attrlist.sort(key=lambda a: a[0])

	for (k, c) in attrlist:
		print()
		print('#: ' + arg)
		string.replace(k, "\\n", "\"\n\"")
		if c:
			for l in c.split('\n'):
				print("#. ", l)
		print('msgid "' + str(k) + '"')
		print('msgstr ""')

	attrlist = set()
