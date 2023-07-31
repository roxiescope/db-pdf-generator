import sys
import xml.etree.ElementTree as ET
import glob

'''
1. getXML:
- pull XML values from xml file
- set in-file constants to those values
- return them based on "attribute tag"
2. setXML:
- update in-file constants with given value
- update xml file with given value
'''

# Set defaults
mConfigLoc = 'RLGconfig.xml'

def getXML(attribute, subattribute=0):
    # maybe I don't have to do this? it wasn't recognizing my variables above unless I called them here again
    # todo - font, size, color (for headings up to 4), page size, page color, page margins, bullet indent, paragraph indent
    global text
    global heading1
    global heading2
    global heading3
    global heading4
    global PageSettings
    global LayoutSettings

    file = glob.glob(mConfigLoc, recursive=False)
    if file:
        tree = ET.parse(mConfigLoc)
        root = tree.getroot()
        if attribute == 'text':
            return root[0][0].text
        # elif attribute == 'banking':
        #     return root[0][1].text
        # elif attribute == 'todo':
        #     return root[0][2].text
        # elif attribute == 'reading':
        #     return root[0][3].text
        # elif attribute == 'wardrobe':
        #     return root[0][4].text
        elif attribute == 'theme':
            return root[1].text
        # elif attribute == 'MintPass':
        #     return root[2].text
        # elif attribute == 'notifications':
        #     return root[3].text
        else:
            print("settings entry is invalid")

    else:
        print("you need to make the xml")
        # TODO: create xml with default values


def setXML(attribute, sub, value):
    print("setting XML: " + attribute)
    tree = ET.parse(mConfigLoc)
    root = tree.getroot()
    if attribute == 'text':
        match sub:
            case "font":
                root[0][1].text = str(value)
            case "size":
                root[0][2].text = str(value)
            case "color":
                root[0][3].text = str(value)
            case _:
                print("invalid attribute setXML")
#     elif attribute == 'banking':
#         banking = value
#         root[0][1].text = str(banking)
#     elif attribute == 'reading':
#         reading = value
#         root[0][3].text = str(reading)
#     elif attribute == 'wardrobe':
#         wardrobe = value
#         root[0][4].text = str(wardrobe)
    elif attribute == 'theme':
        theme = value
        root[1].text = str(theme)
#     elif attribute == 'MintPass':
#         MintPass = value
#         root[2].text = str(MintPass)
#     elif attribute == 'notifications':
#         notifications = value
#         root[3].text = str(notifications)
    else:
        print("settings entry is invalid")

    tree.write(mConfigLoc)
