import os, json

path = "/Users/garimsin/Documents/Integration/Server Upload 3/temp"
os.chdir(path)
asp=["1X1","3X4","4X3","9X16","16X9"]

themes=[
    "BBQ_LC_001",
    "BBQ_GR_002",
    "Valentines_JD_001",
]
counter=0
for theme in themes:
    for cell_count in range(1,10):
        for aspect in asp:
            file_name = "Layout"+theme+"_"+str(cell_count)+"_"+aspect+".json"
            if os.path.exists(file_name):
                with open(file_name) as fname:
                    d = json.load(fname)
                    layout_list=list()
                    for j in range(0,len(d["CollageStateGCells"])):
                        d["CollageStateGCells"][j]["CellStateZorder"]=d["CollageStateGCells"][j]["CellStateZorder"]-60
                        '''
                        temp={
                                "CellStateBackgroundFlag": d["CollageStateGCells"][j]["CellStateBackgroundFlag"],
                                "CellStateCellMask": d["CollageStateGCells"][j]["CellStateCellMask"],
                                "CellStateImageRotation": d["CollageStateGCells"][j]["CellStateImageRotation"],
                                "CellStateNCFrame": {
                                    "h": d["CollageStateGCells"][j]["CellStateNCFrame"]["h"],
                                    "w": d["CollageStateGCells"][j]["CellStateNCFrame"]["w"],
                                    "x": d["CollageStateGCells"][j]["CellStateNCFrame"]["x"],
                                    "y": d["CollageStateGCells"][j]["CellStateNCFrame"]["y"]
                                },
                                "CellStateRotationAngle": d["CollageStateGCells"][j]["CellStateRotationAngle"],
                                "CellStateSuperViewIndexOfSubview": d["CollageStateGCells"][j]["CellStateSuperViewIndexOfSubview"],
                                "CellStateViewProps": d["CollageStateGCells"][j]["CellStateViewProps"],
                                "CellStateZorder": d["CollageStateGCells"][j]["CellStateZorder"]-60,
                                "gridCellMirror": d["CollageStateGCells"][j]["gridCellMirror"],
                                "gridCellSync": d["CollageStateGCells"][j]["gridCellSync"],
                                "gridCellType": d["CollageStateGCells"][j]["gridCellType"],
                                "gridCellVector": d["CollageStateGCells"][j]["gridCellVector"]
                            }
                        layout_list.append(temp)
                    d["CollageStateGCells"]=temp
                    '''
                with open(file_name,"w") as fname:
                    json.dump(d,fname,indent=3)
                    counter=counter+1
            else:
                print('Missing',file_name)

print("Number of files Changed - ",counter)