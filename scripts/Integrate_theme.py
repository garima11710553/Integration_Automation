import shutil, os, json, sys

# path of the theme assets folder
p1="/Users/garimsin/Downloads/Theme"
# path of psx-ios
psx="/Users/garimsin/Documents/psx-ios"
t="/PSExpress/Classes/Collage/ThemeAssets"
sti="/thirdparty/adobe/PSXCommonFeatures/resources/text/stickers/COLLAGE"
pat="/PSExpress/PatternsTiles"
#p="/Users/garimsin/Documents/Integration/ThemeAssets"
#ps="/Users/garimsin/Documents/Integration/COLLAGE"
# p=psx+t
# ps=psx+sti
# pp=psx+pat
p=p1+"/Final_Folder"
#os.mkdir(p1+"/Background")
os.mkdir(p)
pattern_name=""
theme=""
allFiles = list()
sticker_dict=dict()
missing=list()
#absent stickers
ab=dict()
destFolder = ""
#needed assets
Asset_need=list()
os.chdir(p)
def rename_pattern():
    global pattern_name
    os.chdir(p1+'/Background')
    l=os.listdir(p1+'/Background')
    #count=os.listdir(pp)
    #print(len(count))
    for i in l:
        if i !=".DS_Store":
            new_name=theme+"Pattern"+"@3x.jpg"
            allFiles.append(new_name)
            os.rename(i,new_name)
            with open(p1+'/Theme/Theme'+theme+'.json') as fname:
                d = json.load(fname)
                d["CollageStatePattenImage"]=new_name
            with open(p1+'/Theme/Theme'+theme+'.json',"w") as fname:
                json.dump(d,fname,indent=3)
            pattern_name = new_name

def get_theme_name():
    global theme
    os.chdir(p1+'/Theme')
    l=os.listdir(p1+'/Theme')
    for i in l:
        if i !=".DS_Store":
            theme=i[5:]
            theme=theme[:-5]
            allFiles.append(i)
            with open(i) as fname:
                d = json.load(fname)
                d["CollageTextDescription"]="Text"+theme
                d["CollageStickerDescription"]="Sticker"+theme
                d["CollageLayoutDescription"]="Layout"+theme
            with open(i,"w") as fname:
                json.dump(d,fname,indent=3)
def copy_files(filetype):
    global theme
    if filetype == "Layout":
        src=p1+"/Layout/"
        #dest=p+"/LayoutDescriptions/Layout"+theme
        dest=p+"/"
        #if "Layout"+theme not in os.listdir(p+"/LayoutDescriptions"):
         #   os.mkdir(dest)
        dest=dest+"/"
    elif filetype == "need":
    #elif filetype == "assets":
        src=p1+"/"+filetype+"/"
        #dest=ps+"/"
        dest=p+"/"
    elif filetype == "Background":
        src=src=p1+"/"+filetype+"/"
        #dest=pp+"/"
        dest=p+"/"
    else :
        src=p1+"/"+filetype+"/"
        #dest=p+"/"+filetype+"Descriptions/"
        dest=p+"/"
    l=os.listdir(p1+"/"+filetype)
    for i in l:
        if i !=".DS_Store":
            '''
            if i.startswith('Layout') or i.startswith('Sticker') or i.startswith('Text'):
                if i[-8:-5]!='1X1':
                    #print(i)
                    continue
            
            if i.startswith('Layout'):
                os.chdir(src+i)
                for j in os.listdir(src+i):
                    #src=src+i+'/'
                    if j !=".DS_Store":
                        source=src+i+'/'+j
                        destination=dest+j
                        #print(source,destination)
                        shutil.copyfile(source, destination)
            else:
            '''   
            source=src+i
            destination=dest+i
            #print(source,destination)
            shutil.copyfile(source, destination)

