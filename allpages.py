# -*- coding: utf-8 -*-
UTF8_BOM = bytearray([0xEF, 0XBB, 0XBF])
def strip_bom(s):
    if s.startswith(UTF8_BOM):
        return s[len(UTF8_BOM):]
    return s


fr = open("list.md","r")
with open("all.md",'w'):
 pass
fw = open("all.md",'a')
for line in fr:
   path = line.rstrip("\n")
   dir = path.split("/")[0] 
   try:
      f = open(path,"r")
      data = strip_bom(f.read()).replace("img/",dir + "/img/")
      fw.write(data+"\n\n")
      f.close()
   except:
      pass
fr.close()
fw.close()
