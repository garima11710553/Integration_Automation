import os
path="/Users/garimsin/Downloads/PlayWithSVG/play_with_SVG/masterSVGs/main/Sports_EK_003/MasterSVGs"
os.chdir(path)
l=os.listdir(path)

for file in l:
    if file != ".DS_Store":
        s = str()
        c=0
        print(file)
        with open(file) as fname:
            s=fname.read()
    
        f=s.find('<polygon') 
        while f>-1:
            if s.find('id',f) == (f+9):
                s=s[0:s.find('id',f)+3]+'"__cell__"'+s[s.find('"',s.find('id',f)+5)+1:]
            else:
                s=s[0:f+9]+'id = "__cell__" '+s[f+9:]
            f=s.find('<polygon',f+10)
            c=c+1
        '''
        f=s.find('<path') 
        while f>-1:
            s=s[0:f]+'<polygon id="_x5F__x5F_cell_x5F__x5F_"'+s[f+5:]
            f=s.find('<path',f+10)
            c=c+1
        '''
        with open(file,"w") as fname:
            fname.write(s)
            print(c)