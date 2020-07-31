import os, json

path="/Users/garimsin/Documents/Integration/texttemppp"
os.chdir(path)
l=os.listdir(path)

for file in l:
    if file != '.DS_Store':
        print(file)
        with open(file) as fname:
            d = json.load(fname)
            for j in range(0,len(d["CollageStateText"])):
                #print(d["CollageStateText"][j]["TextStateContent"])
                #if d["CollageStateText"][j]["TextStateFont"] == "BickhamScriptStd-Regular":
                #    d["CollageStateText"][j]["TextStateNCFrame"]["h"]=float(d["CollageStateText"][j]["TextStateNCFrame"]["h"]*(1.5))
                old_text=d["CollageStateText"][j]["TextStateContent"]
                new_text=old_text.upper()
                if old_text == "T   I   M   E         T   O      P   A   R  T   Y   !":
                    new_text=""
                    #d["CollageStateText"][j]["TextStateRotationAngle"]=d["CollageStateText"][j]["TextStateRotationAngle"]*.50
                    d["CollageStateText"][j]["TextStateNCFrame"]["x"] = d["CollageStateText"][j]["TextStateNCFrame"]["x"] + float(d["CollageStateText"][j]["TextStateNCFrame"]["w"]/16)
                print(old_text)
                print(new_text)
                if new_text != "":
                    d["CollageStateText"][j]["TextStateContent"]=new_text
            #d["CollageStateText"][1]["TextStateNCFrame"]["x"]=d["CollageStateText"][0]["TextStateNCFrame"]["x"]+d["CollageStateText"][0]["TextStateNCFrame"]["w"]-d["CollageStateText"][1]["TextStateNCFrame"]["w"]
        with open(file,"w") as fname:
            json.dump(d,fname,separators=(',', ':'))
            print('file done')
            