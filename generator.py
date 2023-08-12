import re
import psycopg2
from mdutils.mdutils import MdUtils
from bs4 import BeautifulSoup
from reportlab.lib.units import inch, mm
from reportlab.lib import utils
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
import io
from PIL import Image as Pimage
import config_reader
import rlog

missing_image = 'Utilities/imagemissing.png'


def setDocFormat(t, file='', path=''):
    style = getSampleStyleSheet()
    if t == "page":
        PAGESIZE = (float(config_reader.getXML('PageSettings', 'width')) * inch,
                    float(config_reader.getXML('PageSettings', 'height')) * inch)
        FILENAME = path + "/" + file + ".pdf"
        doc = SimpleDocTemplate(FILENAME,
                                pagesize=PAGESIZE,
                                rightMargin=float(config_reader.getXML('PageSettings', 'rightMargin')),
                                leftMargin=float(config_reader.getXML('PageSettings', 'leftMargin')),
                                topMargin=float(config_reader.getXML('PageSettings', 'topMargin')),
                                bottomMargin=float(config_reader.getXML('PageSettings', 'bottomMargin')),
                                showBoundary=float(config_reader.getXML('PageSettings', 'showBoundary')),
                                allowSplitting=float(config_reader.getXML('PageSettings', 'allowSplitting')),
                                )
        return doc
    elif t == "text":
        textStyle = ParagraphStyle('textStyle',
                                   fontName=config_reader.getXML('text', 'font'),
                                   fontSize=float(config_reader.getXML('text', 'fontSize')),
                                   parent=style['Normal'],
                                   alignment=float(config_reader.getXML('text', 'alignment')),
                                   spaceAfter=float(config_reader.getXML('text', 'spaceAfter')),
                                   textColor=config_reader.getXML('text', 'textColor'),
                                   backColor=config_reader.getXML('text', 'backColor'),
                                   borderColor=config_reader.getXML('text', 'borderColor'),
                                   borderWidth=float(config_reader.getXML('text', 'borderWidth')),
                                   borderPadding=float(config_reader.getXML('text', 'borderPadding')),
                                   textTransform=config_reader.getXML('text', 'textTransform'),
                                   firstLineIndent=float(config_reader.getXML('text', 'firstLineIndent')),
                                   )
        return textStyle
    elif t == "bullet":
        bulletStyle = ParagraphStyle('bulletStyle',
                                     fontName=config_reader.getXML('bullet', 'font'),
                                     fontSize=float(config_reader.getXML('bullet', 'fontSize')),
                                     parent=style['Normal'],
                                     alignment=float(config_reader.getXML('bullet', 'alignment')),
                                     spaceAfter=float(config_reader.getXML('bullet', 'spaceAfter')),
                                     bulletIndent=float(config_reader.getXML('bullet', 'bulletIndent')),
                                     leftIndent=float(config_reader.getXML('bullet', 'leftIndent')),
                                     textColor=config_reader.getXML('bullet', 'textColor'),
                                     backColor=config_reader.getXML('bullet', 'backColor'),
                                     borderColor=config_reader.getXML('bullet', 'borderColor'),
                                     borderWidth=float(config_reader.getXML('bullet', 'borderWidth')),
                                     borderPadding=float(config_reader.getXML('bullet', 'borderPadding')),
                                     textTransform=config_reader.getXML('bullet', 'textTransform'),
                                     firstLineIndent=float(config_reader.getXML('bullet', 'firstLineIndent')),
                                     )
        return bulletStyle
    elif t == "h1":
        h1Style = ParagraphStyle('h1Style',
                                 fontName=config_reader.getXML('heading1', 'font'),
                                 fontSize=float(config_reader.getXML('heading1', 'fontSize')),
                                 parent=style['Normal'],
                                 alignment=float(config_reader.getXML('heading1', 'alignment')),
                                 spaceBefore=float(config_reader.getXML('heading1', 'spaceBefore')),
                                 spaceAfter=float(config_reader.getXML('heading1', 'spaceAfter')),
                                 textTransform=config_reader.getXML('heading1', 'textTransform'),
                                 textColor=config_reader.getXML('heading1', 'textColor'),
                                 backColor=config_reader.getXML('heading1', 'backColor'),
                                 borderColor=config_reader.getXML('heading1', 'borderColor'),
                                 borderWidth=float(config_reader.getXML('heading1', 'borderWidth')),
                                 borderPadding=float(config_reader.getXML('heading1', 'borderPadding')),
                                 )
        return h1Style
    elif t == "h2":
        h2Style = ParagraphStyle('h2Style',
                                 fontName=config_reader.getXML('heading2', 'font'),
                                 fontSize=float(config_reader.getXML('heading2', 'fontSize')),
                                 parent=style['Normal'],
                                 alignment=float(config_reader.getXML('heading2', 'alignment')),
                                 spaceBefore=float(config_reader.getXML('heading2', 'spaceBefore')),
                                 spaceAfter=float(config_reader.getXML('heading2', 'spaceAfter')),
                                 textTransform=config_reader.getXML('heading2', 'textTransform'),
                                 textColor=config_reader.getXML('heading2', 'textColor'),
                                 backColor=config_reader.getXML('heading2', 'backColor'),
                                 borderColor=config_reader.getXML('heading2', 'borderColor'),
                                 borderWidth=float(config_reader.getXML('heading2', 'borderWidth')),
                                 borderPadding=float(config_reader.getXML('heading2', 'borderPadding')),
                                 )
        return h2Style
    elif t == "h3":
        h3Style = ParagraphStyle('h3Style',
                                 fontName=config_reader.getXML('heading3', 'font'),
                                 fontSize=float(config_reader.getXML('heading3', 'fontSize')),
                                 parent=style['Normal'],
                                 alignment=float(config_reader.getXML('heading3', 'alignment')),
                                 spaceBefore=float(config_reader.getXML('heading3', 'spaceBefore')),
                                 spaceAfter=float(config_reader.getXML('heading3', 'spaceAfter')),
                                 textTransform=config_reader.getXML('heading3', 'textTransform'),
                                 textColor=config_reader.getXML('heading3', 'textColor'),
                                 backColor=config_reader.getXML('heading3', 'backColor'),
                                 borderColor=config_reader.getXML('heading3', 'borderColor'),
                                 borderWidth=float(config_reader.getXML('heading3', 'borderWidth')),
                                 borderPadding=float(config_reader.getXML('heading3', 'borderPadding')),
                                 )
        return h3Style
    elif t == "h4":
        h4Style = ParagraphStyle('h4Style',
                                 fontName=config_reader.getXML('heading4', 'font'),
                                 fontSize=float(config_reader.getXML('heading4', 'fontSize')),
                                 parent=style['Normal'],
                                 alignment=float(config_reader.getXML('heading4', 'alignment')),
                                 spaceBefore=float(config_reader.getXML('heading4', 'spaceBefore')),
                                 spaceAfter=float(config_reader.getXML('heading4', 'spaceAfter')),
                                 textTransform=config_reader.getXML('heading4', 'textTransform'),
                                 textColor=config_reader.getXML('heading4', 'textColor'),
                                 backColor=config_reader.getXML('heading4', 'backColor'),
                                 borderColor=config_reader.getXML('heading4', 'borderColor'),
                                 borderWidth=float(config_reader.getXML('heading4', 'borderWidth')),
                                 borderPadding=float(config_reader.getXML('heading4', 'borderPadding')),
                                 )
        return h4Style

