import re
import psycopg2
from mdutils.mdutils import MdUtils
from bs4 import BeautifulSoup
from reportlab.lib.units import inch, mm
from reportlab.lib import utils
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, PageBreak, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
import formats
import io
from PIL import Image as Pimage
import os
import config_reader
import sys

missing_image = './imagemissing.png'
newOut = []


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

def orderPages(input):
    print("ordering pages in db")
    order = fetchData('order')
    ids = fetchData('id')
    search_string = 'Order:'
    first_string = 'Z.O'
    linesplit = []
    newOrder = []
    next_ord = "0"

    # search for first page
    for row in order:
        temp_row = str(row[0])
        if re.search(first_string, temp_row):
            x = order.index(row)
            newOrder.append(input[x])
            next_ord = re.search(r'\d+', temp_row).group()
    # order everything else
    for row in ids:
        temp_row = str(row[0])
        print("id " + temp_row)
        if next_ord == temp_row:
            x = ids.index(row)
            newOrder.append(input[x])
            next_ord = re.search(r'\d+', order[x][0]).group()
            print("points to " + next_ord)
            # todo - how do I repeat this until I've gotten everything in the original list?

def removeTags(tags):
    print("removing unwanted tags")
    # todo remove all tags specified in the config file as not wanted
def fetchData(type):
    # Establishing database connection
    try:
        conn = psycopg2.connect(database = config_reader.getXML('database'),
                                user = config_reader.getXML('user'),
                                host= config_reader.getXML('host'),
                                password = config_reader.getXML('password'),
                                port = config_reader.getXML('port'))
    except:
        print("database credentials are incorrect")
        exit()
    # Establishing a database manipulator
    cur = conn.cursor()
    if type == 'content':
        # Pulling content from database
        cur.execute("SELECT render FROM pages WHERE content LIKE '%[//%';")
        return cur.fetchall()
    elif type == 'imageData':
        images = []
        cur.execute('SELECT data FROM public."assetData";')
        imageC = cur.fetchall()
        for row in imageC:
            file_like = io.BytesIO(row[0])
            img1 = Pimage.open(file_like)
            imageString = str(imageC.index(row)) + '.png'
            img1.save(imageString)
            images.append(imageString)
        return images
    elif type == 'imageNames':
        imageNames = []
        cur.execute('SELECT filename FROM public."assets";')
        imageN = cur.fetchall()
        for row in imageN:
            imageString = str(imageN.index(row)) + '.png'
            image = Pimage.open(imageString)
            image.save(str(row[0]))
            imageNames.append(str(row[0]))
            os.remove(imageString)
        return imageNames
    elif type == 'order':
        cur.execute("SELECT content FROM pages WHERE content LIKE '%[//%';")
        return cur.fetchall()
    elif type == 'id':
        cur.execute("SELECT id FROM pages WHERE content LIKE '%[//%';")
        return cur.fetchall()
    else:
        print("database fetch unsuccessful")


def generateMarkdown(name, path, export):
    mdFile = MdUtils(file_name=str(name))
    output = fetchData('content')
    # Removing the paragraph symbols and their associated links
    for row in output:
        soup = BeautifulSoup(row[0], features="html5lib")
        for a in soup.findAll('a'):
            a.replaceWith("")
        fixed = str(soup).replace("¶", "")
        mdFile.write(fixed)
        newOut.append(fixed)
    orderPages(newOut)
    # Writing updated text to .md file, if user requests it
    if export:
        mdFile.create_md_file()


def generatePdf(name, path):
    flowables = []
    generateMarkdown(name, path, False)
    images = fetchData('imageData')
    imagePaths = fetchData('imageNames')
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
                item = '<u>' + str(a) + '</u>'
                para = Paragraph(item, style=formats.h2Style)
                flowables.append(para)
            if a.name == 'p':
                for child in a.findChildren('img', recursive=False):
                    source = child.get('alt')
                    for row in imagePaths:
                        if str(source) == str(row):
                            flowables.append(get_image(source, width=6 * inch))
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
