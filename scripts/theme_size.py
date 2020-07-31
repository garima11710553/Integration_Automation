import shutil, os, json
import xlrd
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
#
l=[ "Birthday_GR_001",
    "Birthday_GR_002",
    "Birthday_EA_001",
    "Birthday_GR_004",
    "Birthday_LC_007",
    "Birthday_EA_002",
    "Birthday_LC_008",
    "Birthday_GR_003",
    "Comic_EK_003",
    "Comic_GR_001",
    "Comic_LC_001",
    "Comic_GR_002",
    "Comic_EK_002",
    "Congratulations_GR_006",
    "Congratulations_LC_001",
    "Congratulations_LC_004",
    "Congratulations_GR_008",
    "Congratulations_EA_002",
    "Congratulations_GR_007",
    "Congratulations_EA_001",
    "Congratulations_GR_005",
    "Congratulations_GR_003",
    "Generic_GR_001",
    "Generic_GR_009",
    "Generic_MSz_002",
    "Generic_MSz_001",
    "Generic_GM_001",
    "Generic_EA_004",
    "Generic_LC_002",
    "Generic_LC_006",
    "Music_EA_001",
    "Music_LC_001",
    "Music_LC_003",
    "Music_GR_003",
    "Music_LC_002",
    "Music_GR_001",
    "Music_EA_002",
    "Party_GR_006",
    "Party_GR_004",
    "Party_GR_008",
    "Party_GR_009",
    "Party_LC_002",
    "Party_GR_001",
    "Party_GM_001",
    "Party_MSz_002",
    "Party_MSz_001",
    "Winter_EA_001",
    "Winter_GR_004",
    "Winter_EA_002",
    "Winter_LC_002",
    "Winter_LC_004",
    "Winter_GR_002",
    "Winter_EA_003",]
p1='/Users/garimsin/Documents/psx-ios/PSExpress/Classes/Collage/ThemeAssets'
p2='/Users/garimsin/Documents/psx-ios/thirdparty/adobe/PSXCommonFeatures/resources/text/stickers/COLLAGE'
p3='/Users/garimsin/Documents/psx-ios/PSExpress/PatternsTiles'

