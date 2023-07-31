from reportlab.lib.units import inch
# from reportlab.lib.colors import HexColor
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

# todo - read these values from xml file

doc = SimpleDocTemplate("Elestianul.pdf",
                            pagesize=(8.5 * inch, 11 * inch),
                            rightMargin=50,
                            leftMargin=50,
                            topMargin=50,
                            bottomMargin=50,
                            showBoundary=0,
                            allowSplitting=1,)
style = getSampleStyleSheet()
textStyle = ParagraphStyle('textStyle',
                           fontName="Times-Roman",
                           fontSize=10,
                           parent=style['Normal'],
                           alignment=0,
                           spaceAfter=0,
                           textColor='black',
                           backColor='0xFFFFFF',
                           borderColor='0x000000',
                           borderWidth=0,
                           borderPadding=0,
                           textTransform='none',
                           firstLineIndent=0,
                           )
bulletStyle = ParagraphStyle('bulletStyle',
                           fontName="Times-Roman",
                           fontSize=10,
                           parent=style['Normal'],
                           alignment=0,
                           spaceAfter=3,
                           bulletIndent=3,
                           leftIndent=12,
                           textColor='black',
                           backColor='0xFFFFFF',
                           borderColor='0x000000',
                           borderWidth=0,
                           borderPadding=0,
                           textTransform='none',
                           firstLineIndent=0,
                           )

h1Style = ParagraphStyle('h1Style',
                           fontName="Times-Bold",
                           fontSize=16,
                           parent=style['Normal'],
                           alignment=0,
                           spaceBefore=8,
                           spaceAfter=14,
                           textTransform='none',
                           textColor='black',
                           backColor='0xFFFFFF',
                           borderColor='0x000000',
                           borderWidth=0,
                           borderPadding=0,
                           )
h2Style = ParagraphStyle('h2Style',
                           fontName="Times-Roman",
                           fontSize=14,
                           parent=style['Normal'],
                           alignment=0,
                           spaceBefore=8,
                           spaceAfter=8,
                           textTransform='none',
                           textColor='black',
                           backColor='0xFFFFFF',
                           borderColor='0x000000',
                           borderWidth=0,
                           borderPadding=0,
                           )
h3Style = ParagraphStyle('h3Style',
                           fontName="Times-Roman",
                           fontSize=12,
                           parent=style['Normal'],
                           alignment=0,
                           spaceBefore=0,
                           spaceAfter=14,
                           textTransform='none',
                           textColor='black',
                           backColor='0xFFFFFF',
                           borderColor='0x000000',
                           borderWidth=0,
                           borderPadding=0,
                           )
h4Style = ParagraphStyle('h4Style',
                           fontName="Times-Roman",
                           fontSize=12,
                           parent=style['Normal'],
                           alignment=0,
                           spaceAfter=14,
                           textTransform='none',
                           textColor='black',
                           backColor='0xFFFFFF',
                           borderColor='0x000000',
                           borderWidth=0,
                           borderPadding=0,
                           )