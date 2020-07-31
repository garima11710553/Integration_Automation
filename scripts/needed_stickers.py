import shutil, os, json, sys

src='/Users/garimsin/Documents/Integration/53 themes/COLLAGE'
dest='/Users/garimsin/Documents/Integration/53 themes/Stickers'
stic='/Users/garimsin/Documents/Integration/53 themes/StickerDescriptions'
ln=os.listdir(src)
l=list()
a=list()
b=dict()
os.chdir(stic)
for file in os.listdir(stic):
    if file !=".DS_Store":
        with open(file) as fname:
            d = json.load(fname)
            dn = d['CollageStateSticker']
            for i in range(0,len(dn)):
                if d['CollageStateSticker'][i]['StickerStateStyle'] not in l:
                    l.append(d['CollageStateSticker'][i]['StickerStateStyle'])

for i in l:
    svg=i+'.svg'
    jso=i+'.json'
    if svg in ln and jso in ln:
        source=src+'/'+i+'.svg'
        destination=dest+'/'+i+'.svg'
        shutil.move(source, destination)
        source=src+'/'+i+'.json'
        destination=dest+'/'+i+'.json'
        shutil.move(source, destination)
    else:
        a.append(i)
print()
print('a ',len(a))
print('l ',len(l))

for file in os.listdir(stic):
    if file !=".DS_Store":
        with open(file) as fname:
            c=list()
            d = json.load(fname)
            dn = d['CollageStateSticker']
            for i in range(0,len(dn)):
                if d['CollageStateSticker'][i]['StickerStateStyle'] in a:
                    c.append(d['CollageStateSticker'][i]['StickerStateStyle'])
            if len(c)>0:
                b[file]=c

for k in b.keys():
    print(k,"-",b[k])

for i in a:
    print(i)
