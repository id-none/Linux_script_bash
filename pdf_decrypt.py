#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a module to decrypt pdf file '

from PyPDF2 import PdfFileReader, PdfFileWriter


path = input('Please input the path of the pdf file(eg: /home/xxx/xxx.pdf):')
passwd = input('Please input the password of the pdf file:')

pdf_reader = PdfFileReader(path)
pdf_reader.decrypt(passwd)
pdf_writer = PdfFileWriter()
for page in range(pdf_reader.getNumPages()):
    pdf_writer.addPage(pdf_reader.getPage(page))

with open(path[:-4] + '_decrypted.pdf', 'wb') as out: 
    pdf_writer.write(out)
    print('Decrypted successfully!')