def addPageNumber(canvas, doc):
    """
    Add the page number and the background image
    """
    page_num = canvas.getPageNumber()
    text = "Page %s" % page_num
    canvas.setFont("Times-Roman", 8)
    try:
        canvas.drawInlineImage(config_reader.getXML('backImg'),0,0, width=8.5*inch,height=11*inch)
    except:
        if re.search("background image path is invalid", rlog.readlog()):
            pass
        else:
            rlog.writelog("background image path is invalid")
    canvas.drawRightString(200*mm, 10*mm, text)

def get_image(path, width=1*inch):
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    return Image(path, width=width, height=(width * aspect))


def orderPages(input):
    search_string = 'Order:'
    first_string = 'Z.O'
    newOrder = []
    next_ord = "0"
    new_input = []
    unordered = []

    '''
    1. pull order from content and make that the content column [1]
    2. find first id, append that and next_ord pointer to newOrder (columns 0 and 1)
    3. iterate through length of input minus 1
        a. iterate through input itself - for each row, if id (aka [0]) is next_ord, append [0] and [1] to newOrder
        b. set next_ord to [1]
    '''
    for x in input:
        # print(x[0])
        temp_row = str(x[2])
        if re.search(search_string, temp_row):
            x[2] = re.search(r'\d+', temp_row).group()
            # if item has an order specified, add it to new_input
            new_input.append(x)
            if re.search(first_string, temp_row):
                temp_array = (x[0], x[2])
                next_ord = x[2]
                # newOrder will be the final list
                newOrder.append(x)
        # unordered will store all the pages without an order specified
        unordered.append(x)
    for y in range(len(new_input)):
        for z in new_input:
            if z[0] == int(next_ord):
                newOrder.append(z)
                next_ord = z[2]
                break
    # add the unordered pages back in
    for h in unordered:
        newOrder.append(h)
    return newOrder