def convert_to_json(path):
    os.chdir(path)
    l=os.listdir(path)
    for i in l:
        if i !=".DS_Store":
            if i[-5:] == "plist":
                file=i[:-5]+'json'
                b="plutil -convert json "+i+" -o "+file
                os.system(b)
                os.remove(i)
                with open(file) as fname:
                    d = json.load(fname)
                with open(file,"w") as fname:
                    json.dump(d,fname,indent=3)

def change_inside_content(asset_file):
    s=asset_file.split(".")
    with open(asset_file) as fname:
        d = json.load(fname)
        d["item"]["name"]=s[0]
        d["item"]["children"]["items"][0]["svg_props"]["file"]=s[0]
    with open(asset_file,"w") as fname:
        json.dump(d,fname,indent=3)

def change_StickerDescriptionFile_content(file):
    with open(file) as fname:
            f=1
            #if file[-8:-5] == '1X1':
            #    f=1
            d = json.load(fname)
            dn = d['CollageStateSticker']
            for i in range(0,len(dn)):
                old_name = d['CollageStateSticker'][i]['StickerStateStyle']
                if old_name in sticker_dict.keys():
                    new_name = sticker_dict[old_name]
                    d['CollageStateSticker'][i]['StickerStateStyle']=new_name
                    if f == 1:
                        if new_name not in Asset_need:
                            Asset_need.append(new_name)
                else:
                    #print(file)
                    if old_name in ab.keys():
                            if file not in ab[old_name]:
                                ab[old_name].append(file)
                    else:
                        ab[old_name]=[file]
                    if old_name not in missing:
                        missing.append(old_name)
    with open(file,"w") as fname:
            json.dump(d,fname,indent=3)

def renameing(category):
    os.chdir(p1+'/'+category)
    l=os.listdir(p1+'/'+category)
    if category == 'Layout' or category == 'Sticker' or category == 'Text':
        types=['Layout','Sticker','Text']
        for i in l:
            if i !=".DS_Store":
                for t in types:
                    if i.startswith(t):
                        new_name=t+theme+'_'+i[i.rindex('_')-1:]
                        allFiles.append(new_name)
                        os.rename(i,new_name)
                        break
    elif category == 'assets':
        j=1
        k=1
        l.sort()
        for i in l:
            if i !=".DS_Store":
                if i.split(".")[1]=="json":
                    sticker_dict[i.split(".")[0]]=theme+'_'+str(k)
                    os.rename(i,theme+'_'+str(k)+".json")
                    change_inside_content(theme+'_'+str(k)+".json")
                    k=k+1
                    allFiles.append(theme+'_'+str(k)+".json")
                else:
                    os.rename(i,theme+'_'+str(j)+".svg")
                    j=j+1
                    allFiles.append(theme+'_'+str(j)+".svg")

def check_missing_files(category):
    os.chdir(p1+'/'+category)
    l=os.listdir(p1+'/'+category)
    aspect=['1X1','3X4','4X3','9X16','16X9']
    for i in range(1,10):
        for asp in aspect:
            file=category+theme+'_'+str(i)+'_'+asp+'.json'
            old_name=category+theme+'_'+str(i)+'_'+asp+'.json'
            if file not in l:
                missing.append(old_name)

