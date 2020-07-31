import shutil, os, json, sys

src='/Users/garimsin/Documents/Integration/ABC/Layout'
os.chdir(src)
themes=os.listdir(src)
print(len(themes))
c=0
for theme in themes:
    if os.path.isdir(theme):
        c=c+1
        print(theme)
        l=os.listdir(src+'/'+theme)
        os.chdir(src+'/'+theme)
        
        for file in l:
            if file !=".DS_Store":
                print(file)
                with open(file) as fname:
                    d = json.load(fname)
                    dn=d["CollageStateGCells"]
                    for i in range(0,len(dn)):
                        d["CollageStateGCells"][i]["CellStateViewProps"]["NORMALIZED_CONTENT_OFFSET"]['x']=0
                        d["CollageStateGCells"][i]["CellStateViewProps"]["NORMALIZED_CONTENT_OFFSET"]['y']=0
                        print(d["CollageStateGCells"][i]["CellStateViewProps"]["NORMALIZED_CONTENT_OFFSET"])
                with open(file,"w") as fname:
                    json.dump(d,fname,indent=3)
        os.chdir(src)
print(c)