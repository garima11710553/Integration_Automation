import os, json

file='/Users/garimsin/Documents/Integration/scripts/Layouttest1s_3_1X1.json'
al=4
ab=3
if os.path.exists(file):
    d=dict()
    with open(file) as fname:
            d = json.load(fname)
            #print(d)
            for c in range(0,len(d["CollageStateGCells"])):
                            #print(d["CollageStateGCells"][c]["CellStateCellMask"])
                            #print(len(d["CollageStateGCells"][c]["CellStateCellMask"]))
                            for n in range(0,len(d["CollageStateGCells"][c]["CellStateCellMask"])):
                                #print(n)
                                #print(d["CollageStateGCells"][c]["CellStateCellMask"])
                                #print(len(d["CollageStateGCells"][c]["CellStateCellMask"]))
                                temp={}
                               # print(d["CollageStateGCells"][c]["CellStateCellMask"][n])
                                points=d["CollageStateGCells"][c]["CellStateCellMask"][n].keys()
                                #print(points)
                                z=0
                                #print(d["CollageStateGCells"][c]["CellStateCellMask"][n])
                                for m in points:
                                    if m == "cmd" :
                                        if d["CollageStateGCells"][c]["CellStateCellMask"][n][m] == "move":
                                            temp["TYPE"] = 0
                                        elif d["CollageStateGCells"][c]["CellStateCellMask"][n][m] == "addLine":
                                            temp["TYPE"] = 1
                                        elif d["CollageStateGCells"][c]["CellStateCellMask"][n][m] == "addCurve":
                                            temp["TYPE"] = 3
                                        else:
                                            temp["TYPE"] = 2
                                    elif m[0:2] == "cp":
                                        pt=d["CollageStateGCells"][c]["CellStateCellMask"][n][m][0]
                                        if pt > 1.15:
                                            pt=pt/830
                                        temp["POINT"+str(int(m[2])-1)+"x"]=pt
                                        pt=d["CollageStateGCells"][c]["CellStateCellMask"][n][m][1]
                                        if pt > 1.15:
                                            pt=pt/830
                                        temp["POINT"+str(int(m[2])-1)+"y"]=pt
                                        z=z+1
                                    elif m == "pts":
                                        pt=d["CollageStateGCells"][c]["CellStateCellMask"][n][m][0]
                                        if pt > 1.15:
                                            pt=pt/830
                                        temp["POINT"+str(z)+"x"]=pt
                                        pt=d["CollageStateGCells"][c]["CellStateCellMask"][n][m][1]
                                        if pt > 1.15:
                                            pt=pt/830
                                        temp["POINT"+str(z)+"y"]=pt
                                    elif m == "TYPE":
                                        temp["TYPE"]=d["CollageStateGCells"][c]["CellStateCellMask"][n][m]
                                    elif m[0:5] == "POINT" and m[-1] == "x":
                                        pt=d["CollageStateGCells"][c]["CellStateCellMask"][n][m]
                                        if pt > 1.15:
                                            pt=pt/830
                                        temp[m]=pt
                                    elif m[0:5] == "POINT" and m[-1] == "y":
                                        pt=d["CollageStateGCells"][c]["CellStateCellMask"][n][m]
                                        if pt > 1.15:
                                            pt=(pt*al)/(830*ab)
                                        temp[m]=pt
                                d["CollageStateGCells"][c]["CellStateCellMask"][n]=temp
                            #dt={"TYPE": 4}
                            #d["CollageStateGCells"][c]["CellStateCellMask"].append(dt)
    with open('cococ.json',"w") as fname:
        
        json.dump(d,fname,indent=3)