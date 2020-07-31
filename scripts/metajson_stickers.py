import shutil, os, json, sys

category = "Birthday_"
os.chdir("/Users/garimsin/Documents/Integration/Server Upload/All_Files_all aspect")
l1=os.listdir("/Users/garimsin/Documents/Integration/Server Upload/All_Files_all aspect")

os.chdir("/Users/garimsin/Documents/Integration/Server Upload/meta jsons")

l=list()
c=0
for i in l1:
  if category in i or "birthday_" in i:
    if ".svg" in i:
        sticker=i[:-4]
        d={
            "files": [
            sticker+".json",
            sticker+".svg"
            ],
            "name": category[0]+str(c),
            "thumbnail_id": "",
            "is_paid": 0,
            "version": 1,
            "effect_id": sticker
        }
        l.append(d)
        c=c+1

file = "stickers_"+category[:-1]+".json"
with open(file,"w") as fname:
    json.dump(l,fname,indent=3)

print(len(l))