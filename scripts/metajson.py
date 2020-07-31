import shutil, os, json, sys

path_of_folder="/Users/garimsin/Documents/Integration/Server Upload 3/temp"
path_of_psx="/Users/garimsin/Documents/psx-ios"
path_of_metajsons=path_of_psx+"/PSExpress/Classes/FoldableTool/ContentProvider/NewContent_Batch_20_13_0"
themes=list()
#path_of_metajsons="/Users/garimsin/Documents/Integration/Server Upload/meta jsons"
os.chdir(path_of_folder)
files=os.listdir(path_of_folder)
'''
for i in files:
    if i !=".DS_Store":
        if i.startswith('Theme'):
            theme_name=i[:-5]
            theme_name=theme_name[5:]
            themes.append(theme_name)
'''
#themes in required order
themes = [
    "BBQ_JD_002",
    "BBQ_EC_004",
]

print(themes)
print(len(themes))

themes_category_added = dict()
stickers_category_added = dict()
os.chdir(path_of_metajsons)
for theme in themes:
    files_list = list()
    stickers = list()
    for i in files:
        if i !=".DS_Store":
            if theme in i:
                files_list.append(i)
                if i.startswith('Text'):
                    os.chdir(path_of_folder)
                    with open(i,"r") as fname:
                        d = json.load(fname)
                        for j in d["CollageStateText"]:
                            style = j["TextStateStyle"]
                            style=style+".json"
                            if style not in files_list:
                                files_list.append(style)
                    os.chdir(path_of_metajsons)
                elif i.endswith('svg'):
                    stickers.append(i)

    category=theme[:theme.index('_')]
    file = 'themes_'+category+'.json'
    sticker_file = 'stickers_'+category+'.json'
    #adding theme entry
    temp=list()
    if os.path.exists(file):
        with open(file) as fname:
            temp = json.load(fname)
            if category not in list(themes_category_added.keys()):
                themes_category_added[category]=0
            themes_category_added[category]=themes_category_added[category]+1
    else:
        themes_category_added[category]=1
    
    with open(file,"w") as fname:
        d={
            "effect_id": "Theme"+theme, 
            "name": category[0]+str(len(temp)+1), 
            "version": "1",
            "thumbnail_id": "CollageTheme"+category, 
            "is_paid": 1,
            "files": files_list
        }
        temp.append(d)
        json.dump(temp,fname,indent=3)

    #adding stickers entry
    temp=list()
    if os.path.exists(sticker_file):
        with open(sticker_file) as fname:
            temp = json.load(fname)
            if category not in list(stickers_category_added.keys()):
                stickers_category_added[category]=0
    else:
        stickers_category_added[category]=0
    
    with open(sticker_file,"w") as fname:
        for sticker in stickers:
            d={
                    "files": [
                        sticker[:-4]+".json",
                        sticker
                    ],
                    "name": category[0]+str(len(temp)+1),
                    "thumbnail_id": "",
                    "is_paid": 0,
                    "version": 1,
                    "effect_id": sticker[:-4]
                }
            temp.append(d)
            stickers_category_added[category] = stickers_category_added[category]+1
        json.dump(temp,fname,indent=3)

    #adding layout entry
    temp=list()
    for j in range(1,10):
        layout_file = 'layout_themes'+str(j)+'.json'
        with open(layout_file) as fname:
            temp = json.load(fname) 
        with open(layout_file,"w") as fname:
            d = {
                    "effect_id": "Layout"+theme,
                    "name": "L"+str(len(temp)+1),
                    "version": "1",
                    "thumbnail_id": "",
                    "is_paid": 1,
                    "files": [
                        "Layout"+theme+"_"+str(j)+"_1X1.json"
                    ]
                }
            temp.append(d)
            json.dump(temp,fname,indent=3)
    

#theme count entry
file="collage_themes.json"
temp=list()
new_categories=0
new_sticker_category=0
with open(file,"r") as fname:
    temp = json.load(fname)

with open(file,"w") as fname:
    categories_added= themes_category_added.keys()
    categories=list()
    for i in temp:
        categories.append(i["name"])
        if i["name"] in categories_added:
            i["effect_count"]=i["effect_count"]+themes_category_added[i["name"]]
    for i in categories_added:
        if i not in categories:
            new_categories=new_categories+1
            d={
                "category_id": "themes_"+i,
                "name":i ,
                "version": "1",
                "thumbnail_id": "",
                "effect_count": themes_category_added[i]
              }
            temp.append(d)
    json.dump(temp,fname,indent=3)

#sticker count entry
temp=list()
with open("stickers.json","r") as fname:
    temp = json.load(fname)

with open("stickers.json","w") as fname:
    categories_added= stickers_category_added.keys()
    categories=list()
    for i in temp:
        categories.append(i["name"])
        if i["name"] in categories_added:
            i["effect_count"]=i["effect_count"]+stickers_category_added[i["name"]]
    for i in categories_added:
        if i not in categories:
            new_sticker_category=new_sticker_category+1
            d={
                    "category_id": "stickers_"+i,
                    "name": i,
                    "version": "1",
                    "thumbnail_id": "",
                    "effect_count": stickers_category_added[i]
                }
            temp.append(d)
    json.dump(temp,fname,indent=3)

#layout count entry
cell_counts = ["sic","two","three","four","five","six","seven","eight","nine"]
for cell_count in cell_counts:
    temp=list()
    file_name = "collage_layouts_"+cell_count+".json"
    with open(file_name,"r") as fname:
        temp = json.load(fname)
    with open(file_name,"w") as fname:
        temp_write = list()
        for i in temp:
            if i["name"]=="Uncategorised":
                i["effect_count"] = i["effect_count"]+len(themes)
            temp_write.append(i)
        json.dump(temp,fname,indent=3)

temp=list()
file="feature.json"
with open(file,"r") as fname:
    temp = json.load(fname)
with open(file,"w") as fname:
    for i in temp:
        if i["feature_id"]=="collage_themes":
            i["category_count"]=i["category_count"]+new_categories
        if i["feature_id"]=="stickers":
            i["category_count"]=i["category_count"]+new_sticker_category
    json.dump(temp,fname,indent=3)

print("new categories added are",new_categories)
