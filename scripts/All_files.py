import os
import shutil
path_folder='/Users/garimsin/Documents/Integration/Server Upload 2/demo_layouts_data'
dest= '/Users/garimsin/Documents/Integration/Server Upload 3/temp'
os.chdir(path_folder)
list_files=os.listdir(path_folder)
count_duplicate = 0
themefileCount=0
themes_list =[
    "Thank_you_GM_001",
    "Thank_you_LC_002",
]

def arrange(list_current_path_files,path_folder,theme):
    for file in list_current_path_files:
        path=path_folder+'/'+file
        if os.path.isdir(path):
            arrange(os.listdir(path),path,theme)
        else:
            if theme in file:
                correct(file,path)
def correct(file,path):
    global path_folder
    global dest
    global themefileCount
    if 'Theme' in file:
        themefileCount = themefileCount+1
    shutil.move(path,dest)

for theme in themes_list:
    arrange(list_files,path_folder,theme)


print("Total themes - ", themefileCount)