def getTags():
    tags = fetchData("tags")
    return tags


def removeTags(input):
    tagSettings = str(config_reader.getXML("tagsToInclude"))
    newIdList = []
    newData = []
    for x in input:
        if re.search(x[1], tagSettings):
            if x[0] not in newIdList:
                newIdList.append(x[0])
                newData.append(x)

    return newData


def fetchData(type, path=''):
    # Establishing database connection
    try:
        conn = psycopg2.connect(database = config_reader.getXML('database'),
                                user = config_reader.getXML('user'),
                                host= config_reader.getXML('host'),
                                password = config_reader.getXML('password'),
                                port = config_reader.getXML('port'))
    except:
        rlog.writelog("Database credentials are incorrect")
        exit()
    # Establishing a database manipulator
    cur = conn.cursor()
    if type == 'content':
        # Pulling content from database
        # cur.execute('SELECT "id","content","render" FROM pages;')
        cur.execute('SELECT pt."pageId", tags."title", pages."content", pages."render" '
                    'FROM "pageTags" pt '
                    'INNER JOIN "tags" ON pt."tagId" = tags."id" '
                    'INNER JOIN pages ON pages."id" = pt."pageId";')
        return cur.fetchall()
    elif type == 'imageData':
        images = []
        cur.execute('SELECT "data","filename" FROM public."assetData" INNER JOIN public."assets" '
                    'ON public."assetData".id = public."assets".id;')
        imageC = cur.fetchall()
        for row in imageC:
            file_like = io.BytesIO(row[0])
            img1 = Pimage.open(file_like)
            imageString = str(row[1])
            imgPath = imageString
            if path != '':
                imgPath = path + '/' + imageString
            img1.save(imgPath)
            images.append(imgPath)
        return images
    elif type == 'tags':
        cur.execute('SELECT "pageId","title" FROM public."pageTags" INNER JOIN tags ON "tagId" = tags."id";')
        return cur.fetchall()
    else:
        rlog.writelog("Database fetch unsuccessful")


def generateMarkdown(name, path, export):
    mdFile = MdUtils(file_name=str(path + "/" + name))
    output = fetchData('content')
    taggedData = []
    # output is a 3-d array - 1st column is page id, 2nd is tags associated, 3rd is the markdown, 4th is the html
    # Removing the paragraph symbols and their associated links
    taggedData = removeTags(output)
    newData = []
    # Remove linked paragraph signs
    for row in taggedData:
        soup = BeautifulSoup(row[3], features="html5lib")
        for a in soup.findAll('a'):
            a.replaceWith("")
        row = list(row)
        row[3] = str(soup).replace("¶", "")
        newData.append(row)

    newData = orderPages(newData)
    for x in newData:
        mdFile.write(x[3])
    # Writing updated text to .md file, if user requests it
    if export:
        try:
            mdFile.create_md_file()
        except:
            rlog.writelog("Your markdown path probably doesn't exist")
    else:
        return newData


def generatePdf(name, path):
    flowables = []
    finalData = generateMarkdown(name, path, False)
    images = fetchData('imageData', path)
    doc = setDocFormat("page", name, path)
    for row in finalData:
        soup = BeautifulSoup(row[3], features="html5lib")
        for a in soup.findAll(True):
            if a.name == 'h1':
                para = Paragraph(str(a), style=setDocFormat('h1'))
                flowables.append(para)
            if a.name == 'li':
                item = '<bullet>&bull</bullet>' + str(a)
                para = Paragraph(item, style=setDocFormat('bullet'))
                flowables.append(para)
            if a.name == 'h2':
                item = '<u>' + str(a) + '</u>'
                para = Paragraph(item, style=setDocFormat('h2'))
                flowables.append(para)
            if a.name == 'p':
                for child in a.findChildren('img', recursive=False):
                    source = child.get('alt')
                    for x in images:
                        if str(source) == str(x):
                            flowables.append(get_image(source, width=6 * inch))
                    child.replaceWith('')
                para = Paragraph(str(a), style=setDocFormat('text'))
                flowables.append(para)
            if a.name == 'h3':
                para = Paragraph(str(a), style=setDocFormat('h3'))
                flowables.append(para)
            if a.name == 'h4':
                para = Paragraph(str(a), style=setDocFormat('h4'))
                flowables.append(para)
    try:
        doc.build(flowables, onFirstPage=addPageNumber, onLaterPages=addPageNumber)
    except:
        rlog.writelog("your pdf path probably doesn't exist")
