from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("Enter the number of pdf to merge: "))
for i in range(0,n):
    peru = input(f"Enter the name of pdf{i+1}: ")
    pdfs.append(peru)

for pdf in pdfs:
    merger.append(pdf)

merger.write("PDF/merged-pdf.pdf")
merger.close()