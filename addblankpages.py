#!/usr/bin/env python3

"""This program will take an input pdf file and search for a string that signifies the end of a letter.
After the end of the letter is found based on a string, a blank page is added. The output file is then
created in the directory with blank pages added """

import PyPDF2, re
import glob 
import os 
import re
import sys
import uuid

arg1=sys.argv[1]
arg1=arg1[2:]


print(sys.argv[1])

pdfIn = open(arg1, 'rb')
pdfFile = PyPDF2.PdfFileReader(pdfIn)
NumPages = pdfFile.getNumPages()
output = PyPDF2.PdfFileWriter()
outputStream = open(arg1[:-4]+'_write_on.pdf', 'wb')


def end_of_letter():
	pages = []
	for page in range(NumPages):
		pgObj = pdfFile.getPage(page)
		output.addPage(pgObj)
		pages.append(page + 1)
		output.addBlankPage()
	output.write(outputStream)
	print(pages)
	
	
end_of_letter()