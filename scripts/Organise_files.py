import os
import shutil
p='/Users/garimsin/Downloads/Theme'
os.chdir(p)
l1=os.listdir(p)
no=['Text','Layout','Sticker','assets','Background','Theme','Additional']
os.mkdir(p+'/Layout')
os.mkdir(p+'/Sticker')
os.mkdir(p+'/Text')
os.mkdir(p+'/Theme')
os.mkdir(p+'/assets')
os.mkdir(p+'/Background')
os.mkdir(p+'/Additional')
count_duplicate = 0
themefileCount=0
def arrange(lnew,p):
    for l in lnew:
        if l in no:
            continue
        p2=p+'/'+l
        if os.path.isdir(p2):
            arrange(os.listdir(p2),p2)
        else:
            correct(l,p2)
def correct(item,path):
    global p
    global count_duplicate
    global themefileCount
    if item.startswith("Layout"):
        dest=p+'/Layout'
    elif item.startswith("Sticker"):
        dest=p+'/Sticker'
    elif item.startswith("Text"):
        dest=p+'/Text'
    elif item.startswith("Theme"):
        #print(item)
        themefileCount= themefileCount+1
        dest=p+'/Theme'
    elif item.endswith(".svg") or item.endswith(".json"):
        if item.startswith("0CustomLayout"):
            dest=p+'/Additional'
        else:
            dest=p+'/assets'
    elif item.endswith(".jpeg"):
        dest=p+'/Background'
    else:
        dest=p+'/Additional'
    test=os.listdir(dest)
    c=list()
    for i in test:
        c.append(i.upper())
    if item.upper() in c:
        count_duplicate = count_duplicate+1
        #print(item)
    else:
        if dest.endswith("Theme"):
            if themefileCount == 1:
                shutil.move(path,dest)
        else:
            shutil.move(path,dest)

arrange(l1,p)

print("FILES ORGANIZED")

print("Duplicate files = ", count_duplicate)