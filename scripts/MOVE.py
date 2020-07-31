import shutil, os
c=0
l=os.listdir("/Users/garimsin/Documents/Integration/Server Upload/53_themes_files copy")
#src = "abc"
for file in l:
    if file !=".DS_Store":
        src = "/Users/garimsin/Documents/Integration/Server Upload/53_themes_files copy/"+file
        des ="/Users/garimsin/Documents/Integration/Server Upload/All_Files copy/"+file
        shutil.move(src, des)
        c=c+1

print(c)