import os, json

path="/Users/garimsin/Documents/Integration/Winter_LC_004/Text"
os.chdir(path)
l=os.listdir(path)

for file in l:
    if file != '.DS_Store':
        with open(file) as fname:
            temp=dict()
            temp["CollageStateText"]=list()
            d = json.load(fname)
            print(file)
            #print(d["CollageStateText"])
            for j in range(0,len(d["CollageStateText"])):
                #print(d["CollageStateText"][j])
                if d["CollageStateText"][j]["TextStateContent"] == "Turn it\rUP":
                    turn={
                            "TextStateAlignment": "PARAGRAPH_RIGHT",
                            "TextStateColor": {
                                "B": 1.0,
                                "G": 1.0,
                                "R": 1.0
                            },
                            "TextStateColorIdentifier": 99999,
                            "TextStateContent": "Turn it",
                            "TextStateFont": "BickhamScriptStd-Regular",
                            "TextStateIsModelDirty": 4,
                            "TextStateNCFrame": {
                                "h": d["CollageStateText"][j]["TextStateNCFrame"]["h"],
                                "w": d["CollageStateText"][j]["TextStateNCFrame"]["w"],
                                "x": d["CollageStateText"][j]["TextStateNCFrame"]["x"],
                                "y": d["CollageStateText"][j]["TextStateNCFrame"]["y"]
                            },
                            "TextStateOpacity": 1,
                            "TextStatePreviousPanPoint": {
                                "x": 0,
                                "y": 0
                            },
                            "TextStatePreviousRotation": 0,
                            "TextStatePreviousScale": 0,
                            "TextStateRotationAngle": 0.0,
                            "TextStateScale": 1,
                            "TextStateStrokeColor": {
                                "B": 1,
                                "G": 1,
                                "R": 1
                            },
                            "TextStateStrokeWidth": 0.0,
                            "TextStateStyle": "2ctstyle",
                            "TextStateZorder": d["CollageStateText"][j]["TextStateZorder"]
                        }
                    up={
                            "TextStateAlignment": "PARAGRAPH_RIGHT",
                            "TextStateColor": {
                                "B": 1.0,
                                "G": 1.0,
                                "R": 1.0
                            },
                            "TextStateColorIdentifier": 99999,
                            "TextStateContent": "UP",
                            "TextStateFont": "UtopiaStd-Bold",
                            "TextStateIsModelDirty": 4,
                            "TextStateNCFrame": {
                                "h": d["CollageStateText"][j]["TextStateNCFrame"]["h"]/2,
                                "w": d["CollageStateText"][j]["TextStateNCFrame"]["w"],
                                "x": d["CollageStateText"][j]["TextStateNCFrame"]["x"],
                                "y": d["CollageStateText"][j]["TextStateNCFrame"]["y"]+d["CollageStateText"][j]["TextStateNCFrame"]["h"]/2
                            },
                            "TextStateOpacity": 1,
                            "TextStatePreviousPanPoint": {
                                "x": 0,
                                "y": 0
                            },
                            "TextStatePreviousRotation": 0,
                            "TextStatePreviousScale": 0,
                            "TextStateRotationAngle": 0.0,
                            "TextStateScale": 1,
                            "TextStateStrokeColor": {
                                "B": 1,
                                "G": 1,
                                "R": 1
                            },
                            "TextStateStrokeWidth": 0.0,
                            "TextStateStyle": "2ctstyle",
                            "TextStateZorder": d["CollageStateText"][j]["TextStateZorder"]
                        }
                    temp["CollageStateText"].append(turn)
                    temp["CollageStateText"].append(up)
                else:
                    elt=d["CollageStateText"][j]
                    temp["CollageStateText"].append(elt)
            d=temp
                #d["CollageStateText"][j]["TextStateContent"]=new_text
        with open(file,"w") as fname:
            json.dump(d,fname,indent=3)
            print('file done')
