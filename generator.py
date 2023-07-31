import psycopg2
from mdutils.mdutils import MdUtils
from bs4 import BeautifulSoup
from reportlab.lib.units import inch, mm
from reportlab.lib import utils
# from reportlab.lib.colors import HexColor
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, PageBreak, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
import formats
import io
from PIL import Image as Pimage
import os


def addPageNumber(canvas, doc):
    """
    Add the page number
    """
    page_num = canvas.getPageNumber()
    text = "Page %s" % page_num
    canvas.setFont("Times-Roman",8)
    # canvas.drawInlineImage('./page outline - letter.png',0,0, width=8.5*inch,height=11*inch)
    canvas.drawRightString(200*mm, 10*mm, text)

def get_image(path, width=1*inch):
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    return Image(path, width=width, height=(width * aspect))

# Creating output .md file
mdFile = MdUtils(file_name='Example_Markdown')

flowables = []
missing_image = './imagemissing.png'


# Establishing database connection
conn = psycopg2.connect(database = "fictionalUniverse",
                        user = "postgres",
                        host= 'localhost',
                        password = "gay",
                        port = 5433)
# Establishing a database manipulator
cur = conn.cursor()

# Pulling content from database
cur.execute('SELECT render FROM pages;')
output = cur.fetchall()
cur.execute('SELECT data FROM public."assetData";')
images = cur.fetchall()
cur.execute('SELECT filename FROM public."assets";')
imageNames = cur.fetchall()
newOut = []
imagePaths = []

for row in images:
    # print(row[0])
    file_like = io.BytesIO(row[0])
    img1 = Pimage.open(file_like)
    imageString = str(images.index(row)) + '.png'
    img1.save(imageString)
    # img1.show()

for row in imageNames:
    imageString = str(imageNames.index(row)) + '.png'
    image = Pimage.open(imageString)
    image.save(str(row[0]))
    imagePaths.append(str(row[0]))
    os.remove(imageString)



# Removing the paragraph symbols and their associated links
for row in output:
    soup = BeautifulSoup(row[0], features="html5lib")
    for a in soup.findAll('a'):
        a.replaceWith("")
    fixed = str(soup).replace("¶","")
    mdFile.write(fixed)
    newOut.append(fixed)

# Writing updated text to .md file
mdFile.create_md_file()

# Translating PDF
for row in newOut:
    soup = BeautifulSoup(row, features="html5lib")
    for a in soup.findAll(True):
        if a.name == 'h1':
            para = Paragraph(str(a), style=formats.h1Style)
            flowables.append(para)
        if a.name == 'li':
            item = '<bullet>&bull</bullet>' + str(a)
            para = Paragraph(item, style=formats.bulletStyle)
            flowables.append(para)
        if a.name == 'h2':
            item = '<u>' + str(a)+ '</u>'
            para = Paragraph(item, style=formats.h2Style)
            flowables.append(para)
        if a.name == 'p':
            for child in a.findChildren('img', recursive=False):
                source = child.get('alt')
                for row in imagePaths:
                    if str(source) == str(row):
                        flowables.append(get_image(source, width=6*inch))
                child.replaceWith('')
            para = Paragraph(str(a), style=formats.textStyle)
            flowables.append(para)
        if a.name == 'h3':
            para = Paragraph(str(a), style=formats.h3Style)
            flowables.append(para)
        if a.name == 'h4':
            para = Paragraph(str(a), style=formats.h4Style)
            flowables.append(para)


formats.doc.build(flowables, onFirstPage=addPageNumber, onLaterPages=addPageNumber)

