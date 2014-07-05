# -*- coding: utf-8 -*-
import re

UTF8_BOM = bytearray([0xEF, 0XBB, 0XBF])
def strip_bom(s):
    if s.startswith(UTF8_BOM):
        return s[len(UTF8_BOM):]
    return s

fr = open("list.txt","r")
with open("all.md",'w') as fw:
   fw.write("https://gitprint.com/Arctictern265/QGIS_book/blob/master/all.md\n")
   fw.write("<div style='page-break-after: always;'></div>\n\n")
with open("alltext.md",'w') as fwt:
   fwt.write("https://gitprint.com/Arctictern265/QGIS_book/blob/master/alltext.md\n")
   fwt.write("<div style='page-break-after: always;'></div>\n\n")
fw = open("all.md",'a')
fwt = open("alltext.md",'a')

for line in fr:
   path = line.rstrip("\n")
   dir = path.split("/")[0]
   if(path == "--"):
      fw.write("<div style='page-break-after: always;'></div>\n\n")
      fwt.write("<div style='page-break-after: always;'></div>\n\n")
   try:
      f = open(path,"r")
      data = strip_bom(f.read()).replace("img/",dir + "/img/")
      fw.write(data+"\n\n")
      data = re.sub(r'\!\[.*\]\((.*)\)',r'図:\1',data)
      data = re.sub(r'<img src=\"(.*)\">',r'図:\1',data)
      fwt.write(data+"\n\n")
      f.close()
   except:
      pass
fr.close()
fw.close()
fwt.close()