def layout_verify(file):
    flag=0
    with open(file) as fname:
            txt=file[:-5]
            abreath=int(txt[txt.rindex('X')+1:])
            alength=int(txt[txt.rindex('_')+1:txt.rindex('X')])
            d = json.load(fname)
            for i in range(0,len(d["CollageStateGCells"])):
                #d["CollageStateGCells"][i]["CellStateViewProps"]["NORMALIZED_CONTENT_OFFSET"]['x']=0
                #d["CollageStateGCells"][i]["CellStateViewProps"]["NORMALIZED_CONTENT_OFFSET"]['y']=0
                for j in range(0,len(d["CollageStateGCells"][i]["CellStateCellMask"])):
                    for k in d["CollageStateGCells"][i]["CellStateCellMask"][j].keys():
                        if k.endswith('x'):
                            if  d["CollageStateGCells"][i]["CellStateCellMask"][j][k] > 1.5 or d["CollageStateGCells"][i]["CellStateCellMask"][j][k] < -1.5:
                                if alength>=abreath:
                                    d["CollageStateGCells"][i]["CellStateCellMask"][j][k]=d["CollageStateGCells"][i]["CellStateCellMask"][j][k]/830
                                else:
                                    d["CollageStateGCells"][i]["CellStateCellMask"][j][k]=d["CollageStateGCells"][i]["CellStateCellMask"][j][k]*abreath/(880*alength)
                                flag=1
                        if k.endswith('y'):
                            if  d["CollageStateGCells"][i]["CellStateCellMask"][j][k] > 1.5 or d["CollageStateGCells"][i]["CellStateCellMask"][j][k] < -1.5:
                                if alength>=abreath:
                                    d["CollageStateGCells"][i]["CellStateCellMask"][j][k]=d["CollageStateGCells"][i]["CellStateCellMask"][j][k]*alength/(830*abreath)
                                else:
                                    d["CollageStateGCells"][i]["CellStateCellMask"][j][k]=d["CollageStateGCells"][i]["CellStateCellMask"][j][k]/880
                                flag=1
    if flag == 1:
        '''
        print(file)
        '''
    with open(file,"w") as fname:
            json.dump(d,fname,indent=3)

def bound(mask_points, frame):
    x, y, h, w = frame['x'], frame['y'], frame['h'], frame['w']
    maxx, minx, maxy, miny = sys.float_info.min, sys.float_info.max , sys.float_info.min , sys.float_info.max
    for point in mask_points:
        flag = False
        for k,v in point.items():
            if k.endswith('x'):
                flag = True
                v = x + v * w
                maxx = max(maxx, v)
                minx = min(minx, v)
                point[k] = v
            elif k.endswith('y'):
                flag = True
                v = y + v * h
                maxy = max(maxy, v)
                miny = min(miny, v)
                point[k] = v
    if flag or maxx < 0 or minx > 1 or maxy < 0 or miny > 1:
        print(maxx,maxy)
        print("raise AssertionError('Frame bounds are not coming proper')")    
    new_width = maxx - minx
    new_length = maxy - miny
    return minx, miny, new_width, new_length

def update_mask(mask_points, frame):
    x, y, h, w = frame['x'], frame['y'], frame['h'], frame['w']
    for point in mask_points:
        for k,_ in point.items():
            if k.endswith('x'):
                point[k] = (point[k] - x) / w
                if point[k] < 0 or point[k] > 1:
                    raise AssertionError('Mask bounds relative to frame are not coming proper')    
            elif k.endswith('y'):
                point[k] = (point[k] - y) / h
                if point[k] < 0 or point[k] > 1:
                    raise AssertionError('Mask bounds relative to frame are not coming proper')    
    return
def Layout_bound():
    cnt = 0
    #files = layout files of {theme}
    files = os.listdir(p1+'/Layout')
    for fl in files:
        #taking only files in the format of "Layout(.*?).json"
        if fl.startswith('.') or not fl.startswith('Layout') or not fl.endswith('.json'):
            continue
        #print(fl)
        layout_verify(p1+'/Layout/'+fl)
        json_data = open(p1+'/Layout/'+fl, 'r').read()
        parsed_json = (json.loads(json_data))
        if 'CollageStateGCells' in parsed_json:
            #cells = no_of_cells in layout
            cells = parsed_json['CollageStateGCells']
            for cell in cells:
                frame = cell['CellStateNCFrame']
                if 'CellStateCellMask' in cell:
                    frame['x'], frame['y'] , frame['w'], frame['h'] = bound(cell['CellStateCellMask'], frame)
                    update_mask(cell['CellStateCellMask'], frame)
                else:
                    print("CHECK ONCE")
                    print(f'CellStateCellMask key in not present in {theme}/{fl} file, It is not an error, but check the file once')
            cnt += 1
            open(p1+'/Layout/'+fl, 'w').write(json.dumps(parsed_json, indent=4, sort_keys=True))
        else:
            print(fl+ 'is not proper json file describing a layout, check it once as CollageStateGCells key not present in this json file')
    print(cnt, 'no of layout files bounded, Thanks :)')

