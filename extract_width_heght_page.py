from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen.canvas import Canvas

myCanvas = Canvas('myfile.pdf', pagesize=letter)
width, height = letter