for z in range(0,len(l)):
        theme=l[z]
        s1=0.0
        s2=0.0
        s3=0.0
        s4=0.0
        s5=0.0
        s6=0.0
        s7=0.0
        asset=list()
        #asp=['1X1','3X4','4X3','9X16','16X9']
        asp=['3X4','4X3','9X16','16X9']
        #asp=['1X1']
        pat=''
        os.chdir(p1+'/ThemeDescriptions')
        file='Theme'+theme+'.json'
        if os.path.exists(file):
            with open(file) as fname:
                    d = json.load(fname)
            with open(file,"w") as fname:
                    json.dump(d,fname,separators=(',', ':'))
            size=os.path.getsize(file)
            size=float(size)/1000000
            s1=s1+size
            
            source=p1+'/ThemeDescriptions/'+file
            destination="/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/ThemeDescription/"+file
            shutil.copyfile(source, destination)
            destination2='/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/All_Files/'+file
            shutil.copyfile(source, destination2)

            '''
            with open(file) as fname:
                        d = json.load(fname)
                        if "CollageStatePattenImage" in d.keys():
                            pat=d["CollageStatePattenImage"]
                            os.chdir(p3)
                            if os.path.exists(pat):
                                size=os.path.getsize(pat)
                                size=float(size)/1000000
                                s5=s5+size
                            else:
                                print(pat)
            '''
        else:
            print(file)
        
        os.chdir(p1+'/LayoutDescriptions/Layout'+theme)
        os.mkdir("/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/LayoutDescription/Layout"+theme)
        for i in range(1,10):
            for j in asp:
                file='Layout'+theme+'_'+str(i)+'_'+j+'.json'
                if os.path.exists(file):
                    with open(file) as fname:
                        d = json.load(fname)
                        '''
                        for c in range(0,len(d["CollageStateGCells"])):
                            for n in range(0,len(d["CollageStateGCells"][c]["CellStateCellMask"])):
                                for m in d["CollageStateGCells"][c]["CellStateCellMask"][n].keys():
                                    t=d["CollageStateGCells"][c]["CellStateCellMask"][n][m]
                                    if len(str(t))>6:
                                        t=float(str(t)[0:6])
                                        d["CollageStateGCells"][c]["CellStateCellMask"][n][m]=t
                        '''
                        
                    with open(file,"w") as fname:
                            json.dump(d,fname,separators=(',', ':'))
                    size=os.path.getsize(file)
                    size=float(size)/1000000
                    s2=s2+size
                    
                    source=p1+'/LayoutDescriptions/Layout'+theme+"/"+file
                    destination="/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/LayoutDescription/Layout"+theme+"/"+file
                    shutil.copyfile(source, destination)
                    destination2='/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/All_Files/'+file
                    shutil.copyfile(source, destination2)
                    
                else:
                    print(file)

        os.chdir(p1+'/StickerDescriptions')
        
        for i in range(1,10):
            for j in asp:
                file='Sticker'+theme+'_'+str(i)+'_'+j+'.json'
                if os.path.exists(file):
                    with open(file) as fname:
                        d = json.load(fname)
                        #dn = d['CollageStateSticker']
                        dn = d['CSS']
                        for c in range(0,len(dn)):
                            #name = d['CollageStateSticker'][c]['StickerStateStyle']
                            name = d['CSS'][c]['SSSt']
                            if name not in asset:
                                asset.append(name)
                    with open(file,"w") as fname:
                            json.dump(d,fname,separators=(',', ':'))
                    size=os.path.getsize(file)
                    size=float(size)/1000000
                    s3=s3+size
                    
                    source=p1+'/StickerDescriptions'+"/"+file
                    destination="/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/StickerDescription/"+file
                    shutil.copyfile(source, destination)
                    destination2='/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/All_Files/'+file
                    shutil.copyfile(source, destination2)
                    
                else:
                    print(file)
        
        os.chdir(p1+'/TextDescriptions')
        for i in range(1,10):
            for j in asp:
                file='Text'+theme+'_'+str(i)+'_'+j+'.json'
                if os.path.exists(file):
                    with open(file) as fname:
                        d = json.load(fname)
                    with open(file,"w") as fname:
                            json.dump(d,fname,separators=(',', ':'))
                    size=os.path.getsize(file)
                    size=float(size)/1000000
                    s4=s4+size
                    
                    source=p1+'/TextDescriptions'+"/"+file
                    destination="/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/TextDescription/"+file
                    shutil.copyfile(source, destination)
                    destination2='/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/All_Files/'+file
                    shutil.copyfile(source, destination2)
                    
                else:
                    print(file)

        os.chdir(p2)
        for j in asset:
            file=j+'.svg'
            size=os.path.getsize(file)
            size=float(size)/1000000
            s5=s5+size
            
            source=p2+"/"+file
            destination="/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/Assets/"+file
            shutil.copyfile(source, destination)
            destination2='/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/All_Files/'+file
            shutil.copyfile(source, destination2)
            
            file=j+'.json'
            '''
            with open(file) as fname:
                    d = json.load(fname)
                    #d["item"]["children"]["items"][0]["svg_props"]["flexible_aspect"]=1
            with open(file,"w") as fname:
                    json.dump(d,fname,separators=(',', ':'))
            '''
            size=os.path.getsize(file)
            size=float(size)/1000000
            s7=s7+size
            
            source=p2+"/"+file
            destination="/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/Assets/"+file
            shutil.copyfile(source, destination)
            destination2='/Users/garimsin/Documents/Integration/Server Upload/53_themes_all_aspect/All_Files/'+file
            shutil.copyfile(source, destination2)
            
        s6=len(asset)

        k=z+1
        print(k,i)
        a1='A'+str(k)
        c1= sheet[a1]
        a2 = 'B'+str(k)
        c2=sheet[a2]
        a3 = 'C'+str(k)
        c3=sheet[a3]
        a4='D'+str(k)
        c4= sheet[a4]
        a5 = 'E'+str(k)
        c5=sheet[a5]
        a6 = 'F'+str(k)
        c6=sheet[a6]
        a7 = 'G'+str(k)
        c7=sheet[a7]
        a8 = 'H'+str(k)
        c8=sheet[a8]
        c1.value=theme
        c2.value=s1
        c3.value=s2
        c4.value=s3
        c5.value=s4
        c6.value=s5
        c7.value=s7
        c8.value=s6
        print(asset)
        print(pat)
        print(s1,s2,s3,s4,s5,s6)
        

wb.save("/Users/garimsin/Documents/Integration/scripts/size.xlsx")
