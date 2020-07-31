import os, json

path = "/Users/garimsin/Documents/Integration/Server Upload 3/temp"
path_localized_file = "/Users/garimsin/Documents/Integration/Server Upload 3"
os.chdir(path)
asp=["1X1","3X4","4X3","9X16","16X9"]

themes=[
    "BBQ_JD_002",
    "BBQ_EC_004",
]


Localization_list=list()
for theme in themes:
    for cell_count in range(1,10):
        for aspect in asp:
            file_name = "Text"+theme+"_"+str(cell_count)+"_"+aspect+".json"
            if os.path.exists(file_name):
                with open(file_name) as fname:
                    d = json.load(fname)
                    for j in range(0,len(d["CollageStateText"])):
                        text=d["CollageStateText"][j]["TextStateContent"]
                        if text not in Localization_list:
                            Localization_list.append(text)
            else:
                print(file_name)

os.chdir(path_localized_file)
localized_text = list()
for text in Localization_list:
    localized_text.append('"' + repr(text) + '"' + '=' + '"' + repr(text) + '"') 

with open("localize_string.txt","w") as fname:
    fname.writelines(localized_text)

Intermediate_string=str()
stringToWrite=str()
count=0
with open("localize_string.txt","r") as fname:
    Intermediate_string = fname.read()
for i in range(0,len(Intermediate_string)):
    if Intermediate_string[i]!="'":
        if count==4:
            stringToWrite=stringToWrite+';\n'
            count=0
        stringToWrite=stringToWrite+Intermediate_string[i]
    if Intermediate_string[i]=='"':
        count=count+1
stringToWrite=stringToWrite+";"
with open("localize_string.txt","w") as fname:
    fname.write(stringToWrite)