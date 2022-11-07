import PyPDF2
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith('.pdf'):
        print(file)
        merger.append(file)
    merger.write('combinedPDFfiles.pdf')
