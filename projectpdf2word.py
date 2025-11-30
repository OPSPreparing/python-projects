import pdf2docx as pdf
from pdf2docx import Converter
old_pdf = "MedicalClaim.pdf"
new_doc = "medicalclaim.docx"

obj = Converter(old_pdf)
obj.convert(new_doc, start=0, end=None)
obj.close()