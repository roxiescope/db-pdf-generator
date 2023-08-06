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


def countXML():
    file = glob.glob(mConfigLoc, recursive=False)
    if file:
        tree = ET.parse(mConfigLoc)
        root = tree.getroot()
        a = 0
        b = 0
        f = 0
        for x in root:
            print("[" + str(a) + "]" + " " + x.tag)
            for y in x:
                print("[" + str(a) + "][" + str(b) + "]" + " " + y.tag)
                for z in y:
                    print("[" + str(a) + "][" + str(b) + "][" + str(f) + "]" + " " + z.tag)
                    f += 1
                b += 1
            a += 1


def getXML(attribute, subattribute=''):
    file = glob.glob(mConfigLoc, recursive=False)
    if file:
        tree = ET.parse(mConfigLoc)
        root = tree.getroot()
        for x in root.iter(attribute):
            if subattribute == '':
                return x.text
            else:
                for y in x.iter(subattribute):
                    return y.text
    else:
        print("you need to make the xml")
        # TODO: create xml with default values


def setXML(attribute, value, subattribute=''):
    file = glob.glob(mConfigLoc, recursive=False)
    tree = ET.parse(mConfigLoc)
    if file:
        root = tree.getroot()
        for x in root.iter(attribute):
            if subattribute == '':
                x.text = value
            else:
                for y in x.iter(subattribute):
                    y.text = value
    else:
        print("you need to make the xml")
        # TODO: create xml with default values
    tree.write(mConfigLoc)
