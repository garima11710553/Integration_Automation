import shutil, os, json, sys

stic='/Users/garimsin/Downloads/Theme/Sticker'

os.chdir(stic)
for file in os.listdir(stic):
    if file !=".DS_Store":
        with open(file) as fname:
            d = json.load(fname)
            temp = list()
            for i in range(0,len(d['CollageStateSticker'])):
                if d['CollageStateSticker'][i]['StickerStateStyle'] == "Birthday_EA_001_5":
                    print(file)
                    stickerDict = {
                                        "StickerStateNCFrame":  d['CollageStateSticker'][i]["StickerStateNCFrame"],
                                        "StickerStatePreviousPanPoint": {
                                            "x": d['CollageStateSticker'][i]["StickerStatePreviousPanPoint"]["x"],
                                            "y": d['CollageStateSticker'][i]["StickerStatePreviousPanPoint"]["y"]
                                        },
                                        "StickerStatePreviousRotation": 1,
                                        "StickerStatePreviousScale": 0,
                                        "StickerStateRotationAngle": 0,
                                        "StickerStateScale": 1,
                                        "StickerStateStickerCustomSticker": d['CollageStateSticker'][i]["StickerStateStickerCustomSticker"],
                                        "StickerStateStyle": d['CollageStateSticker'][i]["StickerStateStyle"],
                                        "StickerStateZorder": 95
                                    }
                    temp.append(stickerDict)
                else:
                    temp.append(d['CollageStateSticker'][i])

        with open(file,"w") as fname:
            stickerDes = {"CollageStateSticker" : temp}
            json.dump(stickerDes,fname,indent=3)
