import shutil, os, json
import xlrd
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
#
l=list()
Keys=["CSBCo","CSCo","CSGCo","CSPat"]
excel_column=['B','C','D','E']
#path of theme asset folder
p1='/Users/garimsin/Documents/psx-ios/PSExpress/Classes/Collage/ThemeAssets'
os.chdir(p1+'/ThemeDescriptions')
l=os.listdir(p1+'/ThemeDescriptions')
a='A'+str(1)
c= sheet[a]
c.value="THEME"
a='B'+str(1)
c= sheet[a]
c.value="CSBCo"
a='C'+str(1)
c= sheet[a]
c.value="CSCo"
a='D'+str(1)
c= sheet[a]
c.value="CSGCo"
a='E'+str(1)
c= sheet[a]
c.value="CSPat"
for z in range(0,len(l)):
    file=l[z]
    if file != ".DS_Store":
        if os.path.exists(file):
            with open(file) as fname:
                    print(file)
                    a1='A'+str(z+2)
                    c1= sheet[a1]
                    theme=file[5:]
                    theme=theme[:-5]
                    c1.value=theme
                    d = json.load(fname)
                    desc=d.keys()
                    desc= list(desc)
                    for k in range(0,len(Keys)):
                        #print()
                        if Keys[k] in desc:
                            #print(k)
                            a=excel_column[k]+str(z+2)
                            c= sheet[a]
                            val=str(d[Keys[k]])
                            c.value= val
                            #print(d[Keys[k]])

wb.save("/Users/garimsin/Documents/Integration/scripts/size.xlsx")