from pyPdf import PdfFileReader
import slate

content = '/home/irunika/PycharmProjects/cv_classifier/packages/pdf/Lab1_E11431.pdf'

with open(content) as f:
    doc = slate.PDF(f)