def rename_in_psx(category):
    path=p+"/"+category+"Descriptions"
    if category == 'Layout':
        path=path+"/Layout"+theme
    os.chdir(path)
    temp=os.listdir(path)
    for i in range(1,10):
        old=category+theme+str(i)+'_1X1.json'
        new_name=category+theme+str(i)+'.json'
        if old in temp:
            os.rename(old,new_name)


def required_stickers():
    src=p1+'/assets/'
    dest=p1+'/need'
    os.mkdir(dest)
    dest=dest+'/'
    #print(Asset_need)
    for i in Asset_need:
        svg=i+'.svg'
        jso=i+'.json'
        if i not in missing:
            source=src+svg
            destination=dest+svg
            shutil.copyfile(source, destination)
            source=src+jso
            destination=dest+jso
            shutil.copyfile(source, destination)


#convert all plist files to json
convert_to_json(p1+'/Layout')
convert_to_json(p1+'/Sticker')
convert_to_json(p1+'/Text')
convert_to_json(p1+'/Theme')
#modify theme.json file
get_theme_name()
 
if os.path.exists(p1+'/Background'):
    #rename pattern
    rename_pattern()

renameing('assets')

#changing the mapping of stickers in StickerDescriptionFiles
os.chdir(p1+'/Sticker')
l=os.listdir(p1+'/Sticker')
for file in l:
    if file !=".DS_Store":
        change_StickerDescriptionFile_content(file)

renameing('Layout')
renameing('Sticker')
renameing('Text')


#check for missing description files
check_missing_files('Layout')
check_missing_files('Sticker')
check_missing_files('Text')


print(" ")
print("MISSING ASSETS-")
if len(missing)>0:
    for i in missing:
        print(i)
        if i.startswith('Layout') or i.startswith('Sticker') or i.startswith('Text'):
            continue
        else:
            k=ab[i]
            k.sort()
            print('Used in files:')
            for j in k:
                print(j)
        print(' ')
        print(' ')
    print(' ')
else:
    print('NONE')

required_stickers()

#bounding the cells in layout description files
Layout_bound()

if len(missing)==0 or len(missing)>0:

    print(' ')
    print("COPYING...")

    # move theme description file
    copy_files("Theme")
    #move sticker description files
    copy_files("Sticker")
    #move text description files
    copy_files("Text")
    #move layout description files
    copy_files("Layout")
    #move stickers to COLLAGE
    copy_files("need")
    if os.path.exists(p1+'/Background'):
        #move pattern tiles
        copy_files("Background")
    '''
    os.chdir("/Users/garimsin/Documents/psx-ios/PSExpress/Classes/FoldableTool/ContentProvider/NewContent_Batch_20_13_0")
    category=theme[:theme.index('_')]
    file='themes_'+category+'.json'
    temp=list()
    if os.path.exists(file):
        with open(file) as fname:
            temp = json.load(fname)
    with open(file,"w") as fname:
        d={"effect_id": "Theme"+theme, "name": category[0]+str(len(temp)+1), "version": "1", "thumbnail_id": "CollageTheme"+category, "is_paid": 1,"files": allFiles}
        temp.append(d)
        json.dump(temp,fname,indent=3)
    '''

print('     ')
print("theme integrated ",theme)
# if len(pattern_name) > 0:
#     print('     ')
#     print("make an entry in CollageMainViewController in pattern2 array-  ",pattern_name)
#     print('     ')
