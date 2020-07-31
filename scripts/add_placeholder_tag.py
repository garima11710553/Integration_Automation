import os
path="/Users/garimsin/Downloads/PlayWithSVG/play_with_SVG/masterSVGs/main/Sports_EK_003/MasterSVGs"
os.chdir(path)
l=os.listdir(path)
c=0
for file in l:
    if file != ".DS_Store":
        s = str()
        with open(file) as fname:
            s=fname.read()
        f=s.find('<g id="Placeholder">')
        if f == -1:
            c=c+1
            s=s[:s.find('<polygon')]+'<g id="Placeholder">'+s[s.find('<polygon'):]
            #s=s[:s.find('<path')]+'<g id="Placeholder">'+s[s.find('<path'):]
            s=s[:s.find('</svg>')]+'</g>'+s[s.find('</svg>'):]
        with open(file,"w") as fname:
            fname.write(s)
            print(file)
print(c)